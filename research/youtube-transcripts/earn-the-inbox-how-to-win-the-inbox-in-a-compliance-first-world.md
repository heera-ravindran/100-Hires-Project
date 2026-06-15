# Earn the Inbox: How to Win the Inbox in a Compliance-First World

- **URL:** https://www.youtube.com/watch?v=LGwYC-xCnpk
- **Expert:** Dave Gerhardt
- **Date Collected:** 2026-06-15
- **Annotation:** <!-- Add your notes here -->

---

## Transcript

[applause]

>> Hello everyone. I'm excited to be here.

Thank you for

being here and I'm going to be talking

about a very severed topic called

deliverability.

Most marketers are terrified of the word

deliverability.

We've seen people shut down, cry,

turn off their programs

because they say you have a

deliverability issue. And I'm here kind

of to

ease you into the deliverability world

and how it impacts your email program

from traffic source to after you

actually hit the send button.

So my topic is earn the inbox. How to

stay

relevant and use your email marketing to

drive revenue and to drive growth

while staying compliant with all the new

requirements that we have now with our

mailbox providers Gmail and Yahoo and

Outlook

are setting a standard as well as we are

living in a world where your subscribers

control your

your email programs.

But before we get started, I'll

introduce myself. My name is Isra. I'm

an email deliverability and strategy

specialist. I don't like to go by an

expert because I'm always learning as

well. A little fun fact about how I got

into this field cuz you don't really

choose email, it kind of chooses you.

Back in 2016, I was I used to work for

the federal government. I stopped cuz

too much travel, had kids. And I wanted

to get into the online world. And I

tried to apply for email

marketing jobs in general. Thanks Zapier

for rejecting me 100 times.

So I said screw it. I'm just going to

learn it myself. I founded my own

e-commerce store.

And I kind of learned everything about

marketing through there from paid media

to social media. And then we landed on

email marketing when Facebook was kind

of like breaking in 2018 with all the

breach data stuff. So

I took a store. I used to sell cat

accessory products to cat ladies.

They loved it. We had the wonderful meow

cores that, you know, sold

hundreds of thousands of dollars.

And we kind of created a cult following

through that within 18 months. Through

our retention strategy.

That's kind of where I kind of found my

love for email where it was more, you

know, you can use it as a personal way

to connect with your customers, with

your subscribers. And we kind of coined

the classy cat lady instead of the crazy

cat lady

because everybody wants to be seen and

heard. So that was how I got into

retention strategy.

But I knew that if I'm going to use it

long-term,

there has to be a technical aspect that

needs to be taken care of as well.

At the time,

DTC did not have any deliverability

spaces or mentors. So I actually found a

mentor in the affiliate marketing space.

Which if you know anything about

affiliate marketing,

it's pretty shady.

>> [laughter]

>> So they send a lot of emails a day, but

I kind of just learned I took my mentor

kind of handed me a couple of clients in

the biz of. And it was just like

fascinating to me. I'm like, why is

nobody talking about this? And I was

like, you know what?

I'm going to become the professional

email deliverability apper. So

I founded the Winbox. I merged my store

with another store and moved on from

e-commerce. And now I service DTC and um

nonprofit with lifecycle and retention

strategies through our boutique agency.

And yeah, so that's what I've been doing

for the past 7 years. I am safe from

being kidnapped because

I'm telling you I'll talk all day about

email deliverability. [clears throat]

Um

So let's just get into it.

Email deliverability has always been

there. It's always been there. It's

always been more of a nuance to people.

So in the past,

you probably have always heard like when

you set up your marketing programs,

you need records. You need a little bit

of technical. Maybe your technical team

handles it and you're good to go. And

then you just don't think about it. You

just go into your email um

platforms and, you know, create

beautiful emails and you send them out

and money, you know, appears in your

accounts.

Um

but

the best practices have turned into

requirements. You are no longer living

in a best practice world where it's nice

to have, it's more of a must-have now.

