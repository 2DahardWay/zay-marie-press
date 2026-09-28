(() => {
  const search = document.getElementById('parable-search');
  const theme = document.getElementById('parable-theme');
  const count = document.getElementById('parable-count');
  const suggestions = document.getElementById('parable-suggestions');
  const browse = document.getElementById('browse-parables');
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
      searchText: card.dataset.search.toLowerCase().replace(/\s+/g, ' ').trim()
    };
  });
  const normalize = value => value.toLowerCase().replace(/\s+/g, ' ').trim();
  let choices = [];
  let active = -1;

  function filter() {
    const query = normalize(search.value);
    const selectedTheme = theme.value;
    browse.classList.toggle('search-active', !!query || !!selectedTheme);
    let shown = 0;
    for (const group of groups) {
      let inGroup = 0;
      for (const card of group.querySelectorAll('.para-card')) {
        const item = cards.find(entry => entry.card === card);
        const visible = (!selectedTheme || item.group === selectedTheme) && (!query || item.searchText.includes(query));
        card.hidden = !visible;
        if (visible) { inGroup++; shown++; }
      }
      group.hidden = !inGroup;
    }
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
  theme.addEventListener('change', () => { filter(); closeSuggestions(); });
  document.addEventListener('click', event => {
    if (!search.contains(event.target) && !suggestions.contains(event.target)) closeSuggestions();
  });
  filter();
})();
