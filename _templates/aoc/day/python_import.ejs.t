---
to: python/aoc/year<%= year %>/__init__.py
after: (?![\r\n])
---
from .day<%= dayPadded %> import *
