"""Generates the static DigitalFoundry pages. Run: python scripts/build_pages.py"""
import pathlib, json
root = pathlib.Path(__file__).resolve().parent.parent
BASE = 'https://yacoobmohammed19.github.io/digitalfoundry-site/'

def head(title, desc, fname, extra=''):
    return f'''<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="DigitalFoundry">
<link rel="canonical" href="{BASE}{'' if fname == 'index.html' else fname}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{'' if fname == 'index.html' else fname}"><meta property="og:type" content="website">
<meta property="og:image" content="{BASE}og.png"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1A1F">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/df.css">
{extra}</head>
<body>
<nav id="site-nav" class="site-nav"></nav>
<main>
'''

TAIL = '''</main>
<footer id="site-footer" class="site-footer"></footer>
<script src="js/df.js"></script>
</body></html>
'''

def mini_hero(eyebrow, title, sub):
    return f'''<section class="hero hero-mini"><canvas class="hero-canvas" id="heroCanvas"></canvas><div class="hero-gradient"></div>
<div class="hero-content"><div class="hero-eyebrow">{eyebrow}</div><h1 class="hero-title">{title}</h1><p class="hero-sub">{sub}</p></div></section>
'''

def cta(title='Got a process that should run itself?', sub='Tell us what is slowing the business down. We will tell you plainly whether we can fix it, and what it would take.'):
    return f'''<section class="cta"><div class="section-inner"><div class="eyebrow reveal" style="justify-content:center">Start a project</div>
<h2 class="heading-lg reveal">{title}</h2><p class="reveal">{sub}</p>
<a href="contact.html" class="btn-primary reveal">Start a project <span>→</span></a></div></section>
'''

def sec(kind, inner, id=''):
    i = f' id="{id}"' if id else ''
    return f'<section class="section section-{kind}"{i}><div class="section-inner">\n{inner}\n</div></section>\n'

def faq_items(items):
    return '<div class="max-narrow">' + ''.join(
        f'<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button><div class="faq-a"><p>{a}</p></div></div>' for q, a in items) + '</div>'

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj) + '</script>\n'

ORG = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "DigitalFoundry",
       "url": BASE, "logo": BASE + "assets/logo-light.svg",
       "description": "DigitalFoundry designs and builds custom AI agents, workflow automation and data infrastructure for owner-led SMEs and mid-market teams.",
       "areaServed": [{"@type": "Country", "name": "South Africa"}, {"@type": "AdministrativeArea", "name": "Worldwide"}],
       "slogan": "We forge the systems your business runs on."}

FAQS = [
 ('What does DigitalFoundry actually build?', 'Three things: custom AI agents that handle customer and internal conversations, workflow automation that connects the systems you already pay for, and data infrastructure that gives your business one trusted set of numbers. Each stands alone and is stronger together.'),
 ('Who do you work with?', 'Owner-led SMEs and mid-market teams that have outgrown spreadsheets and manual hand-offs. We also partner with agencies and consultancies that want a build partner behind their own client work.'),
 ('How much does a project cost?', 'It depends on scope, so we do not publish a price list. After the first two stages, Unpack and Prioritise, you receive a written fixed scope, milestones and price. Nothing is built until you have agreed it in writing.'),
 ('How long does a build take?', 'A typical single-system build runs about five to ten weeks from first conversation to go-live: roughly one week to Unpack, one to Prioritise, then three to eight weeks to Forge. Larger programmes are planned in phases.'),
 ('Will an AI agent say something wrong to my customers?', 'Agents answer only from content you approve, work inside limits you set, and hand over to a named person with the full thread when confidence is low or a request is out of scope. Every conversation is logged, and quality is measured against test sets built from your real conversations.'),
 ('Who owns the code, the data and the documentation?', 'You do. Code, configuration, data and documentation are handed over to you. There is no lock-in and no black box.'),
 ('How do you handle personal information?', 'We apply least-privilege access, encrypted secrets and sensible retention, with POPIA in mind. We will tell you what data a system touches and where it is stored before it goes live.'),
 ('Can you work with the tools we already use?', 'Usually, yes. We integrate through APIs and webhooks with common accounting, CRM, ERP, e-commerce, email and messaging tools. If a tool has no usable interface we will say so early and propose an alternative.'),
 ('What happens after launch?', 'You can run it yourselves using the runbooks we hand over, or move to a Run & improve plan where we monitor, tune and enhance the system each month and report on performance.'),
 ('Where are you based?', 'We are built in South Africa and deliver to clients locally and internationally.'),
]

pages = {}