That little diagram just shows you like

when you hit send,

that's what your email's going through

before it even reaches the inbox.

There's a lot of filters. There's a lot

of um parsing of information. And you

need to create a program where you can

get through this little diagram as fast

as possible.

So we'll talk we're going to talk a

little bit more about that. The first

one is going to be the price of entry is

your authentication, which is your

digital identity. Who you are. You need

to be identified. So this first part

we're going to talk about how the

mailbox providers look at you and allow

you to actually enter their inbox.

Authentication

is a must, but that doesn't mean you're

going to land in the inbox, which we'll

talk about in the second part. So the

first one is your digital identity. You

need your DNS records set in place.

There are three DNS records

that every, you know, domain has to have

to allow marketing emails, transactional

emails, customer service emails to go

through. They're listed up there. I'm

not going to read them for you. You guys

can read it, but I'll tell you the

acronym. So SPF is um

it is an SPF record is the record that

gives servers permission to send on your

behalf.

You should have one record per domain.

If you have more than that, you got a

problem. You can have it on a subdomain,

but in the recent in recent testing,

we've noticed that it's better to have

like if you were to say like you're

sending a marketing email through

Mailchimp and you have it on a subdomain

SPF, we prefer on your main because your

return path

goes back to your main domain. So

SPF record should have every server that

you're sending from because you're

giving it permission. We don't like to

see more than 10. Most times, people add

servers and never take them off.

They just keep adding.

Which is why I say there's a max of 10

because after

the 10, it gets truncated, it slows it

down, it can cause a fail on the SPF

part and your email lands in

spam folder or gets blocked.

So just make sure that you are giving

permission to the platforms by adding

your entries into the SPF. And then DKIM

is like a sealed

envelope when you send your email with

your signature and it matches to the DNS

record that you have the DKIM record,

which is in your DNS hosting site.

It matches it basically to say, okay,

this is this email was sent untampered.

We're going to let it and it matches our

record. We're going to allow it into the

inbox.

DKIM,

you need a record for every platform you

send from. So if you have like Google

Workspace, you know, your internal that

has a DKIM. Your Klaviyo has a different

DKIM. So make sure that every platform

you have has a specific domain key that

is visible. And then you have DMARC, the

lovely DMARC. So DMARC used to be

a non-thing. Like nobody cared about it.

In 2014, Gmail came in and said, you

need at least a policy none.

We need to monitor your traffic. So

everybody went in and said cool, policy

none.

And they left it at that. However, in

the last couple of years, we are seeing

even if you have a policy none DMARC,

you can land in spam. And the reason is

is it is a monitoring

policy. It is not an enforcement policy.

We like to see we like to move you and

see you on like a quarantine or a reject

policy quarantine.

It doesn't it allows it in the inbox,

but it, you know, quarantines it to

spam. And then reject totally blocks

emails that are you're not giving

permission to. And it's the highest

protection basically. It's if you have

big infrastructure, you should be on a

DMARC policy of reject at some point in

the process.

One thing one more thing about DMARC,

you can block your own emails if you're

doing it wrong. So

DMARC is a monitoring process and most

people will set it and forget it. You're

supposed to be reading those reports

they're sending you. If you're not

getting reports, you should. You should

add an email into your DNS record that

gets it.

So you're supposed to monitor that and

know what is happening because that that

report tells you what is aligning with

your SPF and DKIM and who is actually

maybe spamming or spoofing on your

behalf. We actually had a client who

did not have a good DMARC policy. They

had a bot attack and their whole

Cloudflare system went down. So um

it's hard. And if you are a marketer and

it's it's a technical aspect and you

have a hard time doing it, maybe reach

out to the technical department and work

with them. Make sure these records are

always clean, always monitored. It is

your entry into the inbox.

This is who you say you are. Let's talk

about email headers. This is the second

part of identifying

who you are in the inbox. It's what your

user sees right when they open their

