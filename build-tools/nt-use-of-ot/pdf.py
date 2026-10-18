from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':900})
    pg.goto('file:///home/claude/zay-marie-press/new-testament-use-of-old-testament.html'); pg.wait_for_timeout(500)
    pg.emulate_media(media='print')
    pg.pdf(path='/home/claude/zay-marie-press/assets/new-testament-use-of-old-testament.pdf',format='Letter',print_background=True,margin={'top':'0.5in','bottom':'0.5in','left':'0.5in','right':'0.5in'})
    pg.emulate_media(media='screen')
    pg.screenshot(path='/tmp/claude-0/nt_full.png',full_page=True)
    pg2=b.new_page(viewport={'width':390,'height':800}); pg2.goto('file:///home/claude/zay-marie-press/new-testament-use-of-old-testament.html'); pg2.wait_for_timeout(400)
    print('mobile overflow',pg2.evaluate('document.documentElement.scrollWidth'),390)
