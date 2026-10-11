# The Lord's Ministry Route Map (build recipe)

Free interactive page `jesus-ministry-map.html` (Master Standard v1.130). Mode 2 voice; mode label never shown.

- `stops.py` — 48 stops in eight phases (`PH`, `S`), the last-week day list (`WEEK`) and the limits list. Each stop: id, phase, label, lat, lon, location certainty (S named / C context / I inferred), tags, passages, what happens, what Scripture does not say.
- `chk.py` — verifies every reference exists in the KJV corpus and every “quoted” phrase is in that stop's passages (run `python3 chk.py`; must end `errs 0`).
- `kjv.py` — reads `/home/claude/aruljohn/bible-kjv/<Book>.json` (clone github.com/aruljohn/bible-kjv).
- `geo.py` — projects Natural Earth 10m land, lakes (Sea of Galilee, Dead Sea) and the Jordan into the SVG; set `NE_GEOJSON` to the `geojson/` folder of a sparse clone of `nvkelso/natural-earth-vector`.
- `page.css`, `page.js`, `body.html` — page template; `gen.py` embeds the data and writes `jesus-ministry-map.html`.

Rebuild: `NE_GEOJSON=<path> python3 gen.py`, then copy the page to the repo root. A change to a stop is made in `stops.py`, checked with `chk.py` and regenerated. Placements marked Inferred are the map's, not the text's.
