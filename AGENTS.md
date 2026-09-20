# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## Overview

This is a Jekyll/GitHub Pages site (served at `radio.fabiangeiger.com`, see `CNAME`) that hosts weekly recordings of *Barakan Beat*, a radio show by Peter Barakan. The recordings are captured automatically from Radiko and published as audio files. Each episode is published twice: the full recording in `audio/`, and a music-only version (moderator speech removed) in `audio/music/`.

## Architecture

The system has four pieces that work together:

1. **`rec_radiko_ts.sh`** — A third-party Radiko timefree recorder (by uru, MIT-licensed). It authenticates against Radiko, fetches the timefree stream, and muxes it into an `.m4a`. Treat as vendored — generally don't modify. Key options: `-s` station ID (the show airs on `INT` / InterFM), `-f` start datetime (JST), `-d` duration in minutes, `-o` output path. Recordings are named `audio/DD.MM.YYYY.m4a`.

2. **`strip_speech.py`** — Produces the music-only cut. Runs `inaSpeechSegmenter` over the recording to label the timeline speech/music/noise, drops speech segments of at least `MIN_SPEECH` (3 s), merges the contiguous remainder, and crossfade-concatenates it with `ffmpeg` (`XFADE` = 0.1 s). Called as `strip_speech.py INPUT.m4a OUTPUT.m4a`; the output goes to `audio/music/DD.MM.YYYY.m4a` under the same filename as the original.

3. **`.github/workflows/record.yml`** — The orchestrator, runs every Sunday 13:05 UTC (also `workflow_dispatch`), with a 180-minute timeout to cover recording plus segmentation. Because Radiko geoblocks to Japan, it connects to a Mullvad WireGuard VPN (from `MULLVAD_WG_CONFIG` secret) and verifies the IP is `JP` before recording. The recording date is computed as "6 hours ago" in JST so a queue delay past midnight still picks the right day. After recording it drops the VPN, generates the music-only version, regenerates the README, commits the new files, and prunes history to the last 5 recordings using `git-filter-repo` + force-push.

4. **`README.md`** — The site's homepage. The audio player list between the `[[[cog ... ]]]` / `[[[end]]]` markers is **generated**, not hand-edited. It uses [cogapp](https://nedbatchelder.com/code/cog/) to enumerate `audio/*.m4a`, sort by date descending, and emit one `.episode` block per show with two `<audio>` elements (full and music-only) plus download links.

## Commands

Regenerate the README audio list after adding/removing recordings:

```sh
pip install cogapp
cog -r README.md
```

Record manually (requires a Japanese IP / VPN):

```sh
./rec_radiko_ts.sh -s INT -f YYYYMMDD1800 -d 120 -o audio/DD.MM.YYYY.m4a
```

Generate the music-only version:

```sh
pip install "inaSpeechSegmenter>=0.8.0"
python strip_speech.py audio/DD.MM.YYYY.m4a audio/music/DD.MM.YYYY.m4a
```

## Notes

- `_includes/head-custom.html` overrides the Jekyll theme's head to load the Plyr audio player (CDN) and style it; the `id="player*"` attributes emitted by the cog block in README.md are what Plyr binds to. The cog block emits two players per episode, so IDs run `player1`, `player2`, … two per date.
- History is intentionally rewritten by the workflow's cleanup step to avoid the repo growing unbounded with audio blobs — only the most recent 5 recordings exist in git history (originals and music-only versions are pruned together).
- `_site/` is Jekyll build output and is not tracked.