inbox. There are four components. Your

domain your from name has to be clear

and identified. Gmail came out a couple

months ago and said,

these are the rules. Which is kind of

nice cuz then I'm not gaslit into

telling you "These are the rules." So,

the from domain I'm sorry, the from name

has to be clear.

Either like name from business or the

business name itself. You cannot use an

email address. You cannot use emojis.

Uh, you can't use anything crazy like

Black Friday promotion exclusive like

instead of your name. You have to

identify how your subscriber

knows you. So, for example,

you have people coming from your opt-ins

and the first email they get is from

business name, but then you start

sending campaigns from Daniel. Like who

the hell's Daniel? Um,

so you got to make sure it matches.

Um, how your subscriber sees it cuz it's

two parts.

Mailbox providers are watching you and

then your subscribers are also watching

and being annoyed by you for tricking

them to open this email.

Um, the second one is your from domain.

It has to be uh,

from email email domain based um,

header. So, your from email has to be a

domain based. Now, even I believe for

um, non-bulk senders Gmail is cracking

down on this. You have to have a if you

have a business, it should be like

support or care at business name.com.

You can't use a private like Gmail at

Gmail or Yahoo.

So, those two

Um, that one actually will get you in

spam real quick and it helps fix things

real quick too once you switch it out.

That one is a big one. That one's like

the biggest identifier of um,

uh, you know, your digital identity.

And then

don't use deceptive headlines. I thought

I've seen it all.

I apparently haven't.

As you can see, um,

April 2nd I get this lovely email.

Uh, we're using every single deception

possible on Earth.

Uh, it was basically

I I reached out to this person cuz I

know them and I said, "What are you

doing?" And they were like, "Oh man, it

was our highest revenue." And I was

like, "Yeah, what is it what about your

spam complaints?" It was like 8%. Um, so

don't use it. Not fun. In the long term,

you're really damaging your reputation

with mailbox providers.

And then emojis

in [snorts] subject lines.

This is not a written rule anywhere, but

I've had conversations. Let me just tell

you. So,

I know things that, you know, have

happened in closed rooms where we're not

supposed to say

the information

out loud, but we've, you know,

we like to give you a little hint,

right? So, um,

emojis in subject lines are not a no

rule.

It is

limited. It limit your emoji usage. So,

Wayfair is I don't know if anybody else

receives Wayfair emails. They've kind of

calmed down in the last couple years,

but

it's been crazy. Um,

they want you to use

emojis limiting it to two and they

prefer you to use it after your life

text. Um, just the way that I guess the

algorithm reads it. They prefer emojis

going to the end.

Don't use it for every subject line.

Gets a lot of spam you there.

And then you have this little added

layer of

recognition trust. This is not an

enforcement policy yet. Um, but it's

nice to have. It is an added protection

to your reputation.

Um, if you are going to add so Apple

branded email

and BIMI, which is the uh,

the that little icon identify like brand

ID in the mailbox providers for Gmail

and Apple. So,

um, it is just it it's nice to have

because it's

builds trust with your subscribers

and it does boost engagement. However,

when you um, Apple branded is free and

you can do it through your there's a

Google document that you can just

follow. It does it quickly. So, like

when your subscribers if they use Apple

Mail, they will see your icon there.

Um, but BIMI is a paid certification um,

and it does require a DMARC of uh,

reject or quarantine. So, that's the

nice thing about BIMI is that you have

added security plus the trust and

engagement.

Uh, and it shows up in your like Gmail

uh, what do you call it? Gmail inbox as

well.

Um, I believe also I don't know if Yahoo

already has it, but

it shows up more than just Apple. So,

Apple is just for Apple and then BIMI's

for the other mailbox providers.

Um, Validity Mail actually just did a

just released a case study, which was

nice to see

um, BIMI in action cuz everybody was

talking about BIMI, but nobody knows how

to implement it and then they realized

there's a price tag.

So, um, they just did a uh, case study

