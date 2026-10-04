import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w in (1280,390,360,320):
            pg=await b.new_page(viewport={'width':w,'height':900})
            bad=[]
            pg.on('response',lambda r:bad.append(r.url) if r.status>=400 else None)
            await pg.goto('http://localhost:8140/study-50-election.html'); await pg.wait_for_timeout(500)
            r=await pg.evaluate("()=>[document.documentElement.scrollWidth,innerWidth,[...document.images].filter(i=>!i.complete||!i.naturalWidth).length,document.querySelector('.detail-format').textContent]")
            print(w,r,bad)
        await b.close()
asyncio.run(main())
