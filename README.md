# wifi-word

[![make.fun · u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/nmlyz/wifi-word/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/nmlyz/wifi-word/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

A tiny program that writes one word for your Wi-Fi to a file. The word is three letters: the router comes when called, leaves when it pleases, and knocks things off the table on its way out. It is the only honest name for a network that ignores you all day and purrs back to life at midnight.

## Run it

```sh
python3 main.py
```

It writes the word to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Standard library only, no network, deterministic: two runs produce byte-identical output. Before writing, it checks the word is a single word of 1–20 characters, then flushes the file to disk.

## The word

> Cat

Thirty-six candidate words were written from deliberately different angles, the cliches were thrown out, and the survivors were judged pairwise against the brief by three readers — a comedy editor weighing freshness, a housemate living with flaky Wi-Fi weighing the laugh on first read, and a literalist weighing whether the word could only describe a home network. The cat word won the final 2-1.

---

Entered on [make.fun](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).
