(() => {
  const search = document.getElementById('parable-search');
  const theme = document.getElementById('parable-theme');
  const count = document.getElementById('parable-count');
  const empty = document.getElementById('parable-empty');
  const reset = document.getElementById('parable-reset');
  const suggestions = document.getElementById('parable-suggestions');
  const browse = document.getElementById('browse-parables');
  const sort = document.getElementById('parable-sort');
  const quickFilters = [...document.querySelectorAll('[data-quick-filter]')];
  const sortedSection = document.getElementById('parable-sorted');
  const sortedGrid = sortedSection.querySelector('.para-grid');
  if (!search || !theme || !sort || !count || !empty || !reset || !suggestions || !browse) return;

  const groups = [...document.querySelectorAll('.para-group')];
  const cards = [...document.querySelectorAll('.para-card')].map((card, index) => {
    card.id = `parable-result-${index + 1}`;
    card.tabIndex = -1;
    return {
      card,
      group: card.closest('.para-group').dataset.group,
      title: card.querySelector('h3').textContent.trim(),
      page: card.querySelector('h3 a').getAttribute('href'),
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

  function syncQuickFilters() {
    quickFilters.forEach(button => button.setAttribute('aria-pressed', String(
      button.dataset.quickFilter === 'all' ? !quick && !theme.value : button.dataset.quickFilter === quick
    )));
  }

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
    empty.hidden = shown !== 0;
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
    window.location.assign(item.page);
  }

  function showSuggestions() {
    const query = normalize(search.value);
    if (query.length < 2) { closeSuggestions(); return; }
    choices = cards.filter(item => (!theme.value || item.group === theme.value) &&
      (!quick || (quick === 'paired' ? paired.has(item.index) : item.group === quick)) &&
      item.searchText.includes(query)).slice(0, 6);
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
      meta.textContent = `${item.passage} · ${item.group} · Open study page`;
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
  theme.addEventListener('change', () => { quick = ''; syncQuickFilters(); filter(); closeSuggestions(); });
  sort.addEventListener('change', () => { arrange(); filter(); closeSuggestions(); });
  quickFilters.forEach(button => button.addEventListener('click', () => {
    quick = button.dataset.quickFilter === 'all' || quick === button.dataset.quickFilter ? '' : button.dataset.quickFilter;
    theme.value = '';
    syncQuickFilters();
    filter();
    closeSuggestions();
  }));
  reset.addEventListener('click', () => {
    search.value = '';
    theme.value = '';
    sort.value = 'canonical';
    quick = '';
    syncQuickFilters();
    arrange();
    filter();
    closeSuggestions();
    search.focus();
  });
  document.addEventListener('click', event => {
    if (!search.contains(event.target) && !suggestions.contains(event.target)) closeSuggestions();
  });
  const descriptions = [
    "Trace Jesus’ four soils from hearing to fruitfulness, letting His explanation govern the seed and each response.",
    "Follow sowing, unseen growth, and harvest without turning the crop’s stages into a prophetic timetable.",
    "Compare the mustard seed’s growth and leaven’s spread without assigning hidden meanings to birds or dough.",
    "Follow the enemy’s sowing and delayed harvest using Jesus’ own identification of the field and reapers.",
    "Read the treasure and pearl through their distinct discoveries and decisive responses, without inventing hidden symbols.",
    "Follow the dragnet’s final separation and the trained scribe’s understanding without merging their two images.",
    "See why the son who first refused then obeyed exposes the leaders’ refusal to believe John.",
    "Trace the tenants’ refusal, violence, and rejection of the son as judgment on leaders, without replacing Israel with the Body.",
    "Follow the king’s invitation, rejected messengers, and garment warning without blending Matthew’s feast with Luke’s.",
    "See how excuses exclude the first guests while others enter the ready feast in Luke’s dinner setting.",
    "Read the fig tree’s reprieve beside a generation’s complaints, preserving each passage’s separate occasion.",
    "Hear Jesus answer the fasting question with a bridegroom, cloth, and wineskins without imposing later program labels.",
    "See how Jesus answers grumbling over His welcome of sinners through loss, finding, repentance, and joy.",
    "Follow both sons and their father’s welcome, leaving the elder brother’s final choice where Luke leaves it.",
    "Follow the Samaritan’s concrete mercy as Jesus answers the lawyer’s question, without turning each detail into a symbol.",
    "Follow a forgiven servant’s refusal to forgive as Jesus answers Peter’s question about repeated forgiveness.",
    "Hear Jesus answer Simon through two canceled debts and the woman’s love, keeping this dinner distinct from other anointings.",
    "Contrast two temple prayers and Jesus’ verdict without treating the tax collector’s plea as a formula that earns mercy.",
    "Compare hearing with doing as two houses face collapse, without assigning every storm to a personal hardship.",
    "Follow the rich man’s barns and God’s interruption as Jesus answers an inheritance request, distinguishing wealth from life.",
    "Compare the steward who feeds the household with one who abuses it while awaiting the master’s return.",
    "Trace unequal entrustments and the master’s reckoning without confusing Matthew’s talents with modern abilities or Luke’s minas.",
    "Follow a nobleman’s departure and return, distinguishing his servants’ accounts from the citizens’ rejection of his reign.",
    "Follow the manager’s urgent debt reductions and the master’s limited praise without making dishonesty the lesson.",
    "Trace the rich man’s reversal and appeal to Abraham without making Lazarus a map of the intermediate state.",
    "Compare the midnight friend’s request and the widow’s appeal while keeping their needs and conclusions distinct.",
    "Follow the servant from field to table and hear why completed duty does not put the master in debt.",
    "See Jesus address status-seeking guests and a host’s invitations without treating the lowest seat as a tactic for honor.",
    "Follow an unfinished tower and an outnumbered king as Jesus calls the crowds to count discipleship’s cost.",
    "Hear the first workers’ complaint after equal payment and distinguish the owner’s agreement from his generosity.",
    "Follow the delayed bridegroom and shut door without turning oil or lamps into a timetable for the Body.",
    "Trace the Son of Man’s separation and two judgments, retaining Jesus’ wording about ‘the least of these my brothers.’",
    "Read budding leaves as a sign of nearness without using the fig tree to calculate an exact day.",
    "Compare the thief, doorkeeper, and returning master as calls to readiness without merging their different plots.",
    "Hear Jesus answer how many are saved with the urgent narrow door, not a numerical quota."
  ];
  cards.forEach(item => {
    const tip = `${descriptions[item.index]} ${item.passage} · ${item.group}`;
    const cover = item.card.querySelector('.para-cover-enlarge');
    cover.dataset.tip = tip;
    cover.setAttribute('aria-description', tip);
    const details = document.createElement('details');
    details.className = 'para-card-summary';
    const label = document.createElement('summary');
    label.textContent = 'Study at a glance';
    const description = document.createElement('p');
    description.textContent = descriptions[item.index];
    details.append(label, description);
    item.card.querySelector('.para-passage').after(details);
  });
  syncQuickFilters();
  arrange();
  filter();
})();