# ───────────── HOME ─────────────
h = head('DigitalFoundry — We forge the systems your business runs on', 'DigitalFoundry designs and builds custom AI agents, enterprise workflow automation and data infrastructure for owner-led SMEs and mid-market teams. Built in South Africa.', 'index.html', jsonld(ORG))
h += '''<section class="hero"><canvas class="hero-canvas" id="heroCanvas"></canvas><div class="hero-gradient"></div>
<div class="hero-content"><div>
<div class="hero-eyebrow">AI agents · Automation · Data infrastructure</div>
<h1 class="hero-title"><span class="word">We</span><span class="word">forge</span><span class="word">the</span><span class="word highlight">systems</span><span class="word">your</span><span class="word">business</span><span class="word">runs</span><span class="word">on.</span></h1>
<p class="hero-sub">DigitalFoundry designs, builds and runs production-grade AI agents, workflow automation and data infrastructure for owner-led SMEs and mid-market teams.</p>
<div class="hero-buttons"><a class="btn-primary" href="contact.html">Start a project <span>→</span></a><a class="btn-outline" href="capabilities.html">Explore capabilities</a></div>
<div class="pills"><span class="pill"><i></i>Human-in-the-loop by design</span><span class="pill"><i></i>Fixed-scope delivery</span><span class="pill"><i></i>Built in South Africa</span></div>
</div>
<div class="console" aria-hidden="true"><div class="bar"><b></b><b></b><b></b><span>foundry / run-log</span></div><pre id="term"></pre></div>
</div><div class="hero-scroll"><span></span></div></section>

<div class="strip" id="strip"><div class="section-inner">
<div class="m"><div class="v"><span data-n="4">0</span></div><div class="l">Stage method: Unpack, Prioritise, Forge, Run</div></div>
<div class="m"><div class="v"><span data-n="3">0</span></div><div class="l">Core disciplines under one roof</div></div>
<div class="m"><div class="v"><span data-n="24">0</span><span>/7</span></div><div class="l">Always-on agents with monitored hand-off</div></div>
<div class="m"><div class="v"><span data-n="100">0</span><span>%</span></div><div class="l">Of your data and code stays yours</div></div>
</div></div>
'''
h += sec('light', '''<div class="grid-2"><div>
<div class="eyebrow reveal">Who we are</div>
<h2 class="heading-xl scroll-words">Engineering partners for businesses that have outgrown manual work.</h2>
<div class="divider-gradient reveal"></div>
<a href="about.html" class="btn-dark reveal">About DigitalFoundry →</a></div>
<div class="scroll-stagger">
<p class="text-body scroll-para">DigitalFoundry is a South African engineering studio. We take the processes your team keeps patching with spreadsheets, inboxes and copy-paste, and turn them into systems that run on their own.</p>
<p class="text-body scroll-para">We work in a fixed four-stage method, <strong>Unpack, Prioritise, Forge, Run</strong>, with a defined output at the end of every stage. You know what you are getting, what it costs and when it lands before a line of code is written.</p>
<p class="text-body scroll-para">Agents act inside limits you set and escalate to a person when it matters. Everything we build is logged, documented and handed over. The code, the data and the documentation are yours.</p>
</div></div>''')
h += sec('dark', '''<div class="text-center"><div class="eyebrow reveal">Capabilities</div>
<h2 class="heading-lg reveal">Three disciplines. One engineered system.</h2>
<p class="lead mx reveal">Each capability stands alone and is stronger together. Open a discipline for the full architecture, components and standards.</p></div>
<div class="grid-3 reveal">
<a class="card" href="ai-agents.html"><div class="card-icon">01</div><h3>Custom AI agents</h3><p>Purpose-built agents that handle customer conversations and internal work across WhatsApp, web, email and voice, grounded in your own knowledge and bounded by rules you set.</p><span class="card-link">See the architecture →</span></a>
<a class="card" href="workflow-automation.html"><div class="card-icon">02</div><h3>Enterprise workflow automation</h3><p>Event-driven automation that connects the systems you already use, removes re-keying and adds approval gates and a full audit trail to critical processes.</p><span class="card-link">See the architecture →</span></a>
<a class="card" href="data-infrastructure.html"><div class="card-icon">03</div><h3>Data infrastructure</h3><p>Governed pipelines, a clean warehouse and a shared metrics layer, so every dashboard and every AI agent answers from the same trusted numbers.</p><span class="card-link">See the architecture →</span></a>
</div>''', 'services')
h += sec('alt', '''<div class="eyebrow reveal">Interactive architecture</div><h2 class="heading-lg reveal">See how a forged system fits together.</h2>
<p class="lead reveal">Select a discipline, then select any component to see how it works and what it connects to.</p>
<div class="tabs reveal" id="tabs" role="tablist"></div>
<div class="svc reveal"><div class="panel" id="spec"></div><div class="panel diagram"><div class="hint">▸ INTERACTIVE ARCHITECTURE — select a node</div><svg id="dg" viewBox="0 0 560 360" role="img" aria-label="Architecture diagram"></svg><div class="detail" id="det"></div></div></div>''')
h += sec('dark', '''<div class="eyebrow reveal">The method</div><h2 class="heading-lg reveal">Unpack. Prioritise. Forge. Run.</h2>
<p class="lead reveal">A fixed four-stage path with a defined output at the end of every stage. Select a stage for detail.</p>
<div class="tl reveal" id="tl"></div>
<div class="mt-lg reveal"><a href="process.html" class="btn-outline">Full delivery process →</a></div>''')
h += sec('light', '''<div class="eyebrow reveal">Engineering principles</div><h2 class="heading-lg reveal">How we build, every time.</h2>
<p class="lead reveal">The standards that separate a system your team trusts from a demo that impresses once.</p>
<div class="pr reveal">
<div><h4>Owned by you</h4><p>Your data, code and documentation are yours. No lock-in, no black boxes.</p></div>
<div><h4>Human in the loop</h4><p>Agents act inside defined limits and escalate with context when confidence is low.</p></div>
<div><h4>Observable</h4><p>Logging, alerts and audit trails on every workflow, so you can see what ran and why.</p></div>
<div><h4>Secure by default</h4><p>Least-privilege access, encrypted secrets, and personal data handled with POPIA in mind.</p></div></div>''')
h += sec('alt', '''<div class="text-center"><div class="eyebrow reveal">Where it applies</div><h2 class="heading-lg reveal">The shape of problem we take on.</h2>
<p class="lead mx reveal">Representative scenarios, with the measures we design against. The full write-ups are on the Work page.</p></div>
<div class="grid-3 reveal">
<div class="card"><span class="tag">AI agents · Services</span><h3>After-hours enquiry agent</h3><p>Leads that arrive outside office hours get an immediate, accurate answer and a booked next step.</p><div class="kp"><div><b><span>&lt;</span>1 min</b><small>Target first response, 24/7</small></div><div><b>1</b><small>Inbox for human hand-offs</small></div></div></div>
<div class="card"><span class="tag">Automation · Operations</span><h3>Quote-to-invoice pipeline</h3><p>Quotes, approvals, invoices and follow-ups flow through one event-driven path with a full audit trail.</p><div class="kp"><div><b>5<span>→</span>1</b><small>Target manual touchpoints per order</small></div><div><b>100<span>%</span></b><small>Steps logged and traceable</small></div></div></div>
<div class="card"><span class="tag">Data · Mid-market</span><h3>Single source of truth</h3><p>Sales, stock and finance report from one governed metrics layer instead of three competing spreadsheets.</p><div class="kp"><div><b>1</b><small>Definition per business metric</small></div><div><b>Daily</b><small>Refresh, monitored with alerts</small></div></div></div>
</div><p class="note">Scenarios are illustrative of typical engagements. Figures are design targets we scope against, not published client results.</p>''')
h += sec('dark', '''<div class="eyebrow reveal">Planning tool</div><h2 class="heading-lg reveal">Estimate the time an automation could return.</h2><p class="lead reveal">A rough, transparent model to frame the conversation. Adjust the sliders to your business.</p>
<div class="calc reveal"><div><h3>Hours back to your team</h3><p class="s">Three inputs, one honest formula.</p>
<div class="sl"><label for="r1">Repetitive tasks per week <b id="v1"></b></label><input type="range" id="r1" min="10" max="500" step="10" value="120"></div>
<div class="sl"><label for="r2">Minutes spent per task <b id="v2"></b></label><input type="range" id="r2" min="2" max="60" step="1" value="12"></div>
<div class="sl"><label for="r3">Share of tasks we can automate <b id="v3"></b></label><input type="range" id="r3" min="20" max="90" step="5" value="60"></div></div>
<div class="res"><div class="big"><span id="o1">0</span> h</div><small>staff hours returned per month</small><div class="big"><span id="o2">0</span> days</div><small>working days per year back in your team's hands</small><div class="fn">Hours = tasks × minutes × automation share × 52 ÷ 12 ÷ 60. A planning estimate, confirmed during Unpack.</div></div></div>''')
h += cta()
pages['index.html'] = h + TAIL

