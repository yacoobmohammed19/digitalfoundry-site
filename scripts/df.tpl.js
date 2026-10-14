/* DigitalFoundry — shared components & behaviour */
(function(){
'use strict';
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const NAV=[['index.html','Home'],['capabilities.html','Capabilities'],['process.html','Process'],['work.html','Work'],['about.html','About'],['faq.html','FAQ']];
const FOOT=[['capabilities.html','Capabilities'],['ai-agents.html','AI agents'],['workflow-automation.html','Workflow automation'],['data-infrastructure.html','Data infrastructure'],['process.html','Delivery process'],['work.html','Work'],['about.html','About'],['faq.html','FAQ'],['contact.html','Start a project'],['privacy.html','Privacy policy']];
const page=(location.pathname.split('/').pop()||'index.html');
const SUB=['ai-agents.html','workflow-automation.html','data-infrastructure.html'];

/* nav + footer + mobile menu */
const nav=$('#site-nav');
if(nav){
 nav.innerHTML='<div class="nav-inner"><a href="index.html" class="nav-logo" aria-label="DigitalFoundry home"><img src="assets/logo-dark.svg" alt="DigitalFoundry"></a><div class="nav-links">'+
 NAV.map(n=>`<a href="${n[0]}" ${(page===n[0]||(n[0]==='capabilities.html'&&SUB.includes(page)))?'class="active"':''}>${n[1]}</a>`).join('')+
 '<a href="contact.html" class="nav-cta">Start a project</a></div><button class="mobile-toggle" id="mt" aria-label="Menu"><span></span><span></span><span></span></button></div>';
 const m=document.createElement('div');m.className='mobile-menu';m.id='mm';
 m.innerHTML='<button class="mobile-menu-close" id="mc" aria-label="Close">×</button>'+NAV.map(n=>`<a href="${n[0]}">${n[1]}</a>`).join('')+'<a href="contact.html" style="color:var(--mint)">Start a project</a>';
 document.body.appendChild(m);
 $('#mt').onclick=()=>m.classList.add('open');$('#mc').onclick=()=>m.classList.remove('open');
 const sc=()=>nav.classList.toggle('scrolled',scrollY>20);addEventListener('scroll',sc,{passive:true});sc();
}
const ft=$('#site-footer');
if(ft){
 ft.innerHTML='<div class="footer-inner"><div><img src="assets/logo-dark.svg" alt="DigitalFoundry"><p>We forge the systems your business runs on. AI agents, workflow automation and data infrastructure, built in South Africa.</p></div>'+
 '<div><h4>Explore</h4><ul>'+FOOT.slice(0,6).map(l=>`<li><a href="${l[0]}">${l[1]}</a></li>`).join('')+'</ul></div>'+
 '<div><h4>Company</h4><ul>'+FOOT.slice(6).map(l=>`<li><a href="${l[0]}">${l[1]}</a></li>`).join('')+'</ul></div></div>'+
 '<div class="footer-base"><span>© '+new Date().getFullYear()+' DigitalFoundry. All rights reserved.</span><span>Built in South Africa. Delivered everywhere.</span></div>';
}

/* cursor + grain + global particle canvas */
const g=document.createElement('div');g.className='grain';document.body.appendChild(g);
if(matchMedia('(hover:hover) and (pointer:fine)').matches){
 const d=document.createElement('div'),r=document.createElement('div');d.className='cursor-dot';r.className='cursor-ring';document.body.append(d,r);document.body.classList.add('has-cursor');
 let x=0,y=0,rx=0,ry=0;addEventListener('mousemove',e=>{x=e.clientX;y=e.clientY;d.style.transform=`translate(${x}px,${y}px)`},{passive:true});
 (function loop(){rx+=(x-rx)*.16;ry+=(y-ry)*.16;r.style.transform=`translate(${rx}px,${ry}px)`;requestAnimationFrame(loop)})();
 document.addEventListener('mouseover',e=>{r.classList.toggle('hovering',!!e.target.closest('a,button,.node,.tab,.model,.ph'))});
}
function particles(cv,n,link){
 const c=cv.getContext('2d');let W,H,P=[];
 const size=()=>{const b=cv.parentElement===document.body?{width:innerWidth,height:innerHeight}:cv.parentElement.getBoundingClientRect();W=cv.width=b.width;H=cv.height=b.height;
  P=Array.from({length:Math.min(n,Math.round(W*H/16000))},()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.35,vy:(Math.random()-.5)*.35,r:Math.random()*1.6+.6}))};
 size();addEventListener('resize',size);
 const still=matchMedia('(prefers-reduced-motion:reduce)').matches;
 (function f(){c.clearRect(0,0,W,H);
  for(const p of P){if(!still){p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1}
   c.beginPath();c.arc(p.x,p.y,p.r,0,6.283);c.fillStyle='rgba(95,227,210,.7)';c.fill()}
  if(link)for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){const dx=P[i].x-P[j].x,dy=P[i].y-P[j].y,dd=dx*dx+dy*dy;
   if(dd<14000){c.strokeStyle=`rgba(18,196,176,${.22*(1-dd/14000)})`;c.lineWidth=1;c.beginPath();c.moveTo(P[i].x,P[i].y);c.lineTo(P[j].x,P[j].y);c.stroke()}}
  if(!still)requestAnimationFrame(f)})();
}
const gc=document.createElement('canvas');gc.className='global-canvas';document.body.prepend(gc);particles(gc,70,false);
const hc=$('#heroCanvas');if(hc)particles(hc,90,true);

