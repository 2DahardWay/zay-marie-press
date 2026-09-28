(() => {
  const search = document.getElementById('parable-search');
  const theme = document.getElementById('parable-theme');
  const count = document.getElementById('parable-count');
  const suggestions = document.getElementById('parable-suggestions');
  const browse = document.getElementById('browse-parables');
  const sort = document.getElementById('parable-sort');
  const quickFilters = [...document.querySelectorAll('[data-quick-filter]')];
  const sortedSection = document.getElementById('parable-sorted');
  const sortedGrid = sortedSection.querySelector('.para-grid');
  if (!search || !theme || !count || !suggestions || !browse) return;

  const groups = [...document.querySelectorAll('.para-group')];
  const cards = [...document.querySelectorAll('.para-card')].map((card, index) => {
    card.id = `parable-result-${index + 1}`;
    card.tabIndex = -1;
    return {
      card,
      group: card.closest('.para-group').dataset.group,
      title: card.querySelector('h3').textContent.trim(),
      passage: card.querySelector('.para-passage').textContent.trim(),
      index,
      pages: Number.parseInt(card.querySelector('.para-pages').textContent, 10),
      price: Number.parseFloat(card.querySelector('.para-card-price').textContent.slice(1)),
      home: card.parentElement,
      searchText: card.dataset.search.toLowerCase().replace(/\s+/g, ' ').trim()
    };
  });
  const normalize = value => value.toLowerCase().replace(/\s+/g, ' ').trim();
  let choices = [];
  let active = -1;
  let quick = '';
  const paired = new Set([2, 4, 5, 10, 12, 25, 27, 28]);

  function arrange() {
    if (sort.value === 'canonical') {
      cards.forEach(item => item.home.append(item.card));
      sortedSection.hidden = true;
      groups.forEach(group => group.hidden = false);
      return;
    }
    const order = [...cards];
    if (sort.value === 'theme') order.sort((a, b) => a.group.localeCompare(b.group) || a.index - b.index);
    if (sort.value === 'length') order.sort((a, b) => a.pages - b.pages || a.index - b.index);
    if (sort.value === 'price') order.sort((a, b) => a.price - b.price || a.index - b.index);
    if (sort.value === 'newest') order.reverse();
    order.forEach(item => sortedGrid.append(item.card));
    groups.forEach(group => group.hidden = true);
    sortedSection.hidden = false;
  }

  function filter() {
    const query = normalize(search.value);
    const selectedTheme = theme.value;
    browse.classList.toggle('search-active', !!query || !!selectedTheme || !!quick);
    let shown = 0;
    for (const item of cards) {
      const visible = (!selectedTheme || item.group === selectedTheme) &&
        (!quick || (quick === 'paired' ? paired.has(item.index) : item.group === quick)) &&
        (!query || item.searchText.includes(query));
      item.card.hidden = !visible;
      if (visible) shown++;
    }
    if (sort.value === 'canonical') groups.forEach(group => {
      group.hidden = ![...group.querySelectorAll('.para-card')].some(card => !card.hidden);
    });
    else sortedSection.hidden = shown === 0;
    count.textContent = `${shown} edition${shown === 1 ? '' : 's'} shown`;
    return shown;
  }

  function closeSuggestions() {
    suggestions.hidden = true;
    suggestions.replaceChildren();
    choices = [];
    active = -1;
    search.setAttribute('aria-expanded', 'false');
    search.removeAttribute('aria-activedescendant');
  }

  function setActive(index) {
    active = index;
    [...suggestions.children].forEach((option, i) => {
      option.setAttribute('aria-selected', String(i === index));
      option.classList.toggle('active', i === index);
    });
    if (index >= 0) {
      search.setAttribute('aria-activedescendant', `parable-suggestion-${index}`);
      suggestions.children[index].scrollIntoView({block: 'nearest'});
    } else search.removeAttribute('aria-activedescendant');
  }

  function choose(item) {
    search.value = item.title;
    filter();
    closeSuggestions();
    item.card.scrollIntoView({behavior: 'smooth', block: 'center'});
    item.card.focus({preventScroll: true});
  }

  function showSuggestions() {
    const query = normalize(search.value);
    if (query.length < 2) { closeSuggestions(); return; }
    choices = cards.filter(item => (!theme.value || item.group === theme.value) && item.searchText.includes(query)).slice(0, 6);
    if (!choices.length) { closeSuggestions(); return; }
    suggestions.replaceChildren();
    choices.forEach((item, index) => {
      const option = document.createElement('li');
      option.id = `parable-suggestion-${index}`;
      option.setAttribute('role', 'option');
      option.setAttribute('aria-selected', 'false');
      const title = document.createElement('strong');
      title.textContent = item.title;
      const meta = document.createElement('span');
      meta.textContent = `${item.passage} · ${item.group}`;
      option.append(title, meta);
      option.addEventListener('mousedown', event => event.preventDefault());
      option.addEventListener('click', () => choose(item));
      suggestions.append(option);
    });
    active = -1;
    suggestions.hidden = false;
    search.setAttribute('aria-expanded', 'true');
    search.removeAttribute('aria-activedescendant');
  }

  search.addEventListener('input', () => { filter(); showSuggestions(); });
  search.addEventListener('focus', showSuggestions);
  search.addEventListener('keydown', event => {
    if (event.key === 'Escape') { closeSuggestions(); return; }
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      if (suggestions.hidden) showSuggestions();
      if (!choices.length) return;
      event.preventDefault();
      setActive((active + (event.key === 'ArrowDown' ? 1 : -1) + choices.length) % choices.length);
    }
    if (event.key === 'Enter') {
      if (active >= 0 && choices[active]) { event.preventDefault(); choose(choices[active]); }
      else {
        const visible = cards.filter(item => !item.card.hidden);
        if (visible.length === 1) { event.preventDefault(); choose(visible[0]); }
      }
    }
  });
  theme.addEventListener('change', () => { quick = ''; quickFilters.forEach(button => button.setAttribute('aria-pressed', 'false')); filter(); closeSuggestions(); });
  sort.addEventListener('change', () => { arrange(); filter(); closeSuggestions(); });
  quickFilters.forEach(button => button.addEventListener('click', () => {
    quick = quick === button.dataset.quickFilter ? '' : button.dataset.quickFilter;
    quickFilters.forEach(candidate => candidate.setAttribute('aria-pressed', String(candidate.dataset.quickFilter === quick)));
    theme.value = '';
    filter();
    closeSuggestions();
  }));
  document.addEventListener('click', event => {
    if (!search.contains(event.target) && !suggestions.contains(event.target)) closeSuggestions();
  });
  const descriptions = {
    "Kingdom reception": "Explore the reception and growth of the Kingdom message.",
    "Israel’s response": "Read Jesus’ response to Israel’s hearers in its Gospel setting.",
    "Mercy and repentance": "Examine mercy and repentance in Jesus’ original encounter.",
    "Discipleship and stewardship": "Trace responsibility and stewardship in the parable’s own setting.",
    "Readiness and judgment": "Follow Jesus’ warning and its stated horizon of judgment."
  };
  cards.forEach(item => {
    item.card.querySelector('.para-cover-enlarge').dataset.tip = `${descriptions[item.group]} ${item.passage} · ${item.group}`;
  });
  arrange();
  filter();
})();
