#!/usr/bin/env python3
"""
Automated content collector for B2B SaaS email marketing research.

Fetches YouTube transcripts and Substack/newsletter articles, generates
sources.md, and creates LinkedIn post templates for each expert.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_DIR = SCRIPT_DIR / "research"
YOUTUBE_DIR = RESEARCH_DIR / "youtube-transcripts"
OTHER_DIR = RESEARCH_DIR / "other"
LINKEDIN_DIR = RESEARCH_DIR / "linkedin-posts"
SOURCES_FILE = RESEARCH_DIR / "sources.md"

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

# ---------------------------------------------------------------------------
# Expert registry — edit platforms/URLs here as needed
# ---------------------------------------------------------------------------
EXPERTS: list[dict[str, Any]] = [
    {
        "name": "Dave Gerhardt",
        "platforms": ["LinkedIn", "YouTube", "Newsletter", "Podcast"],
        "linkedin": "https://www.linkedin.com/in/davegerhardt",
        "youtube": "https://www.youtube.com/@ExitFiveCommunity",
        "newsletter": "https://www.exitfive.com/newsletter",
        "website": "https://www.exitfive.com",
        "podcast": "https://www.exitfive.com/podcast",
    },
    {
        "name": "Jay Schwedelson",
        "platforms": ["LinkedIn", "YouTube", "Newsletter", "Website", "Podcast"],
        "linkedin": "https://www.linkedin.com/in/schwedelson",
        "youtube": "https://www.youtube.com/@schwedelson",
        "newsletter": "https://www.jayschwedelson.com/newsletter",
        "website": "https://www.jayschwedelson.com",
        "podcast": "https://www.jayschwedelson.com/podcast",
        "tools": "https://subjectline.com",
    },
    {
        "name": "Emily Kramer",
        "platforms": ["LinkedIn", "YouTube", "Newsletter", "Podcast"],
        "linkedin": "https://www.linkedin.com/in/emilykramer",
        "youtube": "https://www.youtube.com/@emilykramermkt1",
        "newsletter": "https://newsletter.mkt1.co",
        "website": "https://www.mkt1.co",
        "podcast": "https://newsletter.mkt1.co/s/dear-marketers",
    },
    {
        "name": "Corey Haines",
        "platforms": ["LinkedIn", "Newsletter", "Podcast"],
        "linkedin": "https://www.linkedin.com/in/corey-haines",
        "youtube": None,
        "newsletter": "https://swipefiles.kit.com/profile",
        "website": "https://www.swipefiles.com",
        "podcast": "https://www.swipefiles.com/everything-is-marketing",
    },
    {
        "name": "Chase Dimond",
        "platforms": ["LinkedIn", "YouTube", "Newsletter"],
        "linkedin": "https://www.linkedin.com/in/chasedimond",
        "youtube": "https://www.youtube.com/c/ChaseDimond",
        "newsletter": "https://www.chasedimond.com/newsletter",
        "website": "https://www.chasedimond.com",
    },
    {
        "name": "Kyle Poyar",
        "platforms": ["LinkedIn", "Newsletter"],
        "linkedin": "https://www.linkedin.com/in/kyle-poyar",
        "youtube": None,
        "newsletter": "https://www.growthunhinged.com",
        "website": "https://www.growthunhinged.com/about",
        "notes": "Moved from Substack to beehiiv (Jan 2026). Archive: https://kylepoyar.substack.com",
    },
    {
        "name": "Brendan Hufford",
        "platforms": ["LinkedIn", "Website", "Newsletter"],
        "linkedin": "https://www.linkedin.com/in/brendanhufford",
        "youtube": None,
        "newsletter": "https://growthsprints.beehiiv.com",
        "website": "https://brendanhufford.com",
        "notes": "Growing Up SaaS newsletter; SEO list at https://brendanhufford.com/start",
    },
    {
        "name": "Jaina Mistry",
        "platforms": ["LinkedIn", "Website", "Podcast"],
        "linkedin": "https://www.linkedin.com/in/jainamistry",
        "youtube": None,
        "newsletter": None,
        "website": "https://jainamistry.com",
        "podcast": "https://jainamistry.com/podcast",
        "notes": "No personal newsletter; primary content via LinkedIn and guest appearances.",
    },
    {
        "name": "Eman Ismail",
        "platforms": ["LinkedIn", "Website", "Newsletter", "Podcast"],
        "linkedin": "https://www.linkedin.com/in/eman-i307",
        "youtube": None,
        "newsletter": "https://emancopyco.kit.com/profile",
        "website": "https://www.emancopyco.com",
        "podcast": "https://www.emancopyco.com/podcast",
        "notes": "Newsletter: The Email Rules",
    },
    {
        "name": "Ann Handley",
        "platforms": ["LinkedIn", "Newsletter", "Website"],
        "linkedin": "https://www.linkedin.com/in/annhandley",
        "youtube": None,
        "newsletter": "https://annhandley.com/newsletter",
        "website": "https://annhandley.com",
        "notes": "Newsletter name: Total Annarchy (fortnightly)",
    },
]

# ---------------------------------------------------------------------------
# Content to fetch — verified URLs for initial research collection
# Each entry: {"url": "...", "expert": "Exact name from EXPERTS list"}
# ---------------------------------------------------------------------------
YOUTUBE_URLS: list[dict[str, str]] = [
    {"url": "https://www.youtube.com/watch?v=BMXUXN5t7rU", "expert": "Dave Gerhardt"},
    {"url": "https://www.youtube.com/watch?v=LGwYC-xCnpk", "expert": "Dave Gerhardt"},
    {"url": "https://www.youtube.com/watch?v=P6Nkkj0pjSI", "expert": "Dave Gerhardt"},
    {"url": "https://www.youtube.com/watch?v=QmR5BAeTJsI", "expert": "Jay Schwedelson"},
    {"url": "https://www.youtube.com/watch?v=XwYd2zz3M8s", "expert": "Jay Schwedelson"},
    {"url": "https://www.youtube.com/watch?v=kcWuz_SVsQQ", "expert": "Jay Schwedelson"},
    {"url": "https://www.youtube.com/watch?v=Eg8KjnXlr_A", "expert": "Emily Kramer"},
]

SUBSTACK_URLS: list[dict[str, str]] = [
    {"url": "https://newsletter.mkt1.co/p/episode-1-marketing-requests", "expert": "Emily Kramer"},
    {"url": "https://newsletter.mkt1.co/p/pricing-page-examples", "expert": "Emily Kramer"},
]

# Other public article/newsletter URLs (non-Substack) saved to research/other/
OTHER_URLS: list[dict[str, str]] = [
    {"url": "https://www.exitfive.com/newsletter/141", "expert": "Dave Gerhardt"},
    {"url": "https://www.growthunhinged.com/p/your-guide-to-better-email-nurture", "expert": "Kyle Poyar"},
    {"url": "https://www.demandgenreport.com/industry-news/feature/why-email-newsletters-are-a-b2b-marketing-game-changer/49251/", "expert": "Jaina Mistry"},
    {"url": "https://annhandley.optin.com/newsletter/totalannarchy/Mjg2NDA4OTQ=/ta-201-behind-the-scenes.htm", "expert": "Ann Handley"},
    {"url": "https://www.emancopyco.com/podcast/how-to-do-email-in-2024", "expert": "Eman Ismail"},
]


def slugify(text: str, max_length: int = 80) -> str:
    """Convert text to a filesystem-safe slug."""
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_-]+", "-", slug).strip("-")
    return slug[:max_length] or "untitled"


def ensure_directories() -> None:
    for directory in (RESEARCH_DIR, YOUTUBE_DIR, OTHER_DIR, LINKEDIN_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def extract_youtube_video_id(url: str) -> str | None:
    """Extract a YouTube video ID from common URL formats."""
    patterns = [
        r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})",
        r"youtube\.com/shorts/([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_youtube_title(video_url: str) -> str:
    """Fetch video title via YouTube oEmbed."""
    oembed_url = "https://www.youtube.com/oembed"
    response = requests.get(
        oembed_url,
        params={"url": video_url, "format": "json"},
        headers=REQUEST_HEADERS,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["title"]


def fetch_youtube_transcript(video_id: str) -> str:
    """Fetch and concatenate transcript segments for a video."""
    transcript = YouTubeTranscriptApi().fetch(video_id)
    return "\n\n".join(
        snippet.text.strip() for snippet in transcript if snippet.text.strip()
    )


def save_youtube_transcript(video_url: str, expert_name: str) -> Path | None:
    """Fetch a YouTube transcript and save it as a markdown file."""
    video_id = extract_youtube_video_id(video_url)
    if not video_id:
        print(f"  [skip] Could not parse YouTube video ID from: {video_url}")
        return None

    try:
        title = get_youtube_title(video_url)
        transcript = fetch_youtube_transcript(video_id)
    except VideoUnavailable:
        print(f"  [error] Video unavailable: {video_url}")
        return None
    except (TranscriptsDisabled, NoTranscriptFound):
        print(f"  [error] No transcript available for: {video_url}")
        return None
    except requests.RequestException as exc:
        print(f"  [error] Failed to fetch title for {video_url}: {exc}")
        return None

    collected = date.today().isoformat()
    filename = f"{slugify(title)}.md"
    filepath = YOUTUBE_DIR / filename

    content = f"""# {title}

