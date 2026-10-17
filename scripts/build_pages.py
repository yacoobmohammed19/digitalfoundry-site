"""Generates the DigitalFoundry static pages. Run: python scripts/build_pages.py"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
BASE = 'https://yacoobmohammed19.github.io/digitalfoundry-site/'
TAG = 'We forge the systems your business runs on.'
LD = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"DigitalFoundry",'
      '"url":"%s","logo":"%sassets/logo-light.svg","description":"DigitalFoundry is a software engineering firm and business partner for growing and mid-market companies.",'
      '"areaServed":["South Africa","Worldwide"],"slogan":"%s"}</script>') % (BASE, BASE, TAG)


def page(fname, title, desc, body, ld=False):
    url = BASE + ('' if fname == 'index.html' else fname)
    return f'''<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="DigitalFoundry">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:type" content="website">
<meta property="og:image" content="{BASE}og.png"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1A1F">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/df.css">
{LD if ld else ''}
</head>
<body>
<nav id="nav" class="nav"></nav>
<main>
{body}
</main>
<footer id="foot" class="foot"></footer>
<script src="js/df.js"></script>
</body></html>
'''


def mini(eyebrow, h1, sub):
    return f'<section class="hero mini"><div class="wrap"><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p class="sub">{sub}</p></div></section>'


def cta(h='Let us talk about your next step.', p='Tell us the outcome you are after. We will give you a candid view of how we would approach it.', b='Talk to us'):
    return f'<section class="cta"><div class="wrap"><h2>{h}</h2><p>{p}</p><a class="btn" href="contact.html">{b}</a></div></section>'


def sec(inner, cls=''):
    return f'<section class="sec {cls}"><div class="wrap">{inner}</div></section>'


def head(eyebrow, h, lead='', center=False):
    c = ' center' if center else ''
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<div class="{c.strip()}"><div class="eyebrow">{eyebrow}</div><h2 class="h">{h}</h2>{l}</div>'


def card(ic, h, p, href=None, items=None, more='Learn more →'):
    li = '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>' if items else ''
    icon = f'<div class="ic">{ic}</div>' if ic else ''
    if href:
        return f'<a class="card rv" href="{href}">{icon}<h3>{h}</h3><p>{p}</p>{li}<span class="more">{more}</span></a>'
    return f'<div class="card rv">{icon}<h3>{h}</h3><p>{p}</p>{li}</div>'


STEPS = [
    ('Discover', 'We study how your business actually runs, where time and money are lost, and what success looks like in your numbers.', 'Outcome: a clear business case'),
    ('Prioritise', 'We rank the opportunities by return and risk, and agree a fixed scope, milestones and price in writing.', 'Outcome: signed-off scope and price'),
    ('Deliver', 'Our engineers build and test with your team involved, with a working demonstration every two weeks.', 'Outcome: a tested, documented solution'),
    ('Support', 'We launch in stages, train your people, monitor performance and report against the targets we set together.', 'Outcome: measurable results'),
]


def steps(dark=False):
    return '<div class="steps rv">' + ''.join(f'<div class="step"><h4>{a}</h4><p>{b}</p><small>{c}</small></div>' for a, b, c in STEPS) + '</div>'


pages = {}

# ---------------- HOME ----------------
home = f'''<section class="hero"><div class="wrap">
<div class="eyebrow">Software engineering and business partnership</div>
<h1>The technology partner for companies built to last.</h1>
<p class="sub">DigitalFoundry designs, builds and supports the systems that help growing businesses serve customers better, run leaner and make decisions with confidence.</p>
<div class="btns"><a class="btn pri" href="contact.html">Talk to us</a><a class="btn out" href="capabilities.html">Our services</a></div>
</div></section>
<div class="strip"><div class="wrap">
<div><b>Fixed scope, fixed price</b><span>Agreed in writing before any build begins.</span></div>
<div><b>You own everything</b><span>Code, data and documentation are handed over to you.</span></div>
<div><b>Senior-led delivery</b><span>Accountable engineers, regular demonstrations, no surprises.</span></div>
<div><b>Secure and compliant</b><span>Built with POPIA and enterprise security practice in mind.</span></div>
</div></div>
''' + sec(f'''<div class="g2"><div>{head('Who we are', 'A partner invested in your results, not just your project.')}
<a class="btn dk" href="about.html">About DigitalFoundry</a></div>
<div class="rv"><p>DigitalFoundry is a South African software engineering firm. We work alongside owner-led and mid-market companies that have outgrown manual processes and disconnected tools, and need dependable technology to support their next stage of growth.</p><br>
<p>We combine strategic advice with disciplined engineering. Every engagement starts with your business objective, is governed by a clear scope and is measured against outcomes you can verify.</p></div></div>''') + sec(
    head('What we deliver', 'Three services. One objective: a business that runs better.', 'Each service stands alone and is most powerful in combination, designed around your commercial priorities.', True) +
    '<div class="g3 mt">' +
    card('01', 'Customer experience', 'Intelligent assistants that respond to customers instantly, around the clock, and pass the right conversations to your people.', 'ai-agents.html', ['Faster response, higher conversion', 'Consistent service on every channel', 'Your team freed for high-value work']) +
    card('02', 'Operational efficiency', 'Automation that connects your existing systems, removes duplicated effort and gives management full visibility of every process.', 'workflow-automation.html', ['Lower cost to serve', 'Fewer errors and delays', 'A complete audit trail']) +
    card('03', 'Business insight', 'One trusted set of numbers across sales, operations and finance, so leadership decisions rest on facts rather than spreadsheets.', 'data-infrastructure.html', ['Reporting you can rely on', 'Earlier warning of risks', 'A foundation for growth']) +
    '</div>', 'mist') + sec(
    head('Why DigitalFoundry', 'What you can expect from a long-term partner.') +
    '<div class="mt">' +
    '<div class="rule rv"><h4>Commercial clarity</h4><p>Scope, milestones and price are agreed in writing before work starts. You always know what you are getting, when and at what cost.</p></div>'
    '<div class="rule rv"><h4>Ownership and independence</h4><p>The systems we build belong to you, with full documentation. We earn continued work by being useful, not by being indispensable.</p></div>'
    '<div class="rule rv"><h4>Governance and control</h4><p>Automated decisions operate inside limits you set, with clear escalation to your people and a complete record of what happened and why.</p></div>'
    '<div class="rule rv"><h4>Security and compliance</h4><p>Least-privilege access, encrypted credentials and careful handling of personal information, with POPIA in mind from day one.</p></div>'
    '<div class="rule rv"><h4>Accountability</h4><p>We baseline performance before we build and report against the same measures afterwards. We do not claim results we cannot evidence.</p></div></div>', 'dark') + sec(
    head('Our approach', 'A disciplined path from objective to outcome.', 'Four stages, each with a defined deliverable and a decision point for you.') +
    '<div class="mt">' + steps() + '</div><div class="mt"><a class="btn ol" href="process.html">See how we work</a></div>') + sec(
    head('Who we serve', 'Built for ambitious companies and the firms that advise them.', '', True) +
    '<div class="g2 mt">' +
    card('A', 'Growing and mid-market companies', 'Organisations with real volume and real operational complexity, without a large in-house engineering team. We become that team for the duration of the engagement, and beyond if you wish.') +
    card('B', 'Agencies and consultancies', 'Advisory and service firms that want a dependable delivery partner behind their own client work. White-label partnership arrangements are in development.') +
    '</div>', 'mist') + cta('Ready to build with a partner you can rely on?')
pages['index.html'] = page('index.html', 'DigitalFoundry — Software engineering and business partnership',
    'DigitalFoundry is a software engineering firm and business partner for growing and mid-market companies. Customer experience, operational efficiency and business insight, delivered at fixed scope. Based in South Africa.', home, True)

# ---------------- SERVICES ----------------
cap = mini('Services', 'Technology that moves the numbers that matter.', 'Three services, each tied to a commercial outcome: better customer experience, lower operating cost and sharper decisions.') + sec(
    '<div class="g3">' +
    card('01', 'Customer experience', 'Intelligent assistants that answer enquiries, qualify opportunities and book next steps on WhatsApp, web, email and voice, within rules you control.', 'ai-agents.html', more='Explore this service →') +
    card('02', 'Operational efficiency', 'Automation that connects quoting, approvals, invoicing and reporting, so work moves through the business without manual re-keying.', 'workflow-automation.html', more='Explore this service →') +
    card('03', 'Business insight', 'A governed data foundation that gives sales, operations and finance a single version of the truth.', 'data-infrastructure.html', more='Explore this service →') +
    '</div>') + sec(
    head('Better together', 'Designed as one system, delivered in phases.', 'Most clients start with the area of greatest commercial pressure and extend from there. Because the services share the same foundations, each phase makes the next faster and cheaper to deliver.') +
    '<div class="g3 mt">' + card('', 'Start where it counts', 'We begin with the single opportunity that offers the strongest return, so value is visible early.') + card('', 'Build on what exists', 'We integrate with the accounting, CRM, ERP and messaging tools you already pay for.') + card('', 'Scale with confidence', 'Each phase is scoped and priced separately, so you stay in control of investment.') + '</div>', 'mist') + cta()
pages['capabilities.html'] = page('capabilities.html', 'Services — DigitalFoundry', 'Customer experience, operational efficiency and business insight: three services from DigitalFoundry, delivered at fixed scope.', cap)


def service(fname, title, eyebrow, h1, sub, intro, outcomes, covers, fit, cta_h):
    body = mini(eyebrow, h1, sub) + sec(
        f'<div class="g2"><div>{head("The business case", intro[0])}</div><div class="rv"><p>{intro[1]}</p></div></div>') + sec(
        head('Outcomes', 'What this means for your business.', '', True) + '<div class="g3 mt">' + ''.join(card('', a, b) for a, b in outcomes) + '</div>', 'mist') + sec(
        head('Scope', 'What an engagement typically covers.') + '<div class="mt">' + ''.join(f'<div class="rule rv"><h4>{a}</h4><p>{b}</p></div>' for a, b in covers) + '</div>') + sec(
        head('Is this right for you?', fit[0], fit[1]) + '<div class="mt"><a class="btn pri" href="contact.html">Talk to us</a> &nbsp; <a class="btn ol" href="process.html">How we work</a></div>', 'mist') + cta(cta_h)
    return page(fname, f'{title} — DigitalFoundry', sub, body)


pages['ai-agents.html'] = service('ai-agents.html', 'Customer experience', 'Service 01 · Customer experience',
    'Respond to every customer, every time.',
    'Intelligent assistants that serve your customers instantly and consistently, and hand over to your people when it matters.',
    ('Every missed enquiry is revenue you did not earn.', 'Customers expect an answer in minutes, on the channel they prefer. Intelligent assistants give every enquiry an immediate, accurate response, capture the details your team needs and book the next step, while your people focus on the conversations that need a human.'),
    [('Faster response', 'Enquiries are acknowledged immediately, including after hours and at peak times.'), ('Higher conversion', 'Qualified leads reach your team with context, ready for a decision.'), ('Lower cost to serve', 'Routine questions are resolved without staff time.')],
    [('Customer-facing assistants', 'Answer questions, qualify enquiries and arrange appointments or quotes across WhatsApp, web, email and voice.'), ('Internal assistants', 'Help staff find policies, procedures and answers quickly, and triage documents and email.'), ('Controls and governance', 'Answers come only from content you approve. Defined limits and escalation to a named person keep you in control.'), ('Quality assurance', 'Performance is tested against real conversations before launch and reviewed regularly afterwards.')],
    ('Suited to companies with steady customer demand.', 'If your team spends its day answering the same questions, or enquiries are lost outside office hours, this is likely the fastest route to a visible return.'),
    'Ready to improve every customer interaction?')

pages['workflow-automation.html'] = service('workflow-automation.html', 'Operational efficiency', 'Service 02 · Operational efficiency',
    'Run the business without the busywork.',
    'Automation that joins your existing systems together, removes duplicated effort and gives management full visibility.',
    ('Manual hand-offs quietly drain margin.', 'When quotes, approvals, invoices and reports depend on people re-typing information between systems, errors and delays are inevitable. We connect the tools you already own into a single, governed flow with the right approvals at the right points.'),
    [('Lower operating cost', 'Repetitive administration is removed from the day-to-day workload.'), ('Fewer errors', 'Information is captured once and flows to every system that needs it.'), ('Management visibility', 'A complete audit trail shows what happened, when and who approved it.')],
    [('Process redesign', 'We map the current process, agree the target process and remove steps that add no value.'), ('System integration', 'Connection of accounting, CRM, ERP, e-commerce, email and messaging platforms.'), ('Approvals and controls', 'Defined approval stages, thresholds and exception handling that match your policies.'), ('Monitoring', 'Alerts when something fails, and clear reporting on volume, speed and exceptions.')],
    ('Suited to teams under administrative strain.', 'If growth is adding headcount in back-office roles faster than it adds revenue, automation is usually the right place to start.'),
    'Ready to take the busywork out of your business?')

pages['data-infrastructure.html'] = service('data-infrastructure.html', 'Business insight', 'Service 03 · Business insight',
    'One version of the truth for every decision.',
    'A governed data foundation that gives leadership reliable numbers across sales, operations and finance.',
    ('Decisions are only as good as the numbers behind them.', 'When each department reports from its own spreadsheet, leadership spends meetings debating whose figures are right. We bring your data together under agreed definitions, so reporting is consistent, timely and trusted.'),
    [('Confident decisions', 'Everyone works from the same, agreed definition of each key measure.'), ('Earlier warning', 'Trends and exceptions surface while there is still time to act.'), ('A base for growth', 'Clean, governed data underpins reporting, forecasting and any future automation.')],
    [('Data consolidation', 'Bringing data from your operating systems into one secure, well-organised store.'), ('Metric definitions', 'Business-agreed definitions for revenue, margin, stock, pipeline and other key measures.'), ('Management reporting', 'Dashboards and scheduled reports tailored to each leadership role.'), ('Data governance', 'Access controls, quality checks and documentation that stand up to scrutiny.')],
    ('Suited to leadership teams that need clarity.', 'If preparing a monthly report takes days, or the same question gets different answers depending on who you ask, this is the right starting point.'),
    'Ready for numbers you can trust?')

# ---------------- APPROACH ----------------
proc = mini('Our approach', 'A disciplined path from objective to outcome.', 'Fixed stages, defined deliverables and a decision point for you at every step. No surprises on scope, price or timeline.') + sec(
    head('Four stages', 'Discover. Prioritise. Deliver. Support.', 'Indicative timing for a typical single-system engagement is five to ten weeks from first conversation to go-live.') + '<div class="mt">' + steps() + '</div>') + sec(
    head('What you can expect', 'Delivery you can plan around.', '', True) + '<div class="g3 mt">' +
    card('1', 'Agreed before it is built', 'Scope, milestones, success measures and price are documented and signed off before any build begins.') +
    card('2', 'Visible progress', 'You see working software every two weeks, and your feedback shapes the next iteration.') +
    card('3', 'A controlled launch', 'Go-live is staged with a rollback plan, monitoring from day one and training for your team.') + '</div>', 'mist') + sec(
    head('Engagement models', 'Choose how we work with you.', 'Three structures, one standard of delivery. Scope and pricing are always agreed in writing first.') + '<div class="g3 mt">' +
    card('', 'Project delivery', 'A defined solution delivered at a fixed scope, timeline and price. Best for a clear objective.') +
    card('', 'Ongoing partnership', 'A retained team that monitors, improves and extends your systems each month, with regular performance reporting.') +
    card('', 'Delivery partner', 'White-label engineering capacity for agencies and consultancies delivering to their own clients. In development.') + '</div>') + cta('Want to begin with a discovery conversation?', 'Discovery is the lowest-risk way to find out what is worth building and what it would return.')
pages['process.html'] = page('process.html', 'Our approach — DigitalFoundry', 'DigitalFoundry delivers in four stages with fixed scope, regular demonstrations and a controlled launch.', proc)

# ---------------- ENGAGEMENTS ----------------
work = mini('Engagements', 'The kinds of problem we solve.', 'Representative scenarios, with the measures we design against.') + sec(
    '<div class="g3">' +
    card('', 'After-hours enquiry handling', 'Leads that arrive outside office hours receive an immediate, accurate answer and a booked next step.', items=['Target: first response in under a minute, at any hour', 'One inbox for hand-offs to your team']) .replace('<div class="card rv">', '<div class="card rv"><span class="tag">Customer experience</span>') +
    card('', 'Quote-to-invoice pipeline', 'Quotes, approvals, invoices and follow-ups flow through one path with a full audit trail.', items=['Target: five manual touchpoints reduced to one', 'Every step logged and traceable']).replace('<div class="card rv">', '<div class="card rv"><span class="tag">Operational efficiency</span>') +
    card('', 'Single source of truth', 'Sales, stock and finance report from one governed set of definitions instead of competing spreadsheets.', items=['One agreed definition per business measure', 'Daily refresh with monitoring']).replace('<div class="card rv">', '<div class="card rv"><span class="tag">Business insight</span>') +
    '</div><p class="note">These scenarios are illustrative of typical engagements. Figures are design targets we scope against, not published client results.</p>') + cta('Have a similar challenge?')
pages['work.html'] = page('work.html', 'Engagements — DigitalFoundry', 'Representative DigitalFoundry engagements in customer experience, operational efficiency and business insight.', work)

# ---------------- ABOUT ----------------
about = mini('About us', 'Engineering partners for ambitious companies.', 'We are a South African software engineering firm. We build the dependable systems that let a growing business operate without heroics.') + sec(
    f'<div class="g2"><div>{head("Our story", "Good businesses are held back by systems that were never designed.")}</div><div class="rv"><p>Most owner-led businesses grow by adding tools and people. Eventually the work is held together by inboxes, spreadsheets and the one person who knows how it all connects.</p><br><p>DigitalFoundry exists to replace that with engineered systems that support customers, streamline operations and give leadership clear information.</p><br><p>The name is the idea. A foundry takes raw material and, under controlled conditions, forges something strong and reliable. That is how we treat your business processes.</p></div></div>') + sec(
    head('Our principles', 'How we do business.') + '<div class="mt">' +
    '<div class="rule rv"><h4>Plain over clever</h4><p>We choose the simplest solution that does the job and explain it in plain language. If a spreadsheet is enough, we will say so.</p></div>'
    '<div class="rule rv"><h4>You own it</h4><p>Code, data, configuration and documentation are handed to you. We earn the next engagement by being useful.</p></div>'
    '<div class="rule rv"><h4>People stay in charge</h4><p>Automation handles the routine. Your people handle judgement, exceptions and relationships.</p></div>'
    '<div class="rule rv"><h4>Measured, not claimed</h4><p>We baseline before we build and report against the same measures afterwards.</p></div>'
    '<div class="rule rv"><h4>Careful with data</h4><p>Least-privilege access, encrypted credentials and POPIA-aware handling are standard, not extras.</p></div></div>', 'dark') + sec(
    head('Who we work with', 'Two kinds of client.', '', True) + '<div class="g2 mt">' +
    card('A', 'Growing and mid-market companies', 'Businesses with real volume and operational complexity, but without an in-house engineering team.') +
    card('B', 'Agencies and consultancies', 'Firms that want a dependable delivery partner behind their own client work. Partner programmes are in development.') + '</div>', 'mist') + cta('Let us look at your business.')
pages['about.html'] = page('about.html', 'About — DigitalFoundry', 'DigitalFoundry is a South African software engineering firm and business partner for growing companies.', about)

# ---------------- FAQ ----------------
QA = [
    ('What does DigitalFoundry do?', 'We design, build and support business technology in three areas: customer experience, operational efficiency and business insight. Each stands alone and is stronger together.'),
    ('Who do you work with?', 'Owner-led and mid-market companies that have outgrown manual processes, and agencies and consultancies that want a delivery partner behind their own client work.'),
    ('How much does an engagement cost?', 'It depends on scope, so we do not publish a price list. After discovery and prioritisation you receive a written fixed scope, milestones and price. Nothing is built until you have agreed it in writing.'),
    ('How long does it take?', 'A typical single-system engagement runs about five to ten weeks from first conversation to go-live. Larger programmes are planned in phases.'),
    ('Will an automated assistant say something wrong to my customers?', 'Assistants answer only from content you approve, work within limits you set and hand over to a named person with the full conversation when a request is out of scope. Every conversation is logged and quality is reviewed.'),
    ('Who owns the code, data and documentation?', 'You do. Everything is handed over to you, with no lock-in.'),
    ('How do you protect personal information?', 'We apply least-privilege access, encrypted credentials and sensible retention, with POPIA in mind. We tell you what data a system touches and where it is stored before it goes live.'),
    ('Can you work with our existing systems?', 'Usually, yes. We integrate with common accounting, CRM, ERP, e-commerce, email and messaging tools. If a tool cannot be integrated we say so early and propose an alternative.'),
    ('What happens after launch?', 'You can run the solution yourselves using the documentation we hand over, or retain us to monitor, improve and report each month.'),
    ('Where are you based?', 'We are based in South Africa and serve clients locally and internationally.'),
]
faq = mini('FAQ', 'Straight answers to common questions.', 'If yours is not here, ask us directly.') + sec(
    '<div class="faq">' + ''.join(f'<div class="fi"><button class="fq" aria-expanded="false">{q}</button><div class="fa"><p>{a}</p></div></div>' for q, a in QA) + '</div>') + cta('Still have a question?', 'Describe what you are trying to achieve and we will respond candidly.')
pages['faq.html'] = page('faq.html', 'FAQ — DigitalFoundry', 'Answers to common questions about working with DigitalFoundry: cost, timing, ownership, security and support.', faq)

# ---------------- CONTACT ----------------
contact = mini('Talk to us', 'Tell us what you want to achieve.', 'We reply with a candid view of whether we can help and what the first step would be.') + sec(
    '<div class="g2"><div>' + head('Enquiry', 'Start with a short brief.') +
    '<p>Complete the short form and we will assemble it into a clean summary you can copy and send as soon as our contact details are live.</p><br>'
    '<p>Direct contact details are being set up and will appear on this page. Until then nothing you type here is sent anywhere: the summary is built in your browser only.</p>'
    '<div class="mt"><span class="soon">CONTACT DETAILS COMING SOON</span></div>'
    '<ul class="card" style="margin-top:32px;border:0;padding:0"><li>A plain answer on fit</li><li>A scoped discovery conversation as the first step</li><li>Written scope and price before any build</li></ul></div>'
    '<div class="card"><form class="form" id="brief">'
    '<div><label for="n">Your name</label><input id="n" name="name" required autocomplete="name"></div>'
    '<div><label for="b">Company</label><input id="b" name="biz" required autocomplete="organization"></div>'
    '<div><label for="a">Area of interest</label><select id="a" name="area"><option>Customer experience</option><option>Operational efficiency</option><option>Business insight</option><option>Delivery partnership</option><option>Not sure yet</option></select></div>'
    '<div><label for="s">Company size</label><select id="s" name="size"><option>1-10</option><option>11-50</option><option>51-200</option><option>200+</option></select></div>'
    '<div><label for="m">What would you like to achieve?</label><textarea id="m" name="msg" required></textarea></div>'
    '<button class="btn pri" type="submit">Prepare my enquiry</button>'
    '<div class="brief-out" id="briefOut"></div><p id="briefNote" style="display:none;font-size:14px;color:var(--ft)">Summary prepared and copied to your clipboard. Our contact details will be published here shortly.</p>'
    '</form></div></div>')
pages['contact.html'] = page('contact.html', 'Talk to us — DigitalFoundry', 'Start a conversation with DigitalFoundry about your next technology engagement.', contact)

# ---------------- PRIVACY ----------------
priv = mini('Legal', 'Privacy policy', 'Short and plain. Last updated 17 October 2026.') + sec(
    '<div class="prose"><h2>What this website collects</h2><p>This website does not use accounts, tracking cookies or advertising pixels. The enquiry form on the contact page runs entirely in your browser: what you type is not transmitted to us or to any third party.</p>'
    '<h2>Third-party services</h2><p>Fonts are loaded from Google Fonts, which may receive your IP address and browser details when serving the font files. The site is hosted on GitHub Pages, which keeps standard server logs.</p>'
    '<h2>If you contact us</h2><p>When you contact us by any channel, we use what you share only to respond to you and to scope work you ask about. We do not sell personal information, and we keep it only as long as needed for that purpose.</p>'
    '<h2>Your rights</h2><p>Under the Protection of Personal Information Act (POPIA) you may ask what information we hold about you, and ask us to correct or delete it. Contact details for these requests will be published on this site.</p>'
    '<h2>Changes</h2><p>If this policy changes, the date above will change with it.</p></div>')
pages['privacy.html'] = page('privacy.html', 'Privacy policy — DigitalFoundry', 'How DigitalFoundry handles personal information on this website.', priv)

# ---------------- 404 ----------------
nf = '<section class="hero mini" style="min-height:70vh"><div class="wrap"><div class="eyebrow">404</div><h1>This page could not be found.</h1><p class="sub">The page you asked for does not exist or has moved.</p><div class="btns" style="margin-top:30px"><a class="btn pri" href="index.html">Back to home</a><a class="btn out" href="contact.html">Talk to us</a></div></div></section>'
pages['404.html'] = page('404.html', 'Page not found — DigitalFoundry', 'Page not found.', nf)

for f, h in pages.items():
    (root / f).write_text(h, encoding='utf-8')
print('built', len(pages), 'pages')
