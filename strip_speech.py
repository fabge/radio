#!/usr/bin/env python3
"""Produce a music-only version of a recording by cutting moderator speech.

Uses inaSpeechSegmenter to label the timeline as speech/music/noise, drops
speech segments longer than MIN_SPEECH, and crossfade-concatenates the rest.

Usage: strip_speech.py INPUT.m4a OUTPUT.m4a
"""

import subprocess
import sys
import tempfile

from inaSpeechSegmenter import Segmenter

MIN_SPEECH = 3.0  # only cut speech segments at least this long (seconds)
XFADE = 0.1  # crossfade between kept segments (seconds)


def main(src, dst):
    segments = Segmenter(detect_gender=False)(src)

    # Keep everything that isn't a sustained speech segment.
    keep = [(start, end) for label, start, end in segments if not (label == "speech" and end - start >= MIN_SPEECH)]

    # Merge intervals that are contiguous in the original timeline.
    merged = []
    for start, end in keep:
        if merged and start - merged[-1][1] < 1e-3:
            merged[-1] = (merged[-1][0], end)
        else:
            merged.append([start, end])

    # Build the filtergraph: trim each kept interval, then crossfade-chain them.
    lines = [f"[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[a{i}]" for i, (s, e) in enumerate(merged)]
    prev = "a0"
    for i in range(1, len(merged)):
        lines.append(f"[{prev}][a{i}]acrossfade=d={XFADE}[x{i}]")
        prev = f"x{i}"

    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(";\n".join(lines))
        script = f.name

    subprocess.run(
        ["ffmpeg", "-y", "-i", src, "-filter_complex_script", script, "-map", f"[{prev}]", "-c:a", "aac", "-b:a", "64k", dst],
        check=True,
    )


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