# ───────────── CAPABILITIES ─────────────
h = head('Capabilities — AI agents, workflow automation, data infrastructure | DigitalFoundry', 'Three engineering disciplines under one roof: custom AI agents, enterprise workflow automation and governed data infrastructure.', 'capabilities.html')
h += mini_hero('Capabilities', 'Three disciplines. One engineered system.', 'Pick one capability or combine all three. Each is built to the same standards: owned by you, observable, secure by default.')
h += sec('light', '''<div class="grid-3">
<a class="card reveal" href="ai-agents.html"><div class="card-icon">01</div><h3>Custom AI agents</h3><p>Customer-facing assistants, internal knowledge agents and document or email triage, across WhatsApp, web chat, email and voice.</p><ul class="checks"><li>Grounded in your approved content</li><li>Guardrails and named escalation</li><li>Evaluated on your real conversations</li></ul><span class="card-link">Explore AI agents →</span></a>
<a class="card reveal" href="workflow-automation.html"><div class="card-icon">02</div><h3>Workflow automation</h3><p>Order-to-cash, onboarding, procurement, reporting and document handling, connected through APIs and webhooks.</p><ul class="checks"><li>Approval gates and role-based access</li><li>Retries, failure queue and alerts</li><li>Complete audit log</li></ul><span class="card-link">Explore automation →</span></a>
<a class="card reveal" href="data-infrastructure.html"><div class="card-icon">03</div><h3>Data infrastructure</h3><p>Pipelines, a cloud warehouse and a metrics layer that gives every team the same number for the same question.</p><ul class="checks"><li>Raw, cleaned and business-ready layers</li><li>Automated quality tests</li><li>POPIA-aware access and retention</li></ul><span class="card-link">Explore data →</span></a>
</div>''')
h += sec('dark', '''<div class="eyebrow reveal">Interactive architecture</div><h2 class="heading-lg reveal">Explore the building blocks.</h2>
<p class="lead reveal">Select a discipline, then any component in the diagram.</p>
<div class="tabs reveal" id="tabs" role="tablist"></div>
<div class="svc reveal"><div class="panel" id="spec"></div><div class="panel diagram"><div class="hint">▸ INTERACTIVE ARCHITECTURE — select a node</div><svg id="dg" viewBox="0 0 560 360" role="img" aria-label="Architecture diagram"></svg><div class="detail" id="det"></div></div></div>''')
h += sec('alt', '''<div class="text-center"><div class="eyebrow reveal">Better together</div><h2 class="heading-lg reveal">Why the three compound.</h2></div>
<div class="grid-3 reveal">
<div class="card"><h3>Data feeds the agents</h3><p>An agent is only as good as the facts behind it. A governed warehouse and metrics layer give agents trustworthy, current answers about stock, orders and customers.</p></div>
<div class="card"><h3>Automation gives agents hands</h3><p>An agent that can only talk is a brochure. Connected workflows let it book, quote, update records and trigger approvals, with every action logged.</p></div>
<div class="card"><h3>Agents feed the data</h3><p>Every conversation and decision becomes structured, measurable data, closing the loop so the whole system keeps improving.</p></div></div>''')
h += cta()
pages['capabilities.html'] = h + TAIL