with a global food brand

and they saw an 18% increase in

um, engagement lift there, which is kind

of nice just to have and understand. Uh,

the case study is on validitymail.com's

website if you guys want to

look at that. All right. So,

we've talked about

how you are

viewed by mailbox providers. That's the

first part of your email program. These

things are technical and they're easy to

follow rules. So, that's that's the easy

part. Just follow the rules, set them,

monitor them, make sure everything is

clean. The second part is you, the

sender, and your behavior.

We've seen wild things.

So, the first part I'm going to talk

about this in

every aspect of the email program

because I feel like you want to see

where does deliver how does

deliverability kind of view every little

component of your email program as you

are doing the work. So, a lot of time

marketers just come in and like, "Hey,

yeah, we use the segment. We send these

emails."

Cool. Like that's it. But there's a lot

more to your program that impacts

deliverability before you even get to

the campaign level. And the first one is

traffic.

Quantity over quality.

I don't have to really, you know,

explain that. Uh, um,

we want people that want our emails. So,

there are three

recommendations for you. Don't buy

lists.

Don't scrape lists and don't use warming

tools that use bots.

Um, this is a big deliverability risk.

Mailbox providers are very smart. They

know you cannot grow you grow your brand

or grow your business or like hack it

with this

with these type of lists. You are going

to get flagged and it's actually going

to do more damage for you in the long

term and more costly. So, anybody who

comes to me and says, "Hey, I bought a

list."

I don't even speak to them. I just turn

around and go.

Uh, good luck. Uh, the second part is

the lower quality traffic that comes

into your um, into your email programs

and these are the tricky ones because

it's not necessarily a subscriber that

a subscriber that doesn't want your

email, but you have to qualify and make

sure that you get the real segment out

of that subscriber. So, these kind of

lists um,

come through like opt-ins through like

cross promotions or some type of

promotion a collaboration or a giveaway.

And the reason I say you need to qualify

and segment out of that is because

somebody can come in from that traffic

source

and maybe they want your collaborators

in data or like product or information

and you just happen to be there. So,

like they're not really interested in

your business, but they're interested in

other businesses that you're

collaborating with.

So, it's really important to take that

segment and nurture it through a flow.

We'll talk about flow automations.

Um, and then pull out the people that

really do engage and purchase from you

and then the rest, you know,

either, you know, wave them goodbye,

suppress them, you know, try to

re-engage them in another way, but

typically we just want we want the

segment that cares about our business.

And then the ideal traffic is

customers who actually opted in and

said, "Hey, I also want your marketing

email." You know, that little checkbox.

Um, double opt-ins, consent forms,

anybody basically who really loves your

brand or your product or business that

comes in. That's who you really should

be focused on.

Automations.

The bane of my existence. Um,

automations shape your

>> [laughter]

>> Sorry, this is this is literally like my

life right now. Um,

automations shape the quality of your

incoming traffic.

Automations are really important. I've

struggled with this with a lot of

clients because I know it's technical. I

know it's hard to keep up and manage,

but they are necessary. Um,

and they need to be monitored as well.

So, every time a traffic source comes

in, you should be sending

um, an email out. At least one email.

Um, and the reason is it does guard your

deliverability and I'll talk about that

a little bit. But before I go in there,

um,

please do automations responsibly so you

don't get this.

Um, we see it all the time. Clients

will, you know, a subscriber comes in

and they get 15 emails in like 24 hours.

And the reason is that you have every

automation turned on with no filtering,

no understanding of the journey for that

subscriber. So, we do want to make sure

we're not building a bush, but more of

like a beautiful little tree that's

branching out. Um,

so that's the part, you know, just keep

that in mind as you build automations.

And the reason automations are good for

you, um,

they do guard your deliverability. They

actually give you the highest boost into

your email program. So, when we set up

email programs for our clients,

we actually start if they're brand new,

we start with a drip of automations

before we even send out a campaign like

maybe two to three weeks because we want

