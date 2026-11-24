# news-image-20261123 — v2: "Photo Triptych + Photo Deck Grid"

One image summing up Monday 23 November 2026 world news: masthead +
number strip, 3 photo leads (Nvidia's Huang returns, 153 drones over
Ukraine, Java factory toll put at 24), 12 mid cards each with a photo
+ headline + 1-line deck, a generated world map with numbered pins
(one per lead + mid card, pin colour = region), and a numbered "Also on
Monday" list of 30 briefs in 3 columns — 45 stories, 6 continents.

All 15 photos (3 leads + 12 mid cards) and the world map were
generated with Muse's image generation (no text inside the photos);
all text was composited with PIL from the verified story list, so
every headline and deck is exact. Every story was verified against a
primary source for 23 Nov 2026 UTC: the 30 original stories passed
Warden R1 (30/30, 0 wrong dates); the 17 new stories are logged in the
rebuild's `DATE-LOG-R2.md`. The Medicare card was dropped (its AP
article first ran 20 Nov) and the Asia-markets brief reads "Seoul
falls" only (the Taiex rose +2.23% that Monday). Huang appears exactly
twice (lead 1 + card 26); the old cards 27 and 30 were replaced. Card
16's deck reads "One of the largest cybersecurity deals." (Reuters:
"one of the largest"). Card 42's deck reads "404 of 429 Brussels
flights cut." (Brussels Airport spokesperson: 404 flights could not
operate, 429 scheduled). Card 45 reads "NHS opens sign-up for largest
AI cancer trial" (23 Nov = recruitment opening for the EDITH trial).
Pin positions were calibrated from the generated map's own land mask
(Europe pins nudged so all 15 numbers stay readable).

`main.py` (stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, then reads the file back and exits with
an error if the written bytes are not exactly the repository image. The image was composited with PIL
(`../work/render-v2.py`): the photos are centre-cropped into their
panels and all text is drawn from the verified list; re-running the
renderer twice produces byte-identical output.

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/intemu2/news-image-20261123-qwen/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/intemu2/news-image-20261123-qwen/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