- **URL:** {video_url}
- **Expert:** {expert_name}
- **Date Collected:** {collected}
- **Annotation:** <!-- Add your notes here -->

---

## Transcript

{transcript}
"""
    filepath.write_text(content, encoding="utf-8")
    print(f"  [saved] {filepath.relative_to(SCRIPT_DIR)}")
    return filepath


def fetch_page_title(soup: BeautifulSoup, fallback: str) -> str:
    """Extract page title from meta tags or heading elements."""
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        return og_title["content"].strip()

    twitter_title = soup.find("meta", attrs={"name": "twitter:title"})
    if twitter_title and twitter_title.get("content"):
        return twitter_title["content"].strip()

    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    return fallback


def extract_article_text(soup: BeautifulSoup) -> str:
    """Extract main article body text from a newsletter/article page."""
    selectors = [
        ".post-content",
        ".body.markup",
        "article",
        "[class*='post-body']",
        "main",
    ]
    for selector in selectors:
        element = soup.select_one(selector)
        if element:
            paragraphs = [
                p.get_text(" ", strip=True)
                for p in element.find_all(["p", "h2", "h3", "li", "blockquote"])
                if p.get_text(strip=True)
            ]
            if paragraphs:
                return "\n\n".join(paragraphs)

    body = soup.find("body")
    if body:
        return body.get_text("\n\n", strip=True)

    return soup.get_text("\n\n", strip=True)


def save_article(url: str, expert_name: str, source_type: str = "Newsletter") -> Path | None:
    """Fetch and save text content from a public newsletter or article URL."""
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=30)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"  [error] Failed to fetch {url}: {exc}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    title = fetch_page_title(soup, fallback=urlparse(url).path.rstrip("/").split("/")[-1])
    body = extract_article_text(soup)

    collected = date.today().isoformat()
    filename = f"{slugify(title)}.md"
    filepath = OTHER_DIR / filename

    # Avoid overwriting unrelated articles that share a title slug
    counter = 1
    while filepath.exists():
        filepath = OTHER_DIR / f"{slugify(title)}-{counter}.md"
        counter += 1

    content = f"""# {title}

