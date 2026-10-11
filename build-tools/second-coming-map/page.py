# -*- coding: utf-8 -*-
import json,sys
sys.path.insert(0,'.')
import content as C
data=open('data.json',encoding='utf-8').read()
parts=json.dumps([{'id':a,'name':b} for a,b in C.PARTS],ensure_ascii=False)
glance=json.dumps(C.GLANCE,ensure_ascii=False)
notclaim=json.dumps(C.CLAIMS_NOT,ensure_ascii=False)
TITLE="The Second Coming Map | Zay-Marie Press"
DESC="An interactive map of the Second Coming: the four wars, the judgments and who stands at each, and the inauguration of the kingdom, in order, with every passage and where Scripture gives no sequence."
CSS=r"""
:root{--navy:#0b1628;--panel:#14223a;--panel2:#101c31;--gold:#d4af37;--blue:#62a5ff;--green:#72bd8a;--red:#e06b5f;--white:#f7f7f2;--muted:#c4cad4;--dim:#8f9bad;--line:#32435f;--war:#8c2a22;--jud:#1f4f82;--kin:#176536;--apart:#3a4252;--coming:#5b4514}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(circle at 50% 0,#12213a 0,var(--navy) 55%);color:var(--muted);font:17px/1.55 Arial,sans-serif}
a{color:var(--gold)}.wrap{width:min(1120px,94%);margin:auto}
.top{position:sticky;top:0;z-index:20;background:rgba(8,17,32,.96);border-bottom:1px solid #1d2a40}
.nav{display:flex;justify-content:space-between;align-items:center;min-height:62px}
.brand{font:700 20px Georgia,serif;color:var(--gold);text-decoration:none}
.navlinks{display:flex;gap:24px;font-weight:700;font-size:14px}.navlinks a{text-decoration:none;color:var(--muted)}
.hero{text-align:center;padding:76px 0 30px}.eyebrow{color:var(--gold);font-weight:700;letter-spacing:.28em;font-size:13px}
.hero h1{font:700 clamp(40px,7vw,68px)/1.05 Georgia,serif;color:var(--gold);margin:20px 0 8px}
.hero h2{font:italic 22px Georgia,serif;color:var(--white);font-weight:400;margin:0}
.intro{max-width:860px;margin:34px auto 0}.intro p{margin:0 0 14px}
.legend{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:22px 0 0;font-size:14px}
.legend span{background:var(--panel);border:1px solid var(--line);padding:8px 12px;border-radius:7px}
.tag{display:inline-block;font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:10px;margin-right:6px;vertical-align:1px}
.t-S{background:#1b4a30;color:#b8e6c7}.t-C{background:#1d3f66;color:#bcd9ff}.t-I{background:#5b4514;color:#f1d98a}
.actions{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:24px}
.btn{border:1px solid var(--gold);background:var(--gold);color:#091426;padding:11px 18px;border-radius:5px;font-weight:800;text-decoration:none;cursor:pointer;font-size:14px;font-family:inherit}
.btn.alt{background:transparent;color:var(--white)}.btn[disabled]{opacity:.4;cursor:default}
section{padding:34px 0;scroll-margin-top:70px}.section-title{text-align:center;font:700 32px Georgia,serif;color:var(--white);margin:0 0 8px}
.section-sub{text-align:center;color:#8590a2;margin:0 auto 24px;max-width:760px}
/* filter */
.filter{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:0 0 22px}
.filter-label{width:100%;text-align:center;font-size:13px;color:var(--dim);letter-spacing:.04em}
.chip{background:var(--panel);color:var(--muted);border:1px solid var(--line);border-radius:20px;padding:8px 14px;font:700 13px Arial,sans-serif;cursor:pointer}
.chip[aria-pressed=true]{background:var(--gold);color:#091426;border-color:var(--gold)}
/* route */
.route{display:grid;gap:0}
.band{display:grid;grid-template-columns:150px 1fr;gap:16px;align-items:stretch;border-radius:12px}
.band-label{border-radius:10px;padding:14px;color:var(--white);font:700 15px Georgia,serif;display:flex;flex-direction:column;justify-content:center}
.band-label small{font:12px Arial,sans-serif;font-weight:400;color:#e3e6ec;opacity:.85;margin-top:4px}
.band.apart .band-label{background:var(--apart)}.band.coming .band-label{background:var(--coming)}.band.war .band-label{background:var(--war)}.band.judgment .band-label{background:var(--jud)}.band.kingdom .band-label{background:var(--kin)}
.nodes{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px}
.arrow{text-align:center;color:var(--gold);font-size:20px;line-height:1;margin:6px 0;padding-left:166px}
.node{text-align:left;background:var(--panel);color:var(--muted);border:1px solid var(--line);border-top:4px solid var(--line);border-radius:10px;padding:12px 14px;cursor:pointer;font:inherit;position:relative;min-height:112px;display:flex;flex-direction:column;align-items:flex-start;justify-content:flex-start;transition:opacity .15s,border-color .15s}
.node:hover{border-color:var(--gold)}
.band.war .node{border-top-color:#c0453a}.band.judgment .node{border-top-color:#3b82d0}.band.kingdom .node{border-top-color:#3aa05f}.band.coming .node{border-top-color:#c9a23c}.band.apart .node{border-top-color:#6b7488;background:var(--panel2)}
.node[aria-pressed=true]{border-color:var(--gold);box-shadow:0 0 0 2px var(--gold) inset;background:#1a2c4a}
.node .n{display:inline-flex;width:28px;height:28px;border-radius:50%;background:#0b1628;border:1px solid var(--gold);color:var(--gold);align-items:center;justify-content:center;font-weight:800;font-size:14px;margin-bottom:6px}
.node .t{display:block;font:700 16px/1.25 Georgia,serif;color:var(--white)}
.node .s{display:block;font-size:13px;color:var(--dim);margin-top:4px;line-height:1.4}
.node .role{display:none;white-space:normal;margin-top:8px;font-size:12px;font-weight:800;color:#091426;background:var(--gold);border-radius:10px;padding:2px 9px;width:max-content;max-width:100%}
body.filtering .node.dim{opacity:.32}body.filtering .node.on .role{display:inline-block}
body.filtering .node.on{border-color:var(--gold)}
/* detail */
.detail{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:30px;margin-top:26px;scroll-margin-top:80px}
.detail:focus{outline:none}
.d-head{display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap;justify-content:space-between}
.d-head h3{font:700 30px/1.15 Georgia,serif;color:var(--white);margin:0 0 6px}
.pill{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:3px 11px;border-radius:12px;color:var(--white)}
.pill.war{background:var(--war)}.pill.judgment{background:var(--jud)}.pill.kingdom{background:var(--kin)}.pill.coming{background:var(--coming)}.pill.apart{background:var(--apart)}
.d-nav{display:flex;gap:8px}
.when-where{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:18px 0}
.box{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.box h4,.d-sec h4{margin:0 0 6px;font:700 13px Georgia,serif;letter-spacing:.08em;text-transform:uppercase;color:var(--gold)}
.box p{margin:0}
.reading{font-size:18px;color:#dfe3ea;margin:6px 0 20px}
.facts{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-bottom:22px}
.who{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:6px 18px}
.who li{display:flex;gap:10px;align-items:baseline;font-size:15px;padding:6px 0;border-bottom:1px solid #22324d}
.who li.no{opacity:.55}
.who .nm{flex:0 0 46%;color:var(--white);font-weight:700}
.cd{display:inline-block;min-width:62px;text-align:center;font-size:11px;font-weight:800;border-radius:9px;padding:2px 7px;margin-right:6px;color:#091426}
.c-K{background:var(--gold)}.c-J{background:#e58a80}.c-P{background:#8fb8f0}.c-E{background:#b0443a;color:#fff}.c-G{background:#7fd0a0}.c-B{background:#c7a6f0}.c-X{background:#2a3a55;color:#7e8aa0}
.d-sec{margin-top:22px}
details.pass{border:1px solid var(--line);border-radius:9px;margin:8px 0;background:var(--panel2)}
details.pass summary{cursor:pointer;padding:11px 14px;list-style:none;display:block}
details.pass summary::-webkit-details-marker{display:none}
details.pass summary:before{content:"▸";color:var(--gold);margin-right:8px}details.pass[open] summary:before{content:"▾"}
.ref{font:italic 700 16px Georgia,serif;color:var(--gold)}.pnote{display:block;font-size:14px;color:var(--dim);margin:3px 0 0 20px}
.kjv{padding:4px 18px 14px 34px;color:#dfe3ea;font:16px/1.65 Georgia,serif}
.kjv sup{color:var(--gold);font:700 11px Arial,sans-serif;margin-right:3px}.kjv .chp{display:block;color:var(--gold);font:700 12px Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;margin:8px 0 2px}
ul.silent{margin:0;padding-left:20px}ul.silent li{margin:7px 0}
.more a{display:inline-block;margin:4px 14px 0 0}
.feats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}
details.feat[open]{grid-column:1/-1}details.feat{border:1px solid var(--line);border-radius:10px;background:var(--panel2);align-self:start}
details.feat summary{cursor:pointer;padding:12px 14px;list-style:none}details.feat summary::-webkit-details-marker{display:none}
details.feat .ft{display:block;font:700 16px Georgia,serif;color:var(--white)}details.feat .fl{display:block;font-size:13px;color:var(--dim);margin-top:3px}
details.feat .fr{display:block;font:italic 13px Georgia,serif;color:var(--gold);margin-top:5px}
details.feat .fb{padding:0 14px 12px}details.feat .fb p.note{font-size:14px;color:var(--dim)}
details.feat .fb .ref{font-size:14px;display:block;margin-top:8px}details.feat .kjv{padding:2px 0 0 0;font-size:15px}
/* tables */
.tw{overflow-x:auto;border-radius:12px;border:1px solid var(--line);background:var(--panel)}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:11px 13px;border-bottom:1px solid var(--line);font-size:15px;vertical-align:top}
th{background:#3a3422;color:var(--gold);font-size:13px;letter-spacing:.04em}
td:first-child{font-weight:800;color:var(--white)}
.mx th,.mx td{text-align:center;padding:8px 6px;font-size:12px}
.mx th:first-child,.mx td:first-child{text-align:left;position:sticky;left:0;background:var(--panel);min-width:150px;font-size:13px;z-index:1}
.mx th:first-child{background:#3a3422}
.mx th button{background:none;border:0;color:var(--gold);font:800 13px Arial,sans-serif;cursor:pointer;padding:4px 6px}
.mx td button.rowbtn{background:none;border:0;color:var(--white);font:700 13px Arial,sans-serif;text-align:left;cursor:pointer;padding:0}
.mx td .cd{margin:0;min-width:56px}
.gl td:first-child{width:22%}
.nc{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:22px 26px}
.nc ul{margin:0;padding-left:20px}.nc li{margin:9px 0}
.footer{text-align:center;border-top:1px solid #1d2a40;padding:32px;color:#788497;font-size:14px}.footer strong{color:var(--gold)}
#printall{display:none}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;color:#000;padding:6px;z-index:50}
@media(max-width:860px){.band{grid-template-columns:1fr}.band-label{flex-direction:row;gap:10px;align-items:baseline;padding:10px 14px}.arrow{padding-left:0}.facts,.when-where,.who{grid-template-columns:1fr}.navlinks{display:none}.detail{padding:20px 16px}.d-head h3{font-size:25px}.nodes{grid-template-columns:1fr}.node{min-height:0}.hero{padding-top:54px}}
@media print{.top,.actions,.filter,.route,.arrow,#detail,#matrix-sec,.d-nav,.skip{display:none!important}
body{background:#fff;color:#222;font-size:11pt}.hero h1,.eyebrow,.ref,.d-sec h4,.box h4,.footer strong{color:#8a620f!important}.hero h2,.section-title,.d-head h3,td:first-child{color:#111!important}
#printall{display:block}#printall .detail{display:block!important;background:#fff;color:#222;border:1px solid #aaa;break-inside:avoid;margin:14px 0}.box,details.pass,.nc,.tw,th,td{background:#fff!important;color:#222!important;border-color:#aaa!important}.reading,.kjv{color:#222!important}.pill{color:#fff!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}.tag{border:1px solid #888;background:#fff!important;color:#222!important}.footer{color:#555}}
"""
JS=r"""
(function(){
var D=__DATA__,P=__PARTS__,GL=__GLANCE__,NC=__NC__;
var CODE={K:'Leads',J:'Judged',P:'Present',E:'Opposed',G:'Ground',B:'Bound',X:'—'};
var TAG={S:'Stated',C:'Shown by the context',I:'Inferred'};
var BANDS={apart:['Set apart','not part of the Coming'],coming:['The Coming','the King appears'],war:['The Four Wars','the end of the Tribulation'],judgment:['The Three Judgments','after the wars'],kingdom:['The Kingdom','the thousand years']};
var cur=null,filt=null;
function e(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function byId(id){for(var i=0;i<D.length;i++)if(D[i].id===id)return D[i];return null}
function idx(id){for(var i=0;i<D.length;i++)if(D[i].id===id)return i;return -1}
function pname(id){for(var i=0;i<P.length;i++)if(P[i].id===id)return P[i].name;return id}
function kjv(vs){var h='',c=null;vs.forEach(function(v){if(v.c!==c&&c!==null)h+='<span class="chp">Chapter '+v.c+'</span>';c=v.c;h+='<sup>'+v.v+'</sup>'+e(v.t)+' '});return '<div class="kjv">'+h+'</div>'}
function pass(p,open){return '<details class="pass"'+(open?' open':'')+'><summary><span class="ref">'+e(p.ref)+'</span> <span class="tag t-'+p.tag+'">'+TAG[p.tag]+'</span><span class="pnote">'+e(p.note)+'</span></summary>'+kjv(p.vs)+'</details>'}
function feats(fs,open){var h='<div class="d-sec"><h4>The Kingdom, in Five Pictures</h4><div class="feats">';fs.forEach(function(f){h+='<details class="feat"'+(open?' open':'')+'><summary><span class="ft">'+e(f.name)+'</span><span class="fl">'+e(f.line)+'</span><span class="fr">'+e(f.refs)+'</span></summary><div class="fb">'+(f.note?'<p class="note">'+e(f.note)+'</p>':'');f.passages.forEach(function(p){h+='<span class="ref">'+e(p.ref)+'</span>'+kjv(p.vs)});h+='</div></details>'});return h+'</div></div>'}
function detail(s,print){
 var b=BANDS[s.band][0];var h='<div class="d-head"><div><span class="pill '+s.band+'">'+e(b)+'</span><h3>'+(s.num==='◇'?'':e(s.num)+'. ')+e(s.title)+'</h3></div>';
 if(!print)h+='<div class="d-nav"><button class="btn alt" data-nav="-1">← Previous</button><button class="btn alt" data-nav="1">Next →</button></div>';
 h+='</div><div class="when-where"><div class="box"><h4>When</h4><p>'+e(s.when)+'</p></div><div class="box"><h4>Where</h4><p>'+e(s.where)+'</p></div></div>';
 h+='<p class="reading">'+e(s.reading)+'</p><div class="facts"><div class="box"><h4>Who presides or fights</h4><p>'+e(s.presides)+'</p></div><div class="box"><h4>Who is judged or opposed</h4><p>'+e(s.judged)+'</p></div><div class="box"><h4>The ground</h4><p>'+e(s.ground)+'</p></div><div class="box"><h4>The outcome</h4><p>'+e(s.outcome)+'</p></div></div>';
 h+='<div class="d-sec"><h4>Who is at this event</h4><ul class="who">';
 P.forEach(function(p){var r=s.roles[p.id];h+='<li'+(r[0]==='X'?' class="no"':'')+'><span class="nm">'+e(p.name)+'</span><span><span class="cd c-'+r[0]+'">'+CODE[r[0]]+'</span>'+e(r[1]||(r[0]==='X'?'Not at this event':''))+'</span></li>'});
 h+='</ul></div><div class="d-sec"><h4>The passages <span style="text-transform:none;letter-spacing:0;color:#8f9bad;font-weight:400">(tap a passage to read it in the KJV)</span></h4>';
 s.passages.forEach(function(p){h+=pass(p,print)});h+='</div>';
 if(s.features)h+=feats(s.features,print);
 h+='<div class="d-sec"><h4>What Scripture does not say</h4><ul class="silent">';s.silent.forEach(function(t){h+='<li>'+e(t)+'</li>'});h+='</ul></div>';
 if(s.more&&s.more.length){h+='<div class="d-sec more"><h4>Go deeper</h4>';s.more.forEach(function(m){h+='<a href="'+e(m[1])+'">'+e(m[0])+'</a>'});h+='</div>'}
 return h}
function route(){
 var order=['apart:seat','coming','war','judgment','kingdom','apart:gwt'],h='';
 var groups=[['apart',['seat']],['coming',['appears']],['war',['jerusalem','bozrah','armageddon','cleansing']],['judgment',['wheat','nations','stewards']],['kingdom',['kingdom']],['apart',['gwt']]];
 var lab=[['Before the Coming','Outside the nine events'],['The Coming','The King appears'],['The Four Wars','End of the Tribulation'],['The Three Judgments','After the wars'],['The Kingdom','The thousand years'],['After the Kingdom','Outside the nine events']];
 groups.forEach(function(g,i){
  h+='<div class="band '+g[0]+'"><div class="band-label">'+lab[i][0]+'<small>'+lab[i][1]+'</small></div><div class="nodes">';
  g[1].forEach(function(id){var s=byId(id);h+='<button class="node" data-id="'+s.id+'" aria-pressed="false"><span class="n">'+e(s.num)+'</span><span class="t">'+e(s.title)+'</span><span class="s">'+e(s.short)+'</span><span class="role"></span></button>'});
  h+='</div></div>';if(i<groups.length-1)h+='<div class="arrow" aria-hidden="true">↓</div>'});
 document.getElementById('route').innerHTML=h}
function chips(){var h='<span class="filter-label">Follow one participant through the map</span><button class="chip" data-p="" aria-pressed="true">Everyone</button>';
 P.forEach(function(p){h+='<button class="chip" data-p="'+p.id+'" aria-pressed="false">'+e(p.name.replace(/ \(.*/,''))+'</button>'});document.getElementById('filter').innerHTML=h}
function applyFilter(){
 document.body.classList.toggle('filtering',!!filt);
 document.querySelectorAll('.node').forEach(function(n){var s=byId(n.dataset.id),r=filt?s.roles[filt]:null,on=filt&&r[0]!=='X';n.classList.toggle('on',!!on);n.classList.toggle('dim',!!filt&&!on);n.querySelector('.role').textContent=on?(CODE[r[0]]+(r[1]?': '+r[1]:'')):''});
 document.querySelectorAll('.chip').forEach(function(c){c.setAttribute('aria-pressed',String((c.dataset.p||null)===filt))})}
function select(id,scroll){
 var s=byId(id);if(!s)return;cur=id;
 document.querySelectorAll('.node').forEach(function(n){n.setAttribute('aria-pressed',String(n.dataset.id===id))});
 var d=document.getElementById('detail');d.innerHTML=detail(s,false);d.hidden=false;
 try{history.replaceState(null,'','#'+id)}catch(x){}
 if(scroll){d.setAttribute('tabindex','-1');d.scrollIntoView({block:'start'});d.focus({preventScroll:true})}}
function matrix(){
 var h='<table class="mx"><thead><tr><th>Who</th>';D.forEach(function(s){h+='<th><button data-id="'+s.id+'" title="'+e(s.title)+'">'+e(s.num==='◇'?(s.id==='seat'?'◇ Before':'◇ After'):s.num)+'</button></th>'});h+='</tr></thead><tbody>';
 P.forEach(function(p){h+='<tr><td><button class="rowbtn" data-p="'+p.id+'">'+e(p.name.replace(/ \(.*/,''))+'</button></td>';D.forEach(function(s){var r=s.roles[p.id];h+='<td title="'+e(r[1])+'"><span class="cd c-'+r[0]+'">'+CODE[r[0]]+'</span></td>'});h+='</tr>'});
 document.getElementById('matrix').innerHTML=h+'</tbody></table>'}
function glance(){var h='<table class="gl"><thead><tr><th>Judgment</th><th>When and where</th><th>Who presides</th><th>Who stands there</th><th>The ground</th><th>The verdict</th></tr></thead><tbody>';
 GL.forEach(function(g){var s=byId(g[0]);h+='<tr><td>'+e(s.title)+'</td><td>'+e(g[1])+'</td><td>'+e(g[2])+'</td><td>'+e(g[3])+'</td><td>'+e(g[4])+'</td><td>'+e(g[5])+'</td></tr>'});
 document.getElementById('glance').innerHTML=h+'</tbody></table>'}
function init(){route();chips();matrix();glance();
 var l='';NC.forEach(function(t){l+='<li>'+e(t)+'</li>'});document.getElementById('nc').innerHTML=l;
 var pa='';D.forEach(function(s){pa+='<div class="detail">'+detail(s,true)+'</div>'});document.getElementById('printall').innerHTML=pa;
 document.addEventListener('click',function(ev){
  var t=ev.target.closest('[data-id],[data-p],[data-nav]');if(!t)return;
  if(t.dataset.nav){var i=idx(cur)+parseInt(t.dataset.nav,10);if(i>=0&&i<D.length)select(D[i].id,true);return}
  if(t.classList.contains('node')){select(t.dataset.id,true);return}
  if(t.closest('#matrix')&&t.dataset.id){select(t.dataset.id,true);document.getElementById('map').scrollIntoView();setTimeout(function(){document.getElementById('detail').scrollIntoView({block:'start'})},0);return}
  if(t.dataset.p!==undefined){filt=t.dataset.p||null;if(t.closest('#matrix')&&filt===null)return;applyFilter();if(t.closest('#matrix'))document.getElementById('map').scrollIntoView()}});
 var h=(location.hash||'').replace('#','');if(h&&byId(h))select(h,false)}
init()})();
"""
JS=JS.replace('__DATA__',data).replace('__PARTS__',parts).replace('__GLANCE__',glance).replace('__NC__',notclaim)
HTML=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>{TITLE}</title><meta name="description" content="{DESC}"/><link rel="canonical" href="https://zaymariepress.com/second-coming-map.html"/><link rel="icon" href="assets/zay-marie-press-favicon.png" type="image/png"/><style>{CSS}</style><meta property="og:type" content="website"><meta property="og:site_name" content="Zay-Marie Press"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{DESC}"><meta property="og:url" content="https://zaymariepress.com/second-coming-map.html"><meta property="og:image" content="https://zaymariepress.com/assets/share-site-default.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{TITLE}"><meta name="twitter:description" content="{DESC}"><meta name="twitter:image" content="https://zaymariepress.com/assets/share-site-default.jpg">
</head><body><a class="skip" href="#map">Skip to the map</a><header class="top"><div class="wrap nav"><a class="brand" href="resources.html">Zay-Marie Press</a><nav class="navlinks"><a href="#map">Map</a><a href="#matrix-sec">Who Is Where</a><a href="#judgments">Judgments</a><a href="#limits">Limits</a></nav></div></header>
<main><div class="wrap hero"><div class="eyebrow">ZAY-MARIE PRESS · RESOURCES</div><h1>The Second Coming Map</h1><h2>The Wars, the Judgments and the Kingdom, in Order</h2>
<div class="intro"><p>When the King returns, Scripture describes wars He fights, judgments He holds and a kingdom He opens. This map puts them in order, shows who stands at each one and who is being judged, and marks where the order is Scripture’s own and where it is a reading. Choose any station below to open it.</p>
<p>This guide argues a position, and says so. The map begins at the end of the Tribulation. The Body of Christ is shown only at its own judgment seat, before; it is not at the events of the Coming, which belong to Israel and the nations. Each passage carries a tag:</p></div>
<div class="legend"><span><span class="tag t-S">Stated</span> the verse says it</span><span><span class="tag t-C">Shown by the context</span> the surrounding passage shows it</span><span><span class="tag t-I">Inferred</span> the map’s own reading, joining passages</span></div>
<div class="actions"><a class="btn" href="#map">Open the Map</a><button class="btn alt" onclick="window.print()">Print the Whole Map</button></div></div>
<section id="map"><div class="wrap"><h2 class="section-title">The Map</h2><p class="section-sub">Top to bottom is the order. Two grey stations stand outside the nine events of the Coming.</p><div class="filter" id="filter"></div><div class="route" id="route"></div><div class="detail" id="detail" hidden aria-live="polite"></div></div></section>
<section id="matrix-sec"><div class="wrap"><h2 class="section-title">Who Is Where</h2><p class="section-sub">Every participant at every station. Tap a station number to open it, or a name to follow that participant on the map.</p><div class="tw" id="matrix"></div></div></section>
<section id="judgments"><div class="wrap"><h2 class="section-title">The Judgments at a Glance</h2><p class="section-sub">Five separate courts, each with its own seat, people and ground.</p><div class="tw" id="glance"></div></div></section>
<section id="limits"><div class="wrap"><h2 class="section-title">What the Map Does Not Claim</h2><p class="section-sub">Where Scripture gives no order, no length or no identification, the map says so instead of filling it in.</p><div class="nc"><ul id="nc"></ul></div></div></section>
<div class="wrap" id="printall"></div></main>
<div class="footer"><strong>Zay-Marie Press</strong> · A free resource · Scripture quotations are from the King James Version (KJV). · <a href="resources.html">Back to Resources</a></div>
<script>{JS}</script></body></html>"""
open('second-coming-map.html','w',encoding='utf-8').write(HTML)
print(len(HTML))
