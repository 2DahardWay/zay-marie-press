(() => {
  // Parable Studies cart: collects studies on this page and opens one Payhip checkout.
  const IDS = {
 "parable-01-the-growing-seed.html": "Sc2sh",
 "parable-02-the-mustard-seed-and-the-leaven.html": "iwRvQ",
 "parable-03-the-wheat-and-the-weeds.html": "68jey",
 "parable-04-the-hidden-treasure-and-the-pearl.html": "1MARs",
 "parable-05-the-dragnet-and-the-instructed-scribe.html": "bLsKj",
 "parable-06-the-two-sons.html": "WSvPx",
 "parable-07-the-wicked-tenants.html": "RON5F",
 "parable-08-the-wedding-banquet.html": "BiSD2",
 "parable-09-the-great-banquet.html": "Nt0sP",
 "parable-10-the-barren-fig-tree-and-the-generation-s-response.html": "92ekH",
 "parable-11-the-new-cloth-and-new-wineskins.html": "5L98k",
 "parable-12-the-lost-sheep-and-the-lost-coin.html": "YO3Ur",
 "parable-13-the-lost-son-and-the-elder-brother.html": "y1IC5",
 "parable-14-the-good-samaritan.html": "jScV5",
 "parable-15-the-unforgiving-servant.html": "NkKi1",
 "parable-16-the-two-debtors.html": "wJVrv",
 "parable-17-the-pharisee-and-the-tax-collector.html": "jn9b4",
 "parable-18-the-wise-and-foolish-builders.html": "yG362",
 "parable-19-the-rich-fool.html": "oBp8b",
 "parable-20-the-faithful-and-unfaithful-servant.html": "0GXHq",
 "parable-21-the-talents.html": "FLasd",
 "parable-22-the-minas.html": "ByKI9",
 "parable-23-the-shrewd-manager.html": "CxGfh",
 "parable-24-the-rich-man-and-lazarus.html": "4VL3r",
 "parable-25-the-friend-and-the-persistent-widow.html": "o2Kni",
 "parable-26-the-unprofitable-servants.html": "T3Mhw",
 "parable-27-the-lowest-seat-and-banquet-invitation.html": "cxPRX",
 "parable-28-the-tower-and-the-warring-king.html": "KeohQ",
 "parable-29-the-laborers-in-the-vineyard.html": "2C3Qh",
 "parable-30-the-ten-virgins.html": "sEDgP",
 "parable-31-the-sheep-and-the-goats.html": "ErZcT",
 "parable-32-the-fig-tree-lesson.html": "B3C7N",
 "parable-33-the-thief-and-watchful-servants.html": "O3XaM",
 "parable-34-the-narrow-door.html": "9uadb",
 "parable-sower.html": "Ud2Fl"
};
  const PRICE = 3.99;
  const BASE = 'https://shop.zaymariepress.com/buy?s=1';
  const KEY = 'zmp-parable-cart';
  let mem = [];
  const load = () => { try { const v = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(v) ? v.filter(f => IDS[f]) : []; } catch (e) { return mem; } };
  const save = list => { mem = list; try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) {} };
  let cart = load();

  const bar = document.createElement('div');
  bar.className = 'para-cart-bar';
  bar.setAttribute('role', 'region');
  bar.setAttribute('aria-label', 'Your cart');
  bar.hidden = true;
  bar.innerHTML = '<span class="para-cart-summary" aria-live="polite"></span><a class="para-cart-checkout" target="_blank" rel="noopener">Checkout</a><button type="button" class="para-cart-clear">Clear</button>';
  document.body.appendChild(bar);
  const summary = bar.querySelector('.para-cart-summary');
  const checkout = bar.querySelector('.para-cart-checkout');

  const hrefOf = card => { const a = card.querySelector('h3 a'); return a ? a.getAttribute('href') : null; };
  const titleOf = card => { const a = card.querySelector('h3 a'); return a ? a.textContent.trim() : 'this study'; };

  function render() {
    document.querySelectorAll('.para-add').forEach(btn => {
      const on = cart.includes(btn.dataset.file);
      btn.textContent = on ? 'Added \u2713 \u00b7 Remove' : 'Add to cart';
      btn.classList.toggle('is-added', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    bar.hidden = cart.length === 0;
    document.body.classList.toggle('has-para-cart', cart.length > 0);
    const total = (cart.length * PRICE).toFixed(2);
    summary.textContent = cart.length + (cart.length === 1 ? ' study' : ' studies') + ' in your cart \u00b7 $' + total;
    checkout.href = BASE + cart.map(f => '&cart_links%5B%5D=' + IDS[f] + '&qty%5B' + IDS[f] + '%5D=1').join('');
  }

  document.querySelectorAll('.para-card').forEach(card => {
    const file = hrefOf(card);
    if (!file || !IDS[file]) return;
    const meta = card.querySelector('.para-meta');
    if (!meta) return;
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'para-add';
    btn.dataset.file = file;
    btn.setAttribute('aria-label', 'Add ' + titleOf(card) + ' to cart');
    meta.appendChild(btn);
  });

  document.addEventListener('click', e => {
    const btn = e.target.closest('.para-add');
    if (btn) {
      const f = btn.dataset.file;
      cart = cart.includes(f) ? cart.filter(x => x !== f) : cart.concat(f);
      save(cart); render(); return;
    }
    if (e.target.closest('.para-cart-clear')) { cart = []; save(cart); render(); }
  });
  render();
})();
