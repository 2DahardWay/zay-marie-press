(function(){
var input=document.getElementById('packet-search-input'),none=document.getElementById('packet-search-none'),cnt=document.getElementById('packet-search-count');
if(!input)return;
input.hidden=false;
var hdr=document.querySelector('header');
function setHdr(){var h=hdr?Math.round(hdr.getBoundingClientRect().height):0;var st=hdr?getComputedStyle(hdr).position:'';document.documentElement.style.setProperty('--packet-hdr',(st==='fixed'||st==='sticky'?h:0)+'px');}
setHdr();window.addEventListener('resize',setHdr);window.addEventListener('load',setHdr);
var cards=[].slice.call(document.querySelectorAll('.packet-hub-card'));
var groups=[].slice.call(document.querySelectorAll('.packet-hub-grid'));
function norm(t){return t.toLowerCase().replace(/[\u2019\u2018']/g,'').replace(/\s+/g,' ').trim();}
var text=cards.map(function(c){return norm(c.textContent);});
function run(){
var q=norm(input.value),shown=0;
cards.forEach(function(c,i){var ok=!q||q.split(' ').every(function(w){return text[i].indexOf(w)>-1;});c.hidden=!ok;if(ok)shown++;});
groups.forEach(function(g){var any=g.querySelector('.packet-hub-card:not([hidden])');g.hidden=!any;var h=g.previousElementSibling;if(h&&h.classList.contains('packet-section'))h.hidden=!any;});
[].forEach.call(document.querySelectorAll('.packet-testament'),function(h){var n=h.nextElementSibling,any=false;while(n&&!n.classList.contains('packet-testament')){if(n.querySelector&&n.querySelector('.packet-hub-card:not([hidden])'))any=true;n=n.nextElementSibling;}h.hidden=!any;});
none.hidden=shown>0;
if(cnt){cnt.hidden=!q||shown===0;cnt.textContent='Showing '+shown+' of '+cards.length+' packets';}
}
input.addEventListener('input',run);
})();
