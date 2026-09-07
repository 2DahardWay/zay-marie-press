(() => {
  const approvedOld = 'This seven-day devotional lets the practical fruit of the framework come forward: your identity and position in Christ. Select a day below.';
  const approvedScreen = 'This seven-day devotional focuses on the practical fruit of Pauline truth: your identity, position, walk, and hope in Christ. Select a day below.';
  const approvedPrint = 'This seven-day devotional focuses on the practical fruit of Pauline truth: your identity, position, walk, and hope in Christ.';

  const devotionalDays = {
    1:['You Are in Christ','The believer’s fundamental identity is no longer determined by the old life but by his or her position in Christ.','2 Corinthians 5:17; Ephesians 1:3–7','Thank God for the new identity He has given you in Christ. Ask Him to help you think and live from that position.'],
    2:['You Are Accepted by Grace','Your standing before God rests upon His grace and Christ’s finished work, not your religious performance.','Ephesians 1:6–7; 2:8–9; Romans 5:1–2','Give thanks that acceptance before God rests in His grace rather than your ability to earn His favor.'],
    3:['You Are Complete in Christ','You do not need to acquire a superior spiritual standing through religious ordinances, human regulations, or personal merit.','Colossians 2:8–10','Thank God for your completeness in Christ and ask for discernment to reject anything that treats Christ as insufficient.'],
    4:['You Are a Member of One Body','Believing Jews and Gentiles share equal standing in the Body of Christ without national distinction or covenantal hierarchy.','1 Corinthians 12:12–13; Ephesians 3:6','Thank God for placing you in one Body and ask Him to shape your relationships with other believers accordingly.'],
    5:['You Are Blessed in the Heavenly Places','The Body of Christ possesses a heavenly calling and spiritual blessings in Christ.','Ephesians 1:3; 2:4–6','Thank God for the spiritual blessings that are already yours in Christ and ask for greater understanding of your heavenly position.'],
    6:['Walk from Your Position','Christian conduct flows from the believer’s position in Christ; it does not create that position.','Romans 12:1–2; Ephesians 4:1; Colossians 2:6–7','Ask God to renew your thinking so that your daily walk increasingly reflects the position He has already given you in Christ.'],
    7:['Your Hope Is in Christ','Your future is secure in Christ and culminates in glorification and the heavenly destiny of the Body of Christ.','Philippians 3:20–21; 1 Thessalonians 4:13–18','Thank God for your secure hope in Christ and ask Him to let that future hope shape your present faithfulness.']
  };

  const reflection = 'Read the passages slowly. What do they say God has already made true of you in Christ? How should that truth shape the way you think and walk today?';

  const style = document.createElement('style');
  style.textContent = `
    .rl-print-only{display:none}
    .rl-devotional-print{display:none}
    @media print{
      body.rl-printing .rl-screen-only{display:none!important}
      body.rl-printing .rl-print-only{display:inline!important}
      body.rl-printing .rl-days,
      body.rl-printing .rl-devotional{display:none!important}
      body.rl-printing .rl-devotional-print{display:block!important}
      body.rl-printing .rl-devotional-print h3,
      body.rl-printing .rl-devotional-print h4{break-after:avoid-page;page-break-after:avoid}
      body.rl-printing .rl-devotional-print .rl-principle{break-inside:avoid-page;page-break-inside:avoid}
    }
  `;
  document.head.appendChild(style);

  const buildPrintDevotional = () => {
    return Object.entries(devotionalDays).map(([n,d]) => `
      <section class="rl-print-day">
        <h3>Day ${n} — ${d[0]}</h3>
        <h4>Truth</h4><p>${d[1]}</p>
        <h4>Scripture</h4><p>${d[2]}</p>
        <h4>Reflection</h4><p>${reflection}</p>
        <h4>Prayer</h4><p>${d[3]}</p>
        ${Number(n)===7?'<div class="rl-principle"><strong>Closing Truth</strong><p>Your identity in Christ is not something you are trying to achieve. It is the position God has already given you by grace. Christian growth begins by knowing what God has made you in Christ and learning to walk consistently with that truth.</p></div>':''}
      </section>`).join('');
  };

  const applyApprovedResource10 = () => {
    const title = document.querySelector('.rl-resource-head h2');
    if (!title || title.textContent.trim() !== '7-Day Devotional: Who You Are in Christ') return;

    const content = document.querySelector('.rl-content');
    if (!content) return;

    const intro = content.querySelector(':scope > p');
    if (intro && !intro.dataset.resource10Approved) {
      const current = intro.textContent.trim();
      if (current === approvedOld || current === approvedScreen || current.startsWith('This seven-day devotional')) {
        intro.innerHTML = `<span class="rl-screen-only">${approvedScreen}</span><span class="rl-print-only">${approvedPrint}</span>`;
        intro.dataset.resource10Approved = 'true';
      }
    }

    if (!content.querySelector('.rl-devotional-print')) {
      const printHost = document.createElement('div');
      printHost.className = 'rl-devotional-print';
      printHost.setAttribute('aria-hidden','true');
      printHost.innerHTML = buildPrintDevotional();
      const screenDevotional = content.querySelector('.rl-devotional');
      if (screenDevotional) screenDevotional.insertAdjacentElement('afterend', printHost);
      else content.appendChild(printHost);
    }
  };

  const observer = new MutationObserver(() => applyApprovedResource10());
  observer.observe(document.body, { childList: true, subtree: true });
  applyApprovedResource10();
})();