to build that reputation with the

mailbox providers.

Um the first email will have the highest

opens and clicks.

This kind of ties into um Fernando's uh

earlier about uh preference center. I

want to talk about that a little bit,

too. But it it has a high click and

engagement rate because it's the first

email that person is getting from you

and they recognize you. So instead of

even if you're doing a welcome or some

type of like exchange a product for the

email

that email is like sacred to you. You

can provide information that that

subscriber may only see then and never

see again cuz they might not open

another email. And this is where, you

know, where um Fernando was talking

about preference centers and how they're

ineffective they are ineffective in a

campaigns. I'll tell you that. Nobody

cares about that down there.

What they what they care about is that

first email they get. Because you give

power back to the subscriber. You tell

them

>> [snorts]

>> "Hey, you know, we are happier here. We

don't want to bombard you. Please update

your preference now." And that shows

that you care right from the beginning

and set the tone.

And the the subscriber will trust you

more. They're less likely to unsubscribe

to because you become they attach that

memory with your, you know,

um with the act the the actual action

that you give them. So use those first

emails and automations responsibly.

Build trust. Um and the

it also filters on interest buyers. So

like if they have not opened their last

five emails

you can take that out and not put it in

your like master list. I call it master

list for your campaign. So the master

list is the who you send to on a daily

weekly basis.

Um so it also helps with that. It

filters

the unengaged right away so that you're

not, you know, uh sitting there trying

to figure out

you know, six months later who should be

getting emails and who hates us. Uh

so [laughter]

Not everyone belongs on the floor.

We're talking about list segmentations

now. So this is the this is the third

part of your program where we are

looking at lists. And I have seen two

extremes with every program. The over

segmenters

and the under segmenters. The over

segmenters are just freaked out by

hearing deliverability. So they'll just

like

delete people within 30 days. You

You know, you haven't opened, we don't

want you on there. Um

that's that's a very extreme uh

extreme like approach, especially if you

are in a

business of using email marketing for

revenue, uh which is which is what we

are in DTC, right? So that's a big one

for us. The under segmentation are the

people who

just want to prove that they can grow a

list. Um you know, the KPIs is that we

went from

5,000 to 100,000 and only like 2,000 are

actually opening.

Um

So it's it's it's two extremes and there

is a happy medium for that and there are

rules that you should follow.

Segmentation is really hard for people

to understand and I don't blame you

because there is so much information

online that's just total Um

you know, Chad will get on X and tell

you segment 30 60 90. Everybody else is

trash. And then, you know, you have like

your develop deliverability Dan over

here telling you, you know,

>> [laughter]

>> you shouldn't even be sending to this

segment ever again. So it's it's

confusing and most people

take the online advice lightly, but look

into your program. So my advice is

always

what is your subscriber to product life

cycle look like? Um you know, some

people

sell products that are within 30 days,

you know, a

a replenishment. Some sell within like

two years. Like how many couches can you

buy, you know, in two in 30 days.

Nobody's going to buy another couch,

right? So like you have to understand

how your subscribers move and you have

two different types of

um lists inside your segments. You have

your customers and you have your

email engaged subscribers. They can be

customers, but not necessarily. And your

customer

can be a avid buyer from you and they

could be a dead email

um engager.

So I need you to think like separate the

two because everybody thinks a customer

is always opening emails. They're not.

Um I have I have a client that has a

customer who spent $70,000

to this day

and they just they don't need open

emails. They're just a loyal customer

who goes to the store and buys, but we

do have their email. However,

when we segment to send out emails, we

want the actual people who are opening

and um clicking our emails and engaging

with them because those are the signals

mailbox providers are looking for.

They're not They're not opening They're

not looking at the guy who bought

$70,000 from you and say, "Oh, he's a

loyal customer. We'll just keep him

anyway. We'll keep you in the inbox."

Even though he's not hasn't opened in

like the past two years. Like it doesn't

