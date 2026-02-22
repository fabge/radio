# Barakan Beat

This is a collection of recordings of Barakan Beat, a radio show by [Peter Barakan](https://peterbarakan.net/), updated each Sunday at 13:05 UTC.

<!-- [[[cog
import cog
from pathlib import Path
from datetime import datetime

audio_dir = Path('audio')
files = sorted(
    audio_dir.glob('*.m4a'),
    key=lambda f: datetime.strptime(f.stem, '%d.%m.%Y'),
    reverse=True
)

for i, file in enumerate(files, 1):
    cog.outl(f'<p>Barakan Beat, {file.stem} (<a href="/{file}" download>download</a>)</p>')
    cog.outl(f'<audio id="player{i}" controls src="/{file}" preload="none"></audio>')
    cog.outl('')
]]] -->
<p>Barakan Beat, 22.02.2026 (<a href="/audio/22.02.2026.m4a" download>download</a>)</p>
<audio id="player1" controls src="/audio/22.02.2026.m4a" preload="none"></audio>

<p>Barakan Beat, 15.02.2026 (<a href="/audio/15.02.2026.m4a" download>download</a>)</p>
<audio id="player2" controls src="/audio/15.02.2026.m4a" preload="none"></audio>

<p>Barakan Beat, 25.01.2026 (<a href="/audio/25.01.2026.m4a" download>download</a>)</p>
<audio id="player3" controls src="/audio/25.01.2026.m4a" preload="none"></audio>

<p>Barakan Beat, 28.12.2025 (<a href="/audio/28.12.2025.m4a" download>download</a>)</p>
<audio id="player4" controls src="/audio/28.12.2025.m4a" preload="none"></audio>

<p>Barakan Beat, 21.12.2025 (<a href="/audio/21.12.2025.m4a" download>download</a>)</p>
<audio id="player5" controls src="/audio/21.12.2025.m4a" preload="none"></audio>

<p>Barakan Beat, 30.11.2025 (<a href="/audio/30.11.2025.m4a" download>download</a>)</p>
<audio id="player6" controls src="/audio/30.11.2025.m4a" preload="none"></audio>

<!-- [[[end]]] -->
