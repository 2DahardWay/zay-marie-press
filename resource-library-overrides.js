(() => {
  const approvedOld = 'This seven-day devotional lets the practical fruit of the framework come forward: your identity and position in Christ. Select a day below.';
  const approvedNew = 'This seven-day devotional focuses on the practical fruit of Pauline truth: your identity, position, walk, and hope in Christ. Select a day below.';

  const applyApprovedResource10Copy = () => {
    document.querySelectorAll('.rl-content > p').forEach((p) => {
      if (p.textContent.trim() === approvedOld) p.textContent = approvedNew;
    });
  };

  const observer = new MutationObserver(applyApprovedResource10Copy);
  observer.observe(document.body, { childList: true, subtree: true });
  applyApprovedResource10Copy();
})();
