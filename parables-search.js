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

  const aliases = {
    "parable-sower.html": "parable of the sower; sower; four soils; seed and the soils; wayside; stony ground; good ground; seed sown",
    "parable-01-the-growing-seed.html": "seed growing secretly; seed growing by itself; seed growing in secret; earth bears fruit of itself; blade then the ear; the farmer and the seed; patient farmer",
    "parable-02-the-mustard-seed-and-the-leaven.html": "grain of mustard seed; mustard seed; mustard tree; leaven; yeast; woman and the leaven; woman hid leaven in three measures of meal; birds in the branches",
    "parable-03-the-wheat-and-the-weeds.html": "wheat and the tares; tares; weeds; the tares of the field; enemy sowed; darnel; wheat and darnel; good seed and weeds",
    "parable-04-the-hidden-treasure-and-the-pearl.html": "treasure hidden in a field; hidden treasure; pearl of great price; pearl of great value; costly pearl; merchant seeking pearls",
    "parable-05-the-dragnet-and-the-instructed-scribe.html": "drag net; fishing net; net cast into the sea; good and bad fish; householder; scribe instructed unto the kingdom; things new and old; old and new treasures",
    "parable-06-the-two-sons.html": "two sons in the vineyard; father and two sons; work in the vineyard today; son who said no then went; son who said I go sir",
    "parable-07-the-wicked-tenants.html": "absent landlord; the landlord; wicked husbandmen; wicked vinedressers; vineyard tenants; tenant farmers; the vineyard owner; householder who planted a vineyard; rejected cornerstone",
    "parable-08-the-wedding-banquet.html": "marriage feast; wedding feast; marriage of the king's son; king's son wedding; wedding garment; many are called few are chosen; marriage supper",
    "parable-09-the-great-banquet.html": "great supper; the great feast; great dinner; man who made a great supper; the invited guests; excuses; invitation to the feast",
    "parable-10-the-barren-fig-tree-and-the-generation-s-response.html": "barren fig tree; unfruitful fig tree; fig tree in the vineyard; fig tree and the vinedresser; children in the marketplace; piping and dancing; we piped unto you; sit another year; marketplace",
    "parable-11-the-new-cloth-and-new-wineskins.html": "new wine in old bottles; new wine in old wineskins; new wine and old wineskins; old garment; patch; new patch on old cloth; unshrunk cloth; wineskins; bottles; fasting question; bridegroom's friends",
    "parable-12-the-lost-sheep-and-the-lost-coin.html": "ten pieces of silver; ten silver coins; lost piece of silver; lost silver; lost drachma; woman with ten coins; ninety and nine; ninety-nine sheep; one hundred sheep; the shepherd and the sheep; lost and found; the lost sheep; the lost coin",
    "parable-13-the-lost-son-and-the-elder-brother.html": "prodigal son; the prodigal; lost son; two sons; father and two sons; elder brother; older brother; the loving father; the waiting father; pigs; the fatted calf; younger son; far country",
    "parable-14-the-good-samaritan.html": "samaritan; the samaritan; man who fell among thieves; man who fell among robbers; who is my neighbour; who is my neighbor; priest and levite; jericho road",
    "parable-15-the-unforgiving-servant.html": "unmerciful servant; merciless servant; wicked servant; unforgiving debtor; ten thousand talents; hundred pence; hundred denarii; forgive seventy times seven; the king and his servants; settling accounts",
    "parable-16-the-two-debtors.html": "creditor and two debtors; the creditor; two debtors; moneylender; money lender; five hundred pence; fifty pence; five hundred denarii; forgiven much loves much; simon the pharisee; the sinful woman",
    "parable-17-the-pharisee-and-the-tax-collector.html": "pharisee and the publican; the publican; publican and the pharisee; pharisee and publican; pharisee and the tax gatherer; tax gatherer; two men went up to the temple to pray; god be merciful to me a sinner; two men who prayed",
    "parable-18-the-wise-and-foolish-builders.html": "two builders; wise and foolish builder; wise man and foolish man; house on the rock; house on the sand; house built on a rock; house built on sand; wise builder; foolish builder; two houses; hearers and doers",
    "parable-19-the-rich-fool.html": "rich farmer; foolish rich man; the rich man and his barns; rich man and his barns; barns; bigger barns; this night thy soul shall be required; covetousness; the rich landowner",
    "parable-20-the-faithful-and-unfaithful-servant.html": "faithful and wise servant; faithful and wise steward; wise steward; faithful steward; faithful servant; evil servant; unfaithful steward; unfaithful servant; steward and the master; servant left in charge; the faithful manager; the wise and foolish servant; master returns",
    "parable-21-the-talents.html": "parable of the talents; talents; talent; the three servants; ten talents; five talents; two talents; one talent; buried talent; servants and the talents; money entrusted to servants; bags of gold; man traveling to a far country; the master and his servants",
    "parable-22-the-minas.html": "the pounds; pounds; ten pounds; ten minas; mina; pound; nobleman; the nobleman; ten servants; man of noble birth; a certain nobleman; the ten minas; the king and ten servants; i will not have this man to reign over us; bring hither those mine enemies",
    "parable-23-the-shrewd-manager.html": "shrewd steward; unjust steward; unrighteous steward; dishonest steward; dishonest manager; unfaithful steward; crafty steward; clever manager; the rich man's steward; the steward's debtors; unrighteous mammon; make friends by unrighteous mammon; a hundred measures of oil",
    "parable-24-the-rich-man-and-lazarus.html": "lazarus and the rich man; lazarus; dives; beggar lazarus; rich man and the beggar; the rich man in hades; the rich man in hell; abraham's bosom; great gulf fixed; the beggar",
    "parable-25-the-friend-and-the-persistent-widow.html": "friend at midnight; the friend at midnight; persistent friend; importunate friend; three loaves; persistent widow; the persistent widow; importunate widow; unjust judge; the unjust judge; unrighteous judge; judge and the widow; the widow and the judge; parable of the widow; pray always and not faint; ask seek knock",
    "parable-26-the-unprofitable-servants.html": "unprofitable servant; unprofitable servants; unworthy servants; worthless servants; the servant's duty; servant at the table; servants duty; plowing servant; we have done that which was our duty to do; the servant and his master; master and servant",
    "parable-27-the-lowest-seat-and-banquet-invitation.html": "lowest seat; the lowest seat; lowest room; the lowest place; best seats; chief seats; chief rooms; places of honor; places of honour; wedding guest; wedding guests; guests invited to a wedding; take the lowest seat; invite the poor; the humble guest; dinner at a pharisee's house; the banquet invitation",
    "parable-28-the-tower-and-the-warring-king.html": "counting the cost; count the cost; cost of discipleship; tower builder; man building a tower; building a tower; king going to war; warring king; the two kings; king and ten thousand; two kings at war; unfinished tower; tower",
    "parable-29-the-laborers-in-the-vineyard.html": "workers in the vineyard; laborers in the vineyard; labourers in the vineyard; vineyard workers; vineyard laborers; the eleventh hour; eleventh hour workers; the last shall be first; householder hired laborers; the generous landowner; the landowner; the vineyard owner; a penny a day; denarius a day; equal pay; the day laborers; day laborers",
    "parable-30-the-ten-virgins.html": "ten bridesmaids; ten maidens; wise and foolish virgins; five wise and five foolish; five wise virgins; five foolish virgins; the virgins; the bridesmaids; the bridegroom; lamps and oil; oil and lamps; the wise virgins; the foolish virgins; midnight cry",
    "parable-31-the-sheep-and-the-goats.html": "sheep and goats; the last judgment; judgment of the nations; judgement of the nations; the least of these; least of these my brethren; least of these my brothers; son of man in glory; separating the sheep from the goats; i was hungry and ye gave me meat; hungry and thirsty; the final judgment; the judgment seat of the son of man",
    "parable-32-the-fig-tree-lesson.html": "lesson of the fig tree; lesson from the fig tree; learn a parable of the fig tree; learn a lesson from the fig tree; the budding fig tree; budding fig tree; fig tree puts forth leaves; fig tree and all the trees; fig tree leaves; summer is near; this generation shall not pass; the fig tree; the fig tree and all the trees; olivet; olivet discourse",
    "parable-33-the-thief-and-watchful-servants.html": "thief in the night; the thief in the night; the thief; watchful servants; the watchful servants; master of the house; goodman of the house; householder and the thief; the doorkeeper; doorkeeper; servants waiting for their master; waiting servants; servants watching; be ye also ready; the master returns from the wedding; watch and be ready; the burglar; the watchful servant; faithful watchers",
    "parable-34-the-narrow-door.html": "narrow gate; the narrow gate; strait gate; the strait gate; strive to enter in at the strait gate; shut door; the shut door; master of the house shut the door; few be saved; are there few that be saved; the narrow way; the narrow door; narrow and wide gates; wide gate and narrow gate; depart from me ye workers of iniquity"
  };
  // Matching: commas or semicolons separate names (any one may match); within a name, every word must appear.
  const stop = new Set(['the', 'a', 'an', 'of', 'and', 'in', 'to', 'on', 'parable']);
  const fold = value => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[’'`]s?\b/g, '').replace(/[–—-]/g, ' ').replace(/[^a-z0-9: ]+/g, ' ').replace(/\s+/g, ' ').trim();
  const words = value => fold(value).split(' ').filter(word => word && !stop.has(word));
  const matches = (item, query) => query.split(/[,;]+/).map(words).filter(list => list.length).some(list => {
    if (list.some(word => /\d/.test(word))) return item.folded.includes(list.join(' '));
    return list.every(word => item.tokens.some(token => token.startsWith(word) || token.startsWith(word.replace(/s$/, ''))));
  });
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
  }).map(item => {
    const text = item.searchText.replace(item.group.toLowerCase(), '');
    item.folded = fold(`${text} ${aliases[item.page] || ''}`);
    item.tokens = item.folded.split(' ');
    return item;
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
        (!query || matches(item, query));
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
      matches(item, query)).slice(0, 6);
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