work like that. They are looking at

signals on how your subscribers engage

with the inbox and your emails in the

inbox.

So

just make sure

you are looking at your data and not

everyone else's data, not your

competitors' data um when you do your

our segmentations.

Uh we do a lot of apply uh brand uh

sorry, inclusions and exclusions. So

I'll explain a little bit why we do

this.

I like to push So I'm in I'm in the

intersection of deliverability and

marketing. So my clients want the most

revenue without going to spam. So I live

at like that little tiny intersection of

pushing the boundaries, but staying

compliant. Um so our lists are big. We

have very big um inclusion lists. So we

go broad with inclusion and then we

apply exclusions where needed. So let me

give you an example of how we do this

for So like say like we have a 180-day

engagers. Like that's the size

of our engagers in our pool, right?

Um [snorts] we have great open rates, 60

plus for Gmail, Yahoo, Outlook

um for them. But then AOL is like 10%.

So most people will just go in and start

slashing everybody. Everyone from Gmail,

Yahoo, Outlook. Now everybody only who's

engaged in the last 30 days are getting

emails.

That's really not the right approach.

Um and this is something that you need

to be very careful with with your open

rates. Uh do not read the total open

rates. Go and break down by mailbox

providers because that tells you a

different story.

So what we would do, we would actually

take the AOL users and shrink that

segment to a smaller one. So like say

we're only sending to AOL's 30-day

engagers as we remedy that reputation

for them the the reputation with the

mailbox provider that's AOL

while allowing everybody else at the

180-day in Gmail, Yahoo, and Outlook to

continue to receive our emails. That way

you're not just like shutting down a big

chunk of your

um you know, readers, engagers, buyers

just because one mailbox provider is

having an issue.

Uh and then please sunset actively.

Make this part of your program. It

should be automated. Uh define it again

based on your life cycle. Gmail right

now, anything past two years they if

it's an inactive email, it actually

either gets shut down or turns into a

spam trap. So really use that kind of

like your especially if you have a high

Gmail

makeup list makeup, use that as like

your benchmark.

All right.

We live in an AI summarization landscape

now.

Let's go into content. So now you are

designing your campaigns.

This is all recent. So just take it all

in. Uh

design and content copy has become very

um AI basically first.

And so now when you are writing and

designing for your emails, you are

actually writing for AI first. Your

first reader is AI. And he kind of just

tells everybody else what you're saying.

So

make sure it's

you know, you it's readable, it's

digestible, it's clear. We don't want

clever here. Um just stick to being

clear, letting peo letting AI understand

what you are trying to say to the

customer cuz this actually shows up in

the inbox before they even open the

email.

Um if we are going to add design

and images, I am a pro live text, but I

know a lot of brands are very adamant

about their Figma designs. Um so we are

heavy on alt text, very descriptive.

Make sure you you are writing

exactly what that image is. Um the way I

lead my team with design is

images should add to the email. It

should not If it If it disappears

it should not

collapse the email. So the email should

live without the images

um on its own. So

Yeah.

Yeah.

Live text, baby. Um

So that's that's the whole point is that

imagery should evoke emotion, bring in

more to the context, but it if it's not

there, it it does not take away from the

email's message. Um and also

accessibility. Everybody, please, you

know, accessibility is important.

Uh that's what live text is for. And you

know, a lot of people do have images

turned off. So like turn off your images

and just look at your email once in a

while just to see like how does this

render for accessibility because we want

to be inclusive in all aspects of our

programs.

Okay, so additional protocols. This is

kind of like the extras that go into

your email and how you are viewed by

mailbox providers and how your

subscribers kind of react to you. So,

optimize for clear and clean URL links.

We typically recommend between three to

five, maximum five, um but I know that a

lot of people kind of design their

emails to look like landing pages. You

got a header with a million links, a

footer telling your whole story. Um

we Email is a So, let me just retract a

little bit. Email is a medium and the

whole point is you are trying to connect