# ───────────── SUB-CAPABILITY PAGES ─────────────
def subpage(fname, idx, title, desc, eyebrow, h1, sub, intro_head, intro_paras, usecases, stds, faqs, extra_service):
    h = head(title, desc, fname, jsonld({"@context": "https://schema.org", "@type": "Service", "name": h1, "provider": {"@type": "ProfessionalService", "name": "DigitalFoundry"}, "areaServed": "ZA", "description": desc}))
    h += mini_hero(eyebrow, h1, sub)
    h += sec('light', f'''<div class="grid-2"><div><div class="eyebrow reveal">Overview</div><h2 class="heading-xl scroll-words">{intro_head}</h2><div class="divider-gradient reveal"></div></div>
<div class="scroll-stagger">{''.join(f'<p class="text-body scroll-para">{p}</p>' for p in intro_paras)}</div></div>''')
    h += sec('dark', f'''<div class="eyebrow reveal">Architecture</div><h2 class="heading-lg reveal">How it fits together.</h2>
<p class="lead reveal">Select any component to see what it does and what it connects to.</p>
<div id="tabs" data-only="{idx}"></div>
<div class="svc reveal"><div class="panel" id="spec"></div><div class="panel diagram"><div class="hint">▸ INTERACTIVE ARCHITECTURE — select a node</div><svg id="dg" viewBox="0 0 560 360" role="img" aria-label="Architecture diagram"></svg><div class="detail" id="det"></div></div></div>''')
    h += sec('alt', '<div class="eyebrow reveal">Where it applies</div><h2 class="heading-lg reveal">Typical use cases.</h2><div class="grid-3 reveal mt-md">' + ''.join(f'<div class="card"><div class="card-icon">{i+1:02d}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(usecases)) + '</div>')
    h += sec('light', '<div class="eyebrow reveal">Standards</div><h2 class="heading-lg reveal">What you can count on.</h2><div class="pr reveal mt-md">' + ''.join(f'<div><h4>{a}</h4><p>{b}</p></div>' for a, b in stds) + '</div>')
    h += sec('dark', '<div class="text-center"><div class="eyebrow reveal">Questions</div><h2 class="heading-lg reveal">Common questions.</h2></div><div class="reveal mt-md">' + faq_items(faqs) + '</div>')
    h += cta(f'Ready to talk {extra_service}?')
    return h + TAIL

pages['ai-agents.html'] = subpage('ai-agents.html', 0,
 'Custom AI Agents for Business | DigitalFoundry', 'Purpose-built AI agents for WhatsApp, web chat, email and voice, grounded in your own knowledge, bounded by rules you set, with monitored hand-off to your team.',
 'AI agents', 'Custom AI agents that work inside your rules.', 'Customer-facing and internal agents grounded in your approved knowledge, with guardrails, escalation to a named person and full logging.',
 'Agents that answer from facts you approve, and stop where you tell them to.',
 ['An AI agent is not a chatbot bolted onto a website. We design it as a small system: channels it listens on, a knowledge layer it retrieves from, tools it can use, limits it must respect and a person it hands over to.',
  'Every agent is built from your own policies, products and records, so answers stay current and can be traced to a source. Out-of-scope or low-confidence cases never reach the customer unreviewed.',
  'Before launch we build a test set from your real conversations and measure the agent against it. After launch we keep measuring, so quality is a number you can see rather than a feeling.'],
 [('After-hours enquiries', 'Answer, qualify and book leads that arrive when the office is closed, then pass anything unusual to a person with the full thread.'),
  ('Internal knowledge assistant', 'Staff ask questions about policies, pricing and procedures and get cited answers instead of interrupting a colleague.'),
  ('Document and email triage', 'Classify incoming mail and attachments, extract key fields and route each item to the right queue.'),
  ('Appointment and order handling', 'Book, move and confirm appointments or orders through your calendar and systems, with confirmation messages.'),
  ('Payment and follow-up nudges', 'Polite, accurate reminders on overdue items, with a person stepping in when a customer disputes something.'),
  ('Multi-channel consistency', 'One agent serving WhatsApp, web chat and email with the same knowledge and the same limits.')],
 [('Approved-answer scope', 'The agent speaks only to topics and facts you have signed off.'), ('Named escalation', 'A real person receives the full conversation when it matters.'), ('Evaluated', 'Test sets from your own conversations, reviewed before and after launch.'), ('Logged', 'Every conversation and tool call is recorded and reviewable.')],
 [('Can the agent work on WhatsApp?', 'Yes. WhatsApp, web chat, email and voice are all supported channels, and one agent can serve several at once with the same behaviour.'),
  ('What happens when the agent does not know?', 'It says so, and hands the conversation to a named person with the full thread so the customer never has to repeat themselves.'),
  ('Which AI model do you use?', 'Model choice is made per task for quality, cost and data sensitivity, and can change over time without rebuilding the system around it.'),
  ('How do we keep answers up to date?', 'The agent retrieves from your approved content at answer time. Update the source and the answers update with it.')],
 'about AI agents')

pages['workflow-automation.html'] = subpage('workflow-automation.html', 1,
 'Enterprise Workflow Automation | DigitalFoundry', 'Event-driven workflow automation that connects your accounting, CRM, ERP and email, with approval gates, retries and a complete audit trail.',
 'Workflow automation', 'Workflow automation your finance team can audit.', 'Event-driven automation that connects the systems you already pay for, removes re-keying and shows exactly what ran, when and why.',
 'Stop re-typing the same data into five different systems.',
 ['Most businesses run on a chain of hand-offs: an email becomes a spreadsheet row, which becomes a quote, which becomes an invoice, with a person copying data at every step. Each copy is a chance for delay and error.',
  'We replace the chain with an event-driven flow. Something happens, such as a form, a payment or a status change. The event is validated, routed by business rules, approved where policy requires and written to the right system.',
  'Nothing fails silently. Failed steps retry with back-off, then land in a queue with an alert. Every step is recorded in an audit log that supports finance, compliance and fast troubleshooting.'],
 [('Quote-to-invoice', 'Approved quotes become invoices automatically, with payment follow-ups and status written back to your books.'),
  ('Customer and staff onboarding', 'Forms, checks, account creation and welcome steps run in a defined order with reminders for anything outstanding.'),
  ('Procurement and approvals', 'Requests route to the right approver by value and category, with escalation when no one responds.'),
  ('Reporting packs', 'Weekly and month-end reports assembled from live data and delivered on schedule.'),
  ('Document handling', 'Invoices and forms are read, validated and filed, with exceptions flagged for review.'),
  ('System synchronisation', 'Keep CRM, accounting, stock and e-commerce in step without anyone re-keying.')],
 [('Approval gates', 'People sign off where policy needs it, with reminders and escalation.'), ('Resilient', 'Retries, idempotency and a failure queue so nothing is lost or duplicated.'), ('Audit trail', 'Who did what, and when, for every step.'), ('Documented', 'Runbooks so your team can operate it.')],
 [('Do we need to replace our current software?', 'No. We connect the tools you already use through their APIs and webhooks, so your team keeps working in familiar systems.'),
  ('What if a connected system goes down?', 'Steps retry automatically with back-off. If they still fail, they wait in a queue and an alert is raised, so work is delayed rather than lost.'),
  ('Can approvals still involve a person?', 'Yes, by design. Automation handles the routine path and routes exceptions and sign-offs to the right person.'),
  ('How do we know it is working?', 'Monitoring, alerts and a step-by-step audit log show what ran. On a Run & improve plan you also get a monthly report.')],
 'about workflow automation')

pages['data-infrastructure.html'] = subpage('data-infrastructure.html', 2,
 'Data Infrastructure & Metrics Layer | DigitalFoundry', 'Governed data pipelines, a cloud warehouse and a shared metrics layer so every dashboard and AI agent answers from the same trusted numbers.',
 'Data infrastructure', 'One set of numbers your whole business trusts.', 'Governed pipelines, a clean warehouse and a shared metrics layer, tested automatically and secured by role.',
 'End the argument about which number is right.',
 ['When sales, stock and finance each report a different figure for the same thing, decisions slow down and trust erodes. The cause is usually not bad people but undefined metrics and untested pipelines.',
  'We bring your sources into a warehouse with three layers: an untouched raw copy, a cleaned and modelled layer, and a business-ready layer. On top sits a metrics layer where revenue, margin and churn are defined once and served to every dashboard.',
  'Automated tests check freshness, completeness and anomalies, and role-based access and retention rules keep the platform secure and POPIA-aware as it grows.'],
 [('Unified reporting', 'One set of definitions across sales, stock and finance, refreshed on a schedule you can rely on.'),
  ('Dashboards for every team', 'Role-appropriate views that all draw from the same governed layer.'),
  ('AI-ready data', 'A trustworthy feed for your agents, so they quote real stock, prices and order status.'),
  ('Data quality monitoring', 'Alerts when a source goes stale, a field goes missing or a number looks wrong.'),
  ('Spreadsheet retirement', 'Move critical month-end spreadsheets onto a governed, auditable pipeline.'),
  ('Compliance-aware retention', 'Access roles and retention rules aligned to how you handle personal information.')],
 [('Lineage', 'Know where every number came from.'), ('Tested', 'Automated checks on freshness and completeness.'), ('Governed', 'One definition per metric, versioned.'), ('Secure', 'Role-based access and encryption.')],
 [('Do we need a data warehouse if we are small?', 'Not always. During Unpack we check whether a lighter approach is enough, and only recommend a warehouse where it pays for itself.'),
  ('Which tools do you connect to?', 'Common accounting, CRM, e-commerce and operational systems, spreadsheets and third-party APIs, each with credentials you control.'),
  ('Can we keep using our existing dashboard tool?', 'Usually, yes. The metrics layer is tool-agnostic and can serve the BI tool you already use.'),
  ('Who has access to the data?', 'Only the roles you define. Access is least-privilege, encrypted and logged.')],
 'about your data')

# ───────────── PROCESS ─────────────
h = head('Delivery Process: Unpack, Prioritise, Forge, Run | DigitalFoundry', 'A fixed four-stage delivery method with a defined output at every stage, fixed scope agreed in writing before build, and three engagement models.', 'process.html')
h += mini_hero('Delivery process', 'From messy process to a system that runs.', 'A fixed four-stage path with a defined output at the end of every stage. No surprises on scope, price or timeline.')
h += sec('dark', '''<div class="eyebrow reveal">Four stages</div><h2 class="heading-lg reveal">Unpack. Prioritise. Forge. Run.</h2>
<p class="lead reveal">Select a stage for detail. Durations are indicative for a typical single-system build.</p><div class="tl reveal" id="tl"></div>''')
h += sec('light', '''<div class="text-center"><div class="eyebrow reveal">What you can expect</div><h2 class="heading-lg reveal">Delivery you can plan around.</h2></div>
<div class="grid-3 reveal mt-md">
<div class="card"><div class="card-icon">1</div><h3>Written before built</h3><p>Scope, milestones, success measures and price are agreed in writing at the end of Prioritise. Nothing is built before you have signed it off.</p></div>
<div class="card"><div class="card-icon">2</div><h3>Working demos, fortnightly</h3><p>During Forge you see a working system every two weeks, not a slide deck. Feedback goes straight into the next iteration.</p></div>
<div class="card"><div class="card-icon">3</div><h3>Staged go-live</h3><p>Launch is staged with a rollback plan, monitoring from day one and training for the people who will use it.</p></div></div>''')
h += sec('alt', '''<div class="eyebrow reveal">Engagement models</div><h2 class="heading-lg reveal">Choose how we work with you.</h2>
<p class="lead reveal">Three structures, one standard of delivery. Select a model to see where it fits. Scope and pricing are agreed in writing before any build starts.</p>
<div class="eng reveal" id="eng"></div><div class="fit reveal" id="fit"></div>''')
h += cta('Want to start with Unpack?', 'The first stage maps how your business really runs and where time and money leak. It is the cheapest way to find out what is worth building.')
pages['process.html'] = h + TAIL

# ───────────── WORK ─────────────
h = head('Work — Representative engagements | DigitalFoundry', 'Representative DigitalFoundry engagement scenarios showing the shape of problem we take on and the measures we hold ourselves to.', 'work.html')
h += mini_hero('Work', 'What a forged system looks like in practice.', 'Representative engagement scenarios: the problem, the system we would build and the measures we design against.')
def case(tag, t, prob, build, results, kp):
    return f'''<div class="card reveal"><span class="tag">{tag}</span><h3>{t}</h3>
<p><strong style="color:#fff">The problem.</strong> {prob}</p><p style="margin-top:12px"><strong style="color:#fff">What we build.</strong> {build}</p>
<ul class="checks">{''.join(f'<li>{r}</li>' for r in results)}</ul>
<div class="kp">{kp}</div></div>'''
h += sec('dark', '<div class="grid-3">' + case('AI agents · Services', 'After-hours enquiry agent',
 'A service business loses leads that arrive outside office hours.', 'An agent answers on WhatsApp and web chat from approved business knowledge, qualifies the enquiry, books it and hands anything unusual to a person with the full thread.',
 ['Instant first response, any hour', 'Calendar booking without staff', 'Escalation with full context'], '<div><b><span>&lt;</span>1 min</b><small>Target first response, 24/7</small></div><div><b>1</b><small>Inbox for human hand-offs</small></div>') +
 case('Workflow automation · Operations', 'Quote-to-invoice pipeline',
 'Quotes, approvals, invoices and payment follow-ups are re-keyed across email, spreadsheets and accounting.', 'One event-driven flow with approval gates, automatic invoice creation, payment reminders and a complete audit trail.',
 ['Approvals routed by value', 'Invoices created from approved quotes', 'Every step logged'], '<div><b>5<span>→</span>1</b><small>Target manual touchpoints per order</small></div><div><b>100<span>%</span></b><small>Steps logged and traceable</small></div>') +
 case('Data infrastructure · Mid-market', 'Single source of truth',
 'Sales, stock and finance each report different numbers for the same question.', 'Sources consolidated into a governed warehouse with a metrics layer, automated quality tests and role-based access.',
 ['One definition per metric', 'Freshness and quality alerts', 'Dashboards and AI draw from one layer'], '<div><b>1</b><small>Definition per business metric</small></div><div><b>Daily</b><small>Refresh, monitored with alerts</small></div>') +
 '</div><p class="note">Scenarios are illustrative of typical engagements. Figures shown are design targets we scope against, not published client results. Named references are shared on request once a client agrees.</p>')
h += sec('light', '''<div class="eyebrow reveal">How we measure</div><h2 class="heading-lg reveal">Every engagement starts with a baseline.</h2>
<ul class="row-list reveal mt-md">
<li><b>Baseline first</b><span>During Unpack we record how the target process performs today: volume, time per task, error rate, response time. Without a baseline, "improvement" is a guess.</span></li>
<li><b>Success measures in the scope</b><span>The signed scope names the measures that define success, so both sides know what "done" means.</span></li>
<li><b>Reported monthly</b><span>On a Run &amp; improve plan you receive a monthly report against the same measures.</span></li>
<li><b>Honest about limits</b><span>If a process is not worth automating, or a tool cannot be integrated, we say so early.</span></li></ul>''')
h += sec('alt', '''<div class="text-center"><div class="eyebrow reveal">Planning tool</div><h2 class="heading-lg reveal">Estimate the time an automation could return.</h2></div>
<div class="calc reveal mt-md"><div><h3>Hours back to your team</h3><p class="s">Three inputs, one honest formula.</p>
<div class="sl"><label for="r1">Repetitive tasks per week <b id="v1"></b></label><input type="range" id="r1" min="10" max="500" step="10" value="120"></div>
<div class="sl"><label for="r2">Minutes spent per task <b id="v2"></b></label><input type="range" id="r2" min="2" max="60" step="1" value="12"></div>
<div class="sl"><label for="r3">Share of tasks we can automate <b id="v3"></b></label><input type="range" id="r3" min="20" max="90" step="5" value="60"></div></div>
<div class="res"><div class="big"><span id="o1">0</span> h</div><small>staff hours returned per month</small><div class="big"><span id="o2">0</span> days</div><small>working days per year back in your team's hands</small><div class="fn">Hours = tasks × minutes × automation share × 52 ÷ 12 ÷ 60. A planning estimate, confirmed during Unpack.</div></div></div>''')
h += cta()
pages['work.html'] = h + TAIL

# ───────────── ABOUT ─────────────
h = head('About DigitalFoundry | Engineering partners, built in South Africa', 'DigitalFoundry is a South African engineering studio building AI agents, workflow automation and data infrastructure for owner-led SMEs and mid-market teams.', 'about.html', jsonld(ORG))
h += mini_hero('About us', 'A foundry for the systems businesses run on.', 'We are a South African engineering studio. We build the unglamorous plumbing that lets a growing business run without heroics.')
h += sec('light', '''<div class="grid-2"><div><div class="eyebrow reveal">Our story</div><h2 class="heading-xl scroll-words">Good businesses are held back by systems that were never designed.</h2><div class="divider-gradient reveal"></div></div>
<div class="scroll-stagger">
<p class="text-body scroll-para">Most owner-led businesses grow by adding tools and people. Eventually the work is held together by inboxes, spreadsheets and one person who knows how it all connects.</p>
<p class="text-body scroll-para">DigitalFoundry exists to replace that with engineered systems: AI agents that handle conversations, workflows that move work between tools, and data foundations that everyone trusts.</p>
<p class="text-body scroll-para">The name is the idea. A foundry takes raw material and, under controlled conditions, forges something strong and reliable. That is how we treat your processes.</p></div></div>''')
h += sec('dark', '''<div class="eyebrow reveal">What we believe</div><h2 class="heading-lg reveal">Principles we do not negotiate.</h2>
<ul class="row-list reveal mt-md">
<li><b>Plain over clever</b><span>We choose the simplest system that does the job and explain it in plain language. If a spreadsheet is enough, we will say so.</span></li>
<li><b>You own it</b><span>Code, data, configuration and documentation are handed to you. We earn the next engagement by being useful, not by being irreplaceable.</span></li>
<li><b>People stay in charge</b><span>Automation handles the routine path. People handle exceptions, judgement and relationships, and the system makes that hand-off smooth.</span></li>
<li><b>Measured, not claimed</b><span>We baseline before we build and report against the same measures after. We do not publish results we cannot back up.</span></li>
<li><b>Careful with data</b><span>Least-privilege access, encrypted secrets and POPIA-aware handling are defaults, not extras.</span></li></ul>''')
h += sec('alt', '''<div class="text-center"><div class="eyebrow reveal">Who we work with</div><h2 class="heading-lg reveal">Two kinds of client.</h2></div>
<div class="grid-2 reveal mt-md">
<div class="card"><div class="card-icon">A</div><h3>Owner-led SMEs and mid-market teams</h3><p>Businesses with real volume and real process pain, but without an in-house engineering team. We act as that team for the length of the build and, if you want, afterwards.</p></div>
<div class="card"><div class="card-icon">B</div><h3>Agencies and consultancies</h3><p>Firms that sell automation, AI or data work to their own clients and want a dependable build partner behind them. Partner programmes are in development.</p></div></div>''')
h += sec('light', '''<div class="eyebrow reveal">Method</div><h2 class="heading-lg reveal">Our vocabulary is our method.</h2>
<div class="pr reveal mt-md"><div><h4>Unpack</h4><p>Map how the business really runs and where time and money leak.</p></div><div><h4>Prioritise</h4><p>Choose the build that pays back fastest and fix the scope.</p></div><div><h4>Forge</h4><p>Design, build and test with you in the loop.</p></div><div><h4>Run</h4><p>Launch, monitor and keep improving.</p></div></div>
<div class="mt-lg reveal"><a href="process.html" class="btn-dark">See the delivery process →</a></div>''')
h += cta('Let us look at your process.')
pages['about.html'] = h + TAIL

# ───────────── FAQ ─────────────
h = head('FAQ — DigitalFoundry', 'Answers about scope, pricing, timelines, ownership, data handling and how DigitalFoundry builds AI agents, automation and data infrastructure.', 'faq.html',
         jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}))
