"""Content loader. Chapter modules p0.py ... pN.py each define a list C of elements; tail.py defines CONC, APP, BIB."""
import importlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
META = dict(
    vol=1,
    title='The Bride Identity in Prophecy',
    subtitle='The Wife of the LORD, the Wife of the Lamb, and the Marriage Pattern Paul Teaches the Body',
    series='Prophetic Identity Commentary Series',
    imprint=('Copyright © 2026 Alexander S. Marien. All rights reserved. Published by Zay-Marie Press. '
             'Licensed for the personal use of the purchaser; no part may be reproduced or distributed without permission. '
             'Scripture quotations are from the King James Version (KJV).'),
)
ALL = []
_i = 0
while True:
    name = 'p%d' % _i
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), name + '.py')): break
    ALL += importlib.import_module(name).C
    _i += 1
if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tail.py')):
    t = importlib.import_module('tail')
    import appf, appg
    ALL += t.CONC + t.APP + appf.APPF + appg.APPG + t.BIB
