(() => {
  const links = document.querySelectorAll('[data-parable-preview]');
  if (!links.length) return;

  const dialog = document.createElement('dialog');
  dialog.className = 'parable-preview-dialog';
  dialog.setAttribute('aria-label', 'Enlarged study preview');
  dialog.innerHTML = '<div class="parable-preview-dialog-inner"><button class="parable-preview-close" type="button" aria-label="Close study preview">×</button><img alt=""><p>Select × or press Esc to return to the study page.</p></div>';
  document.body.append(dialog);

  const image = dialog.querySelector('img');
  const close = dialog.querySelector('button');
  let opener = null;

  links.forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    opener = link;
    image.src = link.href;
    image.alt = link.querySelector('img')?.alt || 'Study preview page';
    dialog.showModal();
    close.focus();
  }));

  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => {
    image.removeAttribute('src');
    opener?.focus();
  });
})();
