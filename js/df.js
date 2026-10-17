/* DigitalFoundry - nav, footer, reveal, FAQ, enquiry form */
(function(){'use strict';
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const NAV=[['index.html','Home'],['capabilities.html','Services'],['process.html','Our approach'],['work.html','Engagements'],['about.html','About'],['faq.html','FAQ']];
const SUB=['ai-agents.html','workflow-automation.html','data-infrastructure.html'];
const page=location.pathname.split('/').pop()||'index.html';
const nav=$('#nav');
if(nav){nav.innerHTML='<div class="wrap nav-in"><a class="nav-logo" href="index.html" aria-label="DigitalFoundry home"><img src="assets/logo-light.svg" alt="DigitalFoundry"></a><div class="nav-links">'+
NAV.map(n=>`<a href="${n[0]}"${page===n[0]||(n[0]==='capabilities.html'&&SUB.includes(page))?' class="active"':''}>${n[1]}</a>`).join('')+
'<a class="cta-n" href="contact.html">Talk to us</a></div><button class="burger" id="bg" aria-label="Menu"><span></span><span></span><span></span></button></div>';
const m=document.createElement('div');m.className='mm';m.innerHTML='<button id="mc" aria-label="Close">&times;</button>'+NAV.map(n=>`<a href="${n[0]}">${n[1]}</a>`).join('')+'<a href="contact.html" style="color:var(--cyan)">Talk to us</a>';
document.body.appendChild(m);$('#bg').onclick=()=>m.classList.add('open');$('#mc').onclick=()=>m.classList.remove('open')}
const ft=$('#foot');
if(ft){ft.innerHTML='<div class="wrap"><div class="foot-in"><div><img src="assets/logo-dark.svg" alt="DigitalFoundry"><p>A software engineering firm and business partner. We build the systems that help growing companies operate with confidence. Based in South Africa, serving clients worldwide.</p></div>'+
'<div><h4>Services</h4><ul><li><a href="ai-agents.html">Intelligent assistants</a></li><li><a href="workflow-automation.html">Operations automation</a></li><li><a href="data-infrastructure.html">Business intelligence</a></li><li><a href="process.html">Our approach</a></li></ul></div>'+
'<div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="work.html">Engagements</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Talk to us</a></li><li><a href="privacy.html">Privacy policy</a></li></ul></div></div>'+
'<div class="foot-b"><span>&copy; '+new Date().getFullYear()+' DigitalFoundry. All rights reserved.</span><span>We forge the systems your business runs on.</span></div></div>'}
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('v');io.unobserve(e.target)}}),{threshold:.1});
$$('.rv').forEach(e=>io.observe(e));
$$('.fi').forEach(it=>{const q=it.querySelector('.fq'),a=it.querySelector('.fa');q.addEventListener('click',()=>{const o=it.classList.toggle('open');a.style.maxHeight=o?a.scrollHeight+'px':0;q.setAttribute('aria-expanded',o)})});
const f=$('#brief');
if(f)f.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(f);
const t=`DigitalFoundry enquiry\nName: ${d.get('name')}\nCompany: ${d.get('biz')}\nArea of interest: ${d.get('area')}\nCompany size: ${d.get('size')}\n\nObjective:\n${d.get('msg')}`;
const o=$('#briefOut');o.style.display='block';o.textContent=t;if(navigator.clipboard)navigator.clipboard.writeText(t).catch(()=>{});$('#briefNote').style.display='block'});
})();