with your reader inside that email. It

is more important for you to carry the

message outside the email. So, like if

you have a blog, instead of putting the

whole blog in your email, you know, just

summarize it and then send them to the

link. That also helps with your um

engagement with the the signal

engagement for mailbox providers to

realize, "Okay, so they are in more

interested to read more from this um

from this sender." So, clean and clear

URLs. Uh we don't rec- We recommend that

you stick to your domain-based URLs more

than out external ones. The ones I've

seen that break the most are social

links, so check those often if you use

them. Uh usually somebody saves a block

and then they just keep reusing it

forever. Um with our Inbox Monster

testing, we have caught lots of broken

links, social media.

So, just check your links, make sure

they work. Um it's also a signal from

for the mailbox providers if you are

sending to a broken link. Um you know,

if it's a 404 or it breaks somewhere or

there's a like a hot like a high bounce

rate on the link clicks. That's all

being read by the mailbox providers.

They they know what's going on um and

they are checking all these links when

you go through that filtering process.

So, just make sure your links are clear

and clean and minimal.

Words. We used to have lovely people

online exchanging their asking for your

email to give you a list of free spam

words that you should shouldn't use,

especially free.

Uh that's not true at all anymore.

Please don't buy or give anybody your

email for a free spam list. Um

Mailbox providers now look at the tone

and intent overall. So, language is

still important. Uh the way the mailbox

provider like you can't use like really

scammy like they'll look at the whole

email and be like, "Okay, this is a

scammy-looking email or this is a very

gory email. Like we don't allow this in

our

the language we don't allow into our

inbox." So, like it's still important,

but it's it's viewed as a whole versus

per word.

Right. So, that's something to keep in

mind when you are doing it. And also,

the language that you use

keeps you relevant. So, let me explain

how this one works.

Whatever traffic source that comes in,

so the subscriber that comes in, the

tone you are using and the language you

are using there should always carry into

the campaigns you are sending them. So,

I have seen

brands that talk about community and

love and, you know, being together and

then they get to the campaign level and

they're selling them everything under

the sun. Buy my So, it's like,

"Whoa, I thought I was coming in for

community. I'm just being sold." So,

that language is important because it

builds on that relevance and right now

inbox provide Gmail is built on

relevance. So, even if you are inboxing,

if your user hates your emails or just

is not interested as the emails come in,

you are being pushed down in relevance

and ultimately you'll be in spam. So,

relevance is important, language, tone.

Um and then your vitals of your program.

So, I kind of split this into three

uh things that you should check always.

Uh your positive signals are your opens

and clicks. We do not look at opens and

clicks as like, you know, "Awesome, I

have 60%." We look at it as a trend. So,

are we always in that like ballpark of

open rates consistently? So, like if we

are getting like a 65% open rate and

throughout the months I'm seeing that

slip into like 50, 55, 40, something is

eroding in your program and you need to

check on it. Um and then that's where

you kind of have to look at your mailbox

providers. Oh my, did one of them, you

know,

you know, the the subscribers from one

mailbox provider, like say AOL,

doesn't want to, you know, they're

they're not engaging as often. Is that

where we're seeing like the trend in

open rates down? Are we hitting spam

there or is it like a total Is Is all

them Are all the mailbox providers

trending down because our content is not

becoming relevant to the user? So, um

open rates trends into deliverability

the program if it if it erodes slowly.

You'll also see

if you see like a 60% open rate and then

next send you get 10% open rate, that's

a deliverability problem and it's

usually has something to do with your

authentication. So, go back to your

authentication, make sure everything is

clean because

that's the only way you can land in spam

hard um if you don't have your digital

identity aligned.

And then we have um clicks. Clicks are

indicators of your engagement with your

subscribers.

So, you know, is your content relevant?

Do they care about it? Where can we like

improve our click rates there?

Then you have your negative signals.

They're not They're not bad. Don't freak

out about them, but they are They are

your strongest signals into your

