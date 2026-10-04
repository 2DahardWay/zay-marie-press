# 2026-10-04: bare shorthand "Prophecy is suspended" -> "Israel’s Prophecy Program is nationally suspended"
# applied in place (run-level) to Studies 4, 9, 11, 13, 17, 18, 20; page counts unchanged.
import re
R=[(re.compile(r'(?<!Program )Prophecy is suspended'),'Israel’s Prophecy Program is nationally suspended'),
   (re.compile(r'Acts 28 suspends Prophecy;'),'Acts 28 suspends Israel’s Prophecy Program;')]