- **URL:** {url}
- **Expert:** {expert_name}
- **Source Type:** {source_type}
- **Date Collected:** {collected}
- **Annotation:** <!-- Add your notes here -->

---

## Content

{body}
"""
    filepath.write_text(content, encoding="utf-8")
    print(f"  [saved] {filepath.relative_to(SCRIPT_DIR)}")
    return filepath


def generate_sources_md() -> None:
    """Create research/sources.md listing all experts and their platforms."""
    lines = [
        "# Research Sources",
        "",
        "B2B SaaS newsletter and email marketing experts tracked in this repository.",
        "",
        f"_Last updated: {date.today().isoformat()}_",
        "",
        "---",
        "",
    ]

    for index, expert in enumerate(EXPERTS, start=1):
        lines.append(f"## {index}. {expert['name']}")
        lines.append("")
        lines.append(f"- **Platforms:** {', '.join(expert['platforms'])}")
        lines.append(f"- **LinkedIn:** {expert['linkedin']}")

        youtube = expert.get("youtube")
        lines.append(f"- **YouTube:** {youtube if youtube else '—'}")

        newsletter = expert.get("newsletter")
        lines.append(f"- **Newsletter:** {newsletter if newsletter else '—'}")

        website = expert.get("website")
        lines.append(f"- **Website:** {website if website else '—'}")

        podcast = expert.get("podcast")
        lines.append(f"- **Podcast:** {podcast if podcast else '—'}")

        tools = expert.get("tools")
        if tools:
            lines.append(f"- **Tools:** {tools}")

        notes = expert.get("notes")
        if notes:
            lines.append(f"- **Notes:** {notes}")

        lines.append("- **Annotation:** <!-- Add your notes here -->")
        lines.append("")
        lines.append("---")
        lines.append("")

    SOURCES_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"[saved] {SOURCES_FILE.relative_to(SCRIPT_DIR)}")


def generate_linkedin_templates() -> None:
    """Create empty LinkedIn post template files for each expert."""
    for expert in EXPERTS:
        filename = f"{slugify(expert['name'])}.md"
        filepath = LINKEDIN_DIR / filename

        post_sections = []
        for post_num in range(1, 6):
            post_sections.append(
                f"""## Post {post_num}

