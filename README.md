# 27 November 2026 — The World in One Image (v6)

Entry for the make.fun bounty **news-image-20261127**: one image summing up
the world's news of Friday 27 November 2026.

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/yiw8551/news-image-20261127-v6/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/yiw8551/news-image-20261127-v6/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

## The image

44 stories across 10 regions, each checked against reporting from
27 November 2026 (Reuters, AP, BBC, Al Jazeera, Euronews, NDTV). The full
leader package on a clean grid: 3 large drawn scenes (the Kuwait drone
strike, tankers hit by mines off Hormuz, the EU summit) plus 10 small
scenes, a world map with numbered pins, a UTC timeline of the day, a
DATE CHECK box excluding older news, an "ALSO ON FRIDAY" list, and a
numbers strip. Lead stories: the Kuwait drone attack that killed two
Italian technicians, Iran's claim that naval mines hit two tankers in
the Strait of Hormuz, and the EU summit ending early with the €45bn
Ukraine loan pushed to December. Also featured: Israeli strikes in Gaza,
Trump telling Putin to end aggression across Europe, the Macy's parade
postponed by the Thanksgiving storm, Black Friday opening with US online
spending forecast at $12.9bn, the DR Congo Ebola outbreak passing 12,000
cases, and De Cos named the next ECB president.

## How it runs

`main.py` (Python 3, standard library only) copies the pre-rendered
`entry.png` (1024x1024, under 1 MiB) to `<output-dir>/entry.png`, where the
output directory is `argv[1]`, `$MAKEFUN_OUTPUT_DIR`, or `/output`, in that
order. It verifies the copy byte-for-byte (SHA-256) and exits non-zero if
anything is wrong.

```sh
python3 main.py /tmp/out   # writes /tmp/out/entry.png
```