/* hero title word animation */
$$('.hero-title').forEach(t=>{
 if(!t.querySelector('.word')){t.innerHTML=t.textContent.split(' ').map(w=>`<span class="word">${w}</span>`).join(' ')}
 t.querySelectorAll('.word').forEach((w,i)=>setTimeout(()=>w.classList.add('visible'),150+i*110))});

/* scroll words + reveal */
$$('.scroll-words').forEach(el=>{
 const walk=n=>[...n.childNodes].forEach(c=>{
  if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t.trim()){f.append(t)}else{const s=document.createElement('span');s.className='sw';s.textContent=t;f.append(s)}});c.replaceWith(f)}
  else if(c.nodeType===1)walk(c)});walk(el)});
function wordsOnScroll(){$$('.scroll-words').forEach(el=>{const r=el.getBoundingClientRect(),p=Math.min(1,Math.max(0,(innerHeight*.9-r.top)/(innerHeight*.55+r.height*.4)));
 const w=el.querySelectorAll('.sw'),k=Math.round(p*w.length);w.forEach((s,i)=>s.classList.toggle('lit',i<k))})}
addEventListener('scroll',wordsOnScroll,{passive:true});wordsOnScroll();
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;io.unobserve(e.target);e.target.classList.add('visible');
 e.target.querySelectorAll('[data-n]').forEach(c=>{const n=+c.dataset.n;let s=null;const f=t=>{s=s||t;const p=Math.min((t-s)/1200,1);c.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)})}),{threshold:.12});
$$('.reveal,.scroll-para,.strip').forEach(e=>io.observe(e));
$$('.scroll-stagger').forEach(s=>[...s.children].forEach((c,i)=>c.style.transitionDelay=i*.12+'s'));

/* FAQ accordion */
$$('.faq-item').forEach(it=>{const q=it.querySelector('.faq-q'),a=it.querySelector('.faq-a');
 q.addEventListener('click',()=>{const o=it.classList.toggle('open');a.style.maxHeight=o?a.scrollHeight+'px':0;q.setAttribute('aria-expanded',o)})});

/* terminal */
const term=$('#term');
if(term){const L=[
'<span class="d">$</span> <span class="k">foundry</span> unpack --client acme',
'<span class="ok">✓</span> 14 processes mapped, 3 prioritised',
'<span class="d">$</span> <span class="k">foundry</span> forge intake-agent',
'<span class="ok">✓</span> knowledge base indexed',
'<span class="ok">✓</span> guardrails + escalation rules set',
'<span class="ok">✓</span> connected: CRM · WhatsApp · accounting',
'<span class="d">$</span> <span class="k">foundry</span> run --monitor',
'<span class="ok">●</span> live · 24/7 · human hand-off armed<span class="cur"></span>'];
 let i=0;const step=()=>{if(i>=L.length)return;i++;term.innerHTML=L.slice(0,i).join('\n');setTimeout(step,i%2?650:420)};
 if(matchMedia('(prefers-reduced-motion:reduce)').matches)term.innerHTML=L.join('\n');else step()}