- **Date:**
- **Engagement:**
- **Post Content:**

<!-- Paste post content here -->

- **Annotation:** <!-- Add your notes here -->
"""
            )

        content = f"""# {expert['name']} — LinkedIn Posts

- **LinkedIn Profile:** {expert['linkedin']}
- **Annotation:** <!-- Add overall notes about this expert's LinkedIn content -->

---

{chr(10).join(post_sections)}"""
        filepath.write_text(content, encoding="utf-8")
        print(f"[saved] {filepath.relative_to(SCRIPT_DIR)}")


def validate_expert_name(name: str) -> bool:
    """Return True if the expert name exists in EXPERTS."""
    known = {expert["name"] for expert in EXPERTS}
    if name not in known:
        print(f"  [warn] Unknown expert '{name}'. Known experts: {', '.join(sorted(known))}")
        return False
    return True


def collect_youtube_content() -> None:
    if not YOUTUBE_URLS:
        print("\n[info] No YouTube URLs configured — skipping transcript collection.")
        print("       Add entries to YOUTUBE_URLS in collect_content.py.")
        return

    print(f"\nCollecting {len(YOUTUBE_URLS)} YouTube transcript(s)...")
    for entry in YOUTUBE_URLS:
        expert = entry["expert"]
        url = entry["url"]
        if validate_expert_name(expert):
            print(f"  Fetching: {url} ({expert})")
            save_youtube_transcript(url, expert)


def collect_newsletter_content() -> None:
    all_urls = [(entry, "Substack") for entry in SUBSTACK_URLS] + [
        (entry, "Article") for entry in OTHER_URLS
    ]

    if not all_urls:
        print("\n[info] No newsletter/article URLs configured — skipping web content collection.")
        print("       Add entries to SUBSTACK_URLS or OTHER_URLS in collect_content.py.")
        return

    print(f"\nCollecting {len(all_urls)} newsletter/article page(s)...")
    for entry, source_type in all_urls:
        expert = entry["expert"]
        url = entry["url"]
        if validate_expert_name(expert):
            print(f"  Fetching: {url} ({expert})")
            save_article(url, expert, source_type=source_type)


def main() -> int:
    print("B2B SaaS Email Marketing — Content Collector")
    print("=" * 50)

    ensure_directories()

    print("\nGenerating sources.md...")
    generate_sources_md()

    print("\nGenerating LinkedIn post templates...")
    generate_linkedin_templates()

    collect_youtube_content()
    collect_newsletter_content()

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
