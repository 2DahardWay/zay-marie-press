(function(){
var D=__DATA__,PR=D.proj,G=D.geo,ST=D.stops,PH={},cur=null,view='whole',hidden={},marks={},NS='http://www.w3.org/2000/svg';
D.ph.forEach(function(p){PH[p.id]=p});
var LOC={S:['Named','Place named in the text'],C:['Shown by the context','Region named; the marker is a placement'],I:['Inferred','Site uncertain; the marker is a placement']};
var MK={feast:['Feasts','#f1c84b'],gentile:['Gentile and Samaritan contacts','#4fd08a'],sign:['Signs','#7fd6ff'],teach:['Teaching','#c79bff'],israel:['To Israel','#ff9d6b']};
function e(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function X(lon){return (lon-PR.lon0)*PR.K*PR.C}function Y(lat){return (PR.lat1-lat)*PR.K}
function vb(la0,la1,lo0,lo1){return [X(lo0),Y(la1),X(lo1)-X(lo0),Y(la0)-Y(la1)]}
var VIEWS={whole:['The whole land',vb(31.58,33.42,34.95,36.05)],galilee:['Galilee',vb(32.59,32.98,35.17,35.74)],judaea:['Judaea',vb(31.62,32.05,35.02,35.64)],jerusalem:['Jerusalem and Bethany',vb(31.750,31.800,35.205,35.285)]};
var VORDER=['jerusalem','galilee','judaea','whole'];
function inView(v,x,y){var b=VIEWS[v][1];return x>=b[0]&&x<=b[0]+b[2]&&y>=b[1]&&y<=b[1]+b[3]}
// places
var NAMES={bethlehem:'Bethlehem',jordan1:'The Jordan',wilderness:'The Wilderness',cana1:'Cana',capernaum0:'Capernaum',judaea:'Judaea (Aenon)',galilee1:'Galilee circuit',mountain1:'The mountain',gerasenes:'Gadarenes',twelve:'Galilee: the Twelve',bethsaida1:'Bethsaida',gennesaret:'Gennesaret',tyre:'Tyre and Sidon',decapolis:'Decapolis',magdala:'Magdala',caesarea:'Caesarea Philippi',transfig:'High mountain',samaria:'Samaritan village',bethany1:'Bethany',ephraim:'Ephraim',border:'Samaria and Galilee',perea:'Beyond Jordan',jericho:'Jericho',olivet:'Mount of Olives',emmaus:'Emmaus',galilee3:'Sea of Tiberias',nazareth0:'Nazareth',jerusalem12:'Jerusalem',nain:'Nain',sychar:'Sychar'};
var PL={},PLK=[];
ST.forEach(function(s){s.x=X(s.lon);s.y=Y(s.lat);var k=s.lat+','+s.lon;if(!PL[k]){var nm=NAMES[s.id]||s.label.split(/[:,]/)[0];PL[k]={k:k,x:s.x,y:s.y,name:nm,stops:[]};PLK.push(k)}PL[k].stops.push(s);s.pk=k});
var MAJOR={'Bethlehem':1,'Nazareth':1,'Jerusalem':1,'Capernaum':1,'Tyre and Sidon':1,'Caesarea Philippi':1,'Jericho':1,'Sychar':1};
function kjv(vs){var h='',c=null;vs.forEach(function(v){if(c!==null&&v.c!==c)h+='<span class="chp">Chapter '+v.c+'</span>';c=v.c;h+='<sup>'+v.v+'</sup>'+e(v.t)+' '});return '<div class="kjv">'+h+'</div>'}
function pass(p,open){return '<details class="pass"'+(open?' open':'')+'><summary><span class="ref">'+e(p.ref)+'</span></summary>'+kjv(p.vs)+'</details>'}
function visit(s,open){
 var p=PH[s.ph],h='<details class="visit"'+(open?' open':'')+' id="v-'+s.id+'"><summary><span class="pill" style="background:'+p.color+'">'+e(p.name)+'</span><span class="tag t-'+s.loc+'" title="'+e(LOC[s.loc][1])+'">'+LOC[s.loc][0]+'</span><div class="vt">'+s.n+'. '+e(s.label)+'</div></summary><div class="vb">';
 var tg=s.tags.map(function(t){return '<span>'+e(MK[t][0])+'</span>'}).join('');if(tg)h+='<div class="mk-tags">'+tg+'</div>';
 h+='<p>'+e(s.happens)+'</p><h4>The passages</h4>';
 s.passages.forEach(function(q){h+=pass(q,open&&s.passages.length===1)});
 if(s.id==='jerusalem7'){h+='<h4>The week, day by day</h4><div class="week">';D.week.forEach(function(w){h+='<details class="visit"><summary><div class="vt">'+e(w.title)+'</div><span class="sub" style="color:#8f9bad;font-size:13px">'+e(w.day)+'</span></summary><div class="vb"><p>'+e(w.happens)+'</p>';w.passages.forEach(function(q){h+=pass(q,false)});h+='</div></details>'});h+='</div><h4>What Scripture does not say about the week</h4><ul class="silent">';D.weekSilent.forEach(function(t){h+='<li>'+e(t)+'</li>'});h+='</ul>'}
 if(s.silent.length){h+='<h4>What Scripture does not say</h4><ul class="silent">';s.silent.forEach(function(t){h+='<li>'+e(t)+'</li>'});h+='</ul>'}
 if(s.id==='olivet2'||s.id==='jerusalem7')h+='<h4>Go deeper</h4><p><a href="second-coming-map.html">The Second Coming Map</a> follows the coming of the King that the two men and the Olivet discourse describe.</p>';
 return h+'</div></details>'}
function panel(){
 var el=document.getElementById('panel');
 if(!cur){el.innerHTML='<h3>Start Anywhere</h3><p class="sub">Forty-eight stops, eight phases.</p><p>Tap a marker on the map, or choose a stop from the list below it. Each stop shows what happens there, the passage in the KJV, and what Scripture does not say about it.</p><p>The Gospels do not agree on one strict order. The map follows Matthew and Mark for Galilee and John for the feasts, and says so where it matters.</p><p><button class="btn" data-go="bethlehem">Begin at Bethlehem</button> <button class="btn alt" data-go="capernaum1">Go to Capernaum</button> <button class="btn alt" data-go="jerusalem7">Go to the last week</button></p>';return}
 var pl=PL[cur.pk],i=cur.n-1,h='<h3>'+e(pl.name)+'</h3><p class="sub">'+(pl.stops.length>1?pl.stops.length+' stops here; the one you chose is open.':'Stop '+cur.n+' of '+ST.length)+'</p>';
 pl.stops.forEach(function(s){h+=visit(s,s===cur)});
 h+='<div class="nav2"><button class="btn alt" data-nav="-1"'+(i<1?' disabled':'')+'>← Previous stop</button><button class="btn alt" data-nav="1"'+(i>=ST.length-1?' disabled':'')+'>Next stop →</button></div>';
 el.innerHTML=h}
function svgEl(n,a,t){var x=document.createElementNS(NS,n);for(var k in a)x.setAttribute(k,a[k]);if(t!=null)x.textContent=t;return x}
function visible(s){return !hidden[s.ph]}
function anyMark(){for(var k in marks)if(marks[k])return true;return false}
function foc(c){return !cur||cur.ph===c.ph}
var placed;
var VB;
function free(r){if(r[0]<VB[0]+2||r[2]>VB[0]+VB[2]-2||r[1]<VB[1]||r[3]>VB[1]+VB[3])return false;for(var i=0;i<placed.length;i++){var q=placed[i];if(r[0]<q[2]&&r[2]>q[0]&&r[1]<q[3]&&r[3]>q[1])return false}return true}
function draw(){placed=[];VB=VIEWS[view][1];
 var svg=document.getElementById('svg'),b=VIEWS[view][1];svg.setAttribute('viewBox',b.join(' '));
 var cw=svg.clientWidth||440,s=b[2]/cw;svg.innerHTML='';
 var X0=0,Y0=0,Wd=PR.W,Ht=PR.H;
 svg.appendChild(svgEl('rect',{x:X0,y:Y0,width:Wd,height:Ht,fill:'#0e2a4a'}));
 svg.appendChild(svgEl('path',{d:G.land,fill:'#22395a','fill-rule':'evenodd',stroke:'#3a5780','stroke-width':1.2*s}));
 svg.appendChild(svgEl('path',{d:G.galilee,fill:'#0e2a4a',stroke:'#3a5780','stroke-width':1*s}));
 svg.appendChild(svgEl('path',{d:G.dead,fill:'#0e2a4a',stroke:'#3a5780','stroke-width':1*s}));
 svg.appendChild(svgEl('path',{d:G.jordan,fill:'none',stroke:'#4a78b0','stroke-width':1.6*s,'stroke-linecap':'round'}));
 function lab(t,lon,lat,o){var el=svgEl('text',{x:X(lon),y:Y(lat),'font-size':(o.f||11)*s,fill:o.c||'#6f8db5','font-style':'italic','text-anchor':o.a||'middle','font-family':'Georgia,serif'},t);svg.appendChild(el)}
 var big=view==='whole';
 lab('Mediterranean Sea',34.97,32.30,{a:'start',f:12});
 lab('Sea of Galilee',35.585,32.80,{f:big?9:11,c:'#8fb2dd'});lab('Dead Sea',35.48,31.52+0.14,{f:big?10:11,c:'#8fb2dd'});
 if(view!=='jerusalem'){lab('Jordan',35.56,32.40,{f:10});
  if(view==='whole'||view==='judaea'){lab('JUDAEA',35.00,31.90,{f:11,c:'#7f9cc4',a:'start'})}
  if(view==='whole'||view==='judaea'){lab('SAMARIA',35.10,32.28,{f:11,c:'#7f9cc4',a:'start'})}
  if(view==='whole'||view==='galilee'){lab('GALILEE',35.22,32.86,{f:11,c:'#7f9cc4',a:'start'})}
  if(view==='whole'){lab('Decapolis',35.83,32.62,{f:11,c:'#7f9cc4'});lab('Perea',35.80,31.95,{f:11,c:'#7f9cc4'})}}
 // legs
 var seen={},legs=[];
 for(var i=1;i<ST.length;i++){var a=ST[i-1],c=ST[i];if(a.pk===c.pk||hidden[c.ph])continue;var pk=[a.pk,c.pk].sort().join('|');seen[pk]=(seen[pk]||0);var k=seen[pk]++;legs.push([a,c,k])}
 legs.forEach(function(l){var a=l[0],c=l[1],k=l[2],dx=c.x-a.x,dy=c.y-a.y,L=Math.sqrt(dx*dx+dy*dy);if(L<0.5)return;
  var off=(k===0?0:(k%2?1:-1)*Math.ceil(k/2)*4.5*s),nx=-dy/L*off,ny=dx/L*off,mx=(a.x+c.x)/2+nx,my=(a.y+c.y)/2+ny;
  var col=PH[c.ph].color,dash=(a.loc!=='S'||c.loc!=='S')?(5*s)+' '+(4*s):'';
  var d='M'+a.x+','+a.y+' Q'+mx+','+my+' '+c.x+','+c.y;
  var pth=svgEl('path',{d:d,fill:'none',stroke:col,'stroke-width':(foc(c)?3*s:1.7*s),opacity:(foc(c)?.95:.5),'stroke-linecap':'round'});if(dash)pth.setAttribute('stroke-dasharray',dash);svg.appendChild(pth);
  if(L>34*s){var t=.5,bx=(1-t)*(1-t)*a.x+2*(1-t)*t*mx+t*t*c.x,by=(1-t)*(1-t)*a.y+2*(1-t)*t*my+t*t*c.y,tx=2*(1-t)*(mx-a.x)+2*t*(c.x-mx),ty=2*(1-t)*(my-a.y)+2*t*(c.y-my),tl=Math.sqrt(tx*tx+ty*ty)||1;tx/=tl;ty/=tl;var z=5*s;
   svg.appendChild(svgEl('path',{d:'M'+(bx+tx*z)+','+(by+ty*z)+' L'+(bx-tx*z-ty*z*.8)+','+(by-ty*z+tx*z*.8)+' L'+(bx-tx*z+ty*z*.8)+','+(by-ty*z-tx*z*.8)+'Z',fill:col}))}});
 // markers
 var am=anyMark(),gs=[];
 PLK.forEach(function(k){var pl=PL[k],vs=pl.stops.filter(visible);if(!vs.length)return;
  if(!inView(view,pl.x,pl.y))return;
  var first=vs[0],on=!am||vs.some(function(s){return s.tags.some(function(t){return marks[t]})});
  var g=svgEl('g',{class:'mk',tabindex:0,role:'button','aria-label':pl.name+', stop'+(vs.length>1?'s ':' ')+vs.map(function(s){return s.n}).join(', '),'data-pk':k,opacity:on?1:.3});
  var sel=cur&&cur.pk===k;
  if(sel)g.appendChild(svgEl('circle',{cx:pl.x,cy:pl.y,r:17*s,fill:'none',stroke:'#fff','stroke-width':2.2*s}));
  g.appendChild(svgEl('circle',{class:'body',cx:pl.x,cy:pl.y,r:11*s,fill:PH[first.ph].color,stroke:'#0b1628','stroke-width':2*s}));
  g.appendChild(svgEl('text',{x:pl.x,y:pl.y+4*s,'text-anchor':'middle','font-size':(first.n>9?11:12)*s,'font-weight':700,fill:'#0b1628','font-family':'Arial,sans-serif'},first.n));
  if(vs.length>1){g.appendChild(svgEl('circle',{cx:pl.x+10*s,cy:pl.y-10*s,r:6.5*s,fill:'#0b1628',stroke:'#d4af37','stroke-width':1.2*s}));g.appendChild(svgEl('text',{x:pl.x+10*s,y:pl.y-7.4*s,'text-anchor':'middle','font-size':8.5*s,'font-weight':700,fill:'#d4af37','font-family':'Arial,sans-serif'},'×'+vs.length))}
  var ti=0;for(var m in MK){if(marks[m]&&vs.some(function(s){return s.tags.indexOf(m)>=0})){g.appendChild(svgEl('circle',{cx:pl.x-12*s+ti*8*s,cy:pl.y+14*s,r:3.6*s,fill:MK[m][1],stroke:'#0b1628','stroke-width':.8*s}));ti++}}
  g.appendChild(svgEl('title',{},pl.name));
  g._lab=(view!=='whole'||MAJOR[pl.name]||sel)?pl.name:null;g._pl=pl;g._sel=sel;
  svg.appendChild(g);gs.push(g)});
 labels(svg,gs,s)}
function labels(svg,gs,s){
 gs.forEach(function(g){var p=g._pl;placed.push([p.x-14*s,p.y-14*s,p.x+14*s,p.y+14*s])});
 gs.sort(function(a,b){return (b._sel?1:0)-(a._sel?1:0)});
 gs.forEach(function(g){if(!g._lab)return;var p=g._pl,fs=12.5*s,w=g._lab.length*fs*.6+4*s,h=fs*1.2,pos=[[p.x+15*s,'start'],[p.x-15*s-w,'start']],ok=false;
  for(var i=0;i<pos.length;i++){var r=[pos[i][0],p.y-h/2,pos[i][0]+w,p.y+h/2];if(free(r)){placed.push(r);var t=svgEl('text',{x:pos[i][0],y:p.y+4*s,'font-size':fs,'font-weight':700,fill:'#f7f7f2','font-family':'Arial,sans-serif','paint-order':'stroke',stroke:'#0b1628','stroke-width':3.4*s,'stroke-linejoin':'round','pointer-events':'none'},g._lab);g.appendChild(t);ok=true;break}}
 });}
function chips(){
 var h='<span class="lab">Phases of the ministry (tap to hide or show)</span>';D.ph.forEach(function(p){h+='<button class="chip" data-ph="'+p.id+'" aria-pressed="'+!hidden[p.id]+'"><i style="background:'+p.color+'"></i>'+e(p.name)+'</button>'});h+='<button class="chip" data-all="1">Show all</button><button class="chip" data-all="0">Hide all</button>';document.getElementById('phases').innerHTML=h;
 h='<span class="lab">Mark on the map</span>';for(var m in MK)h+='<button class="chip" data-mk="'+m+'" aria-pressed="'+!!marks[m]+'"><i style="background:'+MK[m][1]+'"></i>'+e(MK[m][0])+'</button>';document.getElementById('marks').innerHTML=h;
 h='';for(var v in VIEWS)h+='<button class="chip" data-view="'+v+'" aria-pressed="'+(v===view)+'">'+e(VIEWS[v][0])+'</button>';document.getElementById('views').innerHTML=h}
function seq(){var h='',last='';ST.forEach(function(s){if(s.ph!==last){last=s.ph;var p=PH[s.ph];h+='<div class="seqph">'+e(p.name)+'<small>'+e(p.sub)+'</small></div><ul class="seq">'}
 h+='<li><button style="--c:'+PH[s.ph].color+'" data-go="'+s.id+'" aria-pressed="'+(cur===s)+'"><span class="n">'+s.n+'</span><span>'+e(s.label)+'</span><span class="q">'+LOC[s.loc][0]+'</span></button></li>';
 var nx=ST[s.n];if(!nx||nx.ph!==s.ph)h+='</ul>'});document.getElementById('seq').innerHTML=h}
function setView(v){view=v;chips();draw()}
function select(id,scroll){var s=null;ST.forEach(function(x){if(x.id===id)s=x});if(!s)return;cur=s;
 if(hidden[s.ph]){hidden[s.ph]=false;chips()}
 var pl=PL[s.pk];if(!inView(view,pl.x,pl.y)){for(var i=0;i<VORDER.length;i++)if(inView(VORDER[i],pl.x,pl.y)){view=VORDER[i];break}chips()}
 draw();panel();seq();try{history.replaceState(null,'','#'+id)}catch(x){}
 var p=document.getElementById('panel');if(scroll==='map')document.getElementById('map').scrollIntoView();else if(scroll&&window.innerWidth<=900){p.scrollIntoView({block:'start'})}}
function init(){
 chips();seq();panel();draw();
 var nc='';D.glob.forEach(function(t){nc+='<li>'+e(t)+'</li>'});document.getElementById('nc').innerHTML=nc;
 var pa='';ST.forEach(function(s){pa+=visit(s,true)});document.getElementById('printall').innerHTML=pa;
 document.addEventListener('click',function(ev){
  var t=ev.target.closest('[data-all],[data-pk],[data-ph],[data-mk],[data-view],[data-go],[data-nav]');if(!t)return;
  if(t.dataset.all!==undefined){D.ph.forEach(function(p){hidden[p.id]=t.dataset.all==='0'});chips();draw();return}
  if(t.dataset.pk){var pl=PL[t.dataset.pk],vs=pl.stops.filter(visible);var pick=(cur&&cur.pk===pl.k)?cur:vs[0];select(pick.id,true);return}
  if(t.dataset.go){select(t.dataset.go,'map');return}
  if(t.dataset.nav){var i=cur.n-1+parseInt(t.dataset.nav,10);if(i>=0&&i<ST.length)select(ST[i].id,true);return}
  if(t.dataset.ph){hidden[t.dataset.ph]=!hidden[t.dataset.ph];chips();draw();return}
  if(t.dataset.mk){marks[t.dataset.mk]=!marks[t.dataset.mk];chips();draw();return}
  if(t.dataset.view){setView(t.dataset.view)}});
 document.addEventListener('keydown',function(ev){if((ev.key==='Enter'||ev.key===' ')&&ev.target.classList&&ev.target.classList.contains('mk')){ev.preventDefault();ev.target.dispatchEvent(new MouseEvent('click',{bubbles:true}))}});
 var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(draw,150)});
 var h=(location.hash||'').replace('#','');ST.forEach(function(s){if(s.id===h)select(h,false)})}
init()})();