deliverability health and reputation.

Bounces.

Um please, if you are excluding soft

bounces, don't do that.

>> [snorts]

>> That's my rule I had.

Um check with your ESPs and CRMs because

they have a very Most of them have a

good program with the bounces. So, like

if they're hard bounce, they suppress

them. If they're soft bounce, they will

retry several times before suppression

or allowing. But please do not suppress

soft bounces because they bounced, you

know, one or two times. It's usually

because there's some issue with like

getting into the inbox at that time. So,

we saw that with Yahoo earlier this year

when they shrunk their size of their

Yahoo inboxes for people. We had the

high bounces there. Um

Once people start cleaning those out,

those emails went back into the inbox.

So, bounces,

do not, you know, exclude soft bounces

unless, you know,

your ESP and CRM will take care of that

for you. However,

for your automations, that first email

should be You should be checking your

bounce rates on those first emails. And

the reason I say that is because your

traffic coming in

indicates if you have bot activity, spam

traps, um low leads, all of that. Um

you'll see the hard bounces at the

traffic source and you can take uh

action to mitigate that before even hits

your um other email

categories and segmentations. So,

use bounces at the automation level and

also don't worry about them when it

comes to the soft bounce. Just keep a

monitor. You you want it uh

less than a 2% bounce rate

at all times for every send, I guess. Um

And then you have spam complaints.

How many of you use Google Postmaster?

Does anybody use SNDS? Microsoft? Okay.

All right, so please use your Google

Postmaster.

Um Google does not have a feedback loop

to your ESPs or CRMs. You do not see

spam complaints because they don't go

back to your CRM. So, it's not that you

have zero spam complaints in Gmail, it's

just not visible to you.

Um please sign up for a Google

Postmaster account, set up your domain,

and that data will show up and it will

surprise you. Um

there's a new version of the Google

Postmaster. We We monitor now error

delivery as well. Uh Google Postmaster

will tell you when like your content is

spammy or there's like a rate limiting

um you're exceeding that by sending

Basically it throttles your emails. So,

um

it just tells you more data. That's

where you get your Gmail data on like

spam complaints and um the the bounce

rates and all the area the area user

stuff. It's not in your CRM or ESP. The

other mailbox providers do have them in

there. They do come back to your ESP.

So, you'll have that there.

And then we have unsubscribes. So,

unsubscribes do not impact

deliverability directly, but as as

Fernando was saying, unsubscribes tell

you how relevant you are to your user.

If they hate you, they're unsubscribing.

Um

so, just make sure that you stay

relevant to whatever they signed up for

when it comes to your content. And then

finally, you have subscribers' feedback

and, you know, beyond email touchpoints.

Like I said, email is a medium. You

should use it as a passing through

instead of a hard stop because when you

stop at email, you really don't have the

enough data to know what your

subscribers really want beyond that

email. Does that mean you have to,

you know, sell a click every email? No,

but you should have a comprehensive

program where you understand when to

drive that action.

>> [sighs]

>> And finally, the effort you put in is

the inbox you get out. Um it is an

ongoing monitoring system.

The hardest part Like the only thing I

want to you take away is it's not a set

in stone thing. Email deliverability is

always ongoing. It's in every aspect of

your program, in every category, and

needs to be taken care of. The mailbox

providers are watching you, the senders

are watching the subscribers are

watching you, and you're like in the

middle trying to like balance all that.

And so the key takeaway here is

authenticate, [snorts]

clean up, and make sure that you are

constantly monitoring your DNS records,

earn permission, nothing crazy spammy,

get the right and then qualify that

traffic as well. So, make sure that you

are actually getting the right users on

your segments, and stay relevant. Send

good emails, really good emails.

Send them.

>> [applause]

>> Thank you.

>> [applause]

>> And I know this was like a lot, so I

just want to like shock you a little

bit.

The mailbox providers are always

watching, just like that.

Thank you.

>> [applause]