/* interactive architecture explorer */
/*@S*/
const tabsEl=$('#tabs');
if(tabsEl){
 const only=tabsEl.dataset.only;let cur=only!==undefined?+only:0,sel=null;
 const render=()=>{const s=S[cur];
  tabsEl.innerHTML=only!==undefined?'':S.map((x,i)=>`<button class="tab ${i==cur?'on':''}" role="tab" aria-selected="${i==cur}" data-i="${i}">${x.k}</button>`).join('');
  $('#spec').innerHTML=`<h3>${s.t}</h3><p>${s.p}</p><ul class="spec">${s.spec.map(r=>`<li><b>${r[0]}</b><span>${r[1]}</span></li>`).join('')}</ul>`;
  const W=160,H=62;let h='<rect class="zone" x="6" y="14" width="548" height="338" rx="14"/><text class="zl" x="20" y="30">SYSTEM BOUNDARY</text>';
  h+=s.edges.map(e=>{const a=s.nodes[e[0]],b=s.nodes[e[1]];const x1=a[3]+W/2,y1=a[4]+H/2,x2=b[3]+W/2,y2=b[4]+H/2;
   const p=`M${x1} ${y1} C${(x1+x2)/2} ${y1},${(x1+x2)/2} ${y2},${x2} ${y2}`;const on=sel!==null&&(s.nodes[sel]==a||s.nodes[sel]==b);
   return `<path class="edge" d="${p}"/><path class="flow" style="opacity:${on?1:.3}" d="${p}"/>`}).join('');
  h+=s.nodes.map((n,i)=>`<g class="node ${sel===i?'on':''}" tabindex="0" role="button" data-i="${i}"><rect x="${n[3]}" y="${n[4]}" width="${W}" height="${H}" rx="10"/><text x="${n[3]+14}" y="${n[4]+27}">${n[1]}</text><text class="sm" x="${n[3]+14}" y="${n[4]+46}">${n[2]}</text></g>`).join('');
  $('#dg').innerHTML=h;
  const dd=sel===null?['Select a component','Hover or tap any node to see what it does and how it connects.']:[s.nodes[sel][1],s.d[s.nodes[sel][0]]];
  $('#det').innerHTML=`<b>${dd[0]}</b>${dd[1]}`};
 const pick=i=>{if(sel===i)return;sel=i;render()};
 tabsEl.addEventListener('click',e=>{const b=e.target.closest('.tab');if(b){cur=+b.dataset.i;sel=null;render()}});
 $('#dg').addEventListener('click',e=>{const n=e.target.closest('.node');if(n)pick(+n.dataset.i)});
 $('#dg').addEventListener('mouseover',e=>{const n=e.target.closest('.node');if(n)pick(+n.dataset.i)});
 $('#dg').addEventListener('focusin',e=>{const n=e.target.closest('.node');if(n)pick(+n.dataset.i)});
 render();
}

/* engagement models */
/*@E*/
const engEl=$('#eng');
if(engEl){let em=0;const rE=()=>{engEl.innerHTML=E.map((m,i)=>`<button class="model ${i==em?'on':''}" aria-pressed="${i==em}" data-i="${i}"><span class="t">${m.t}</span><h3>${m.n}</h3><p>${m.p}</p><ul>${m.l.map(x=>`<li>${x}</li>`).join('')}</ul></button>`).join('');
 const m=E[em];$('#fit').innerHTML=[m.f,m.g,m.o].map(x=>`<div><h4>${x[0]}</h4><p>${x[1]}</p></div>`).join('')};
 engEl.addEventListener('click',e=>{const b=e.target.closest('.model');if(b){em=+b.dataset.i;rE()}});rE()}

/* process timeline */
/*@P*/
const tl=$('#tl');
if(tl){let pi=0;const rP=()=>{tl.innerHTML=P.map((x,i)=>`<button class="ph ${i==pi?'on':''}" aria-expanded="${i==pi}" data-i="${i}"><span class="dot"></span><div class="wk">${x.w}</div><h3>${x.n}</h3><p>${x.p}</p><div class="more"><ul>${x.l.map(y=>`<li>${y}</li>`).join('')}</ul><div class="out">${x.o}</div></div></button>`).join('')};
 tl.addEventListener('click',e=>{const b=e.target.closest('.ph');if(b){pi=+b.dataset.i;rP()}});rP()}

/* ROI calculator */
if($('#r1')){const calc=()=>{const a=+$('#r1').value,b=+$('#r2').value,c=+$('#r3').value;
 $('#v1').textContent=a;$('#v2').textContent=b+' min';$('#v3').textContent=c+'%';
 const h=a*b*(c/100)*52/12/60;$('#o1').textContent=Math.round(h).toLocaleString('en-ZA');$('#o2').textContent=Math.round(h*12/8)};
 ['r1','r2','r3'].forEach(i=>$('#'+i).addEventListener('input',calc));calc()}

/* project brief builder (no public contact details yet: builds a copyable brief) */
const bf=$('#brief');
if(bf){bf.addEventListener('submit',e=>{e.preventDefault();const f=new FormData(bf);
 const t='DigitalFoundry project brief\nName: '+f.get('name')+'\nBusiness: '+f.get('biz')+'\nInterested in: '+f.get('area')+'\nTeam size: '+f.get('size')+'\n\nWhat is slowing the business down:\n'+f.get('msg');
 const o=$('#briefOut');o.style.display='block';o.textContent=t;
 if(navigator.clipboard)navigator.clipboard.writeText(t).catch(()=>{});
 $('#briefNote').style.display='block'})}
})();