h += mini_hero('FAQ', 'Straight answers to the questions we hear most.', 'If yours is not here, tell us what you are trying to fix and we will answer it directly.')
h += sec('light', faq_items(FAQS))
h += cta('Still have a question?', 'Describe the process you want to fix. We will tell you plainly whether we can help.')
pages['faq.html'] = h + TAIL

# ───────────── CONTACT ─────────────
h = head('Start a project — DigitalFoundry', 'Tell DigitalFoundry what is slowing your business down. We will tell you plainly whether we can fix it, and what it would take.', 'contact.html')
h += mini_hero('Start a project', 'Got a process that should run itself?', 'Tell us what is slowing the business down. We reply with a plain view of whether we can help and what the first step would be.')
h += sec('dark', '''<div class="grid-2"><div>
<div class="eyebrow reveal">Project brief</div><h2 class="heading-lg reveal">Write it down once.</h2>
<p class="text-body reveal">Fill in the short brief and we will assemble it into a clean summary you can copy and send as soon as our contact details are live.</p>
<p class="text-body reveal">Direct contact details are being set up and will appear on this page. Until then nothing you type here is sent anywhere: the brief is built in your browser only.</p>
<div class="mt-md reveal"><span class="soon">CONTACT DETAILS COMING SOON</span></div>
<ul class="checks mt-lg reveal"><li>Reply with a plain yes or no on fit</li><li>First step is Unpack: a short, scoped process review</li><li>Written scope and price before any build</li></ul></div>
<div class="card reveal"><form class="contact-form" id="brief">
<div><label for="n">Your name</label><input id="n" name="name" required autocomplete="name"></div>
<div><label for="b">Business</label><input id="b" name="biz" required autocomplete="organization"></div>
<div><label for="a">Interested in</label><select id="a" name="area"><option>AI agents</option><option>Workflow automation</option><option>Data infrastructure</option><option>Not sure yet</option></select></div>
<div><label for="s">Team size</label><select id="s" name="size"><option>1-10</option><option>11-50</option><option>51-200</option><option>200+</option></select></div>
<div><label for="m">What is slowing the business down?</label><textarea id="m" name="msg" required></textarea></div>
<button class="btn-primary" type="submit" style="justify-content:center">Build my brief</button>
<div class="brief-out" id="briefOut"></div><p id="briefNote" style="display:none;font-size:13px;color:var(--mint)">Brief built and copied to your clipboard. Keep it handy: our contact details will be published here shortly.</p>
</form></div></div>''')
pages['contact.html'] = h + TAIL

# ───────────── PRIVACY ─────────────
h = head('Privacy Policy — DigitalFoundry', 'How DigitalFoundry handles personal information on this website.', 'privacy.html')
h += mini_hero('Legal', 'Privacy policy', 'Short and plain. Last updated 14 October 2026.')
h += sec('light', '''<div class="prose max-narrow">
<h2>What this website collects</h2><p>This website does not use accounts, tracking cookies or advertising pixels. The project brief form on the contact page runs entirely in your browser: what you type is not transmitted to us or to any third party.</p>
<h2>Third-party services</h2><p>Fonts are loaded from Google Fonts, which may receive your IP address and browser details as part of serving the font files. The site is hosted on GitHub Pages, which keeps standard server logs.</p>
<h2>If you contact us</h2><p>When you contact us by any channel, we use what you share only to respond to you and to scope work you ask about. We do not sell personal information. We keep it only as long as needed for that purpose.</p>
<h2>Your rights</h2><p>Under the Protection of Personal Information Act (POPIA) you may ask what information we hold about you, and ask us to correct or delete it. Contact details for these requests will be published on this site.</p>
<h2>Changes</h2><p>If this policy changes, the date above will change with it.</p></div>''')
pages['privacy.html'] = h + TAIL

# ───────────── 404 ─────────────
h = head('Page not found — DigitalFoundry', 'This page could not be found.', '404.html')
h += '<section class="hero hero-mini" style="min-height:80vh;display:flex;align-items:center"><div class="hero-gradient"></div><div class="hero-content"><div class="hero-eyebrow">404</div><h1 class="hero-title">This page did not make it out of the mould.</h1><p class="hero-sub">The page you asked for does not exist or has moved.</p><div class="hero-buttons" style="margin-top:30px"><a class="btn-primary" href="index.html">Back to home</a><a class="btn-outline" href="contact.html">Start a project</a></div></div></section>\n'
pages['404.html'] = h + TAIL

for k, v in pages.items():
    (root / k).write_text(v, encoding='utf-8')
urls = ''.join(f'<url><loc>{BASE}{"" if k=="index.html" else k}</loc></url>' for k in pages if k != '404.html')
(root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>', encoding='utf-8')
(root / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n', encoding='utf-8')
print(len(pages), 'pages')
