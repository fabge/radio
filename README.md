# Barakan Beat

This is a collection of recordings of Barakan Beat, a radio show by [Peter Barakan](https://peterbarakan.net/), updated each Sunday at 13:05 UTC.

<!-- [[[cog
import cog
from pathlib import Path
from datetime import datetime

audio_dir = Path('audio')
music_dir = audio_dir / 'music'
files = sorted(
    audio_dir.glob('*.m4a'),
    key=lambda f: datetime.strptime(f.stem, '%d.%m.%Y'),
    reverse=True
)

for i, file in enumerate(files):
    music = music_dir / file.name
    cog.outl('<div class="episode">')
    cog.outl(f'<p>Barakan Beat, {file.stem}<br>full (<a href="/{file}" download>download</a>) · music only (<a href="/{music}" download>download</a>)</p>')
    cog.outl(f'<audio id="player{2*i+1}" controls src="/{file}" preload="none"></audio>')
    cog.outl(f'<audio id="player{2*i+2}" controls src="/{music}" preload="none"></audio>')
    cog.outl('</div>')
]]] -->
<div class="episode">
<p>Barakan Beat, 09.08.2026<br>full (<a href="/audio/09.08.2026.m4a" download>download</a>) · music only (<a href="/audio/music/09.08.2026.m4a" download>download</a>)</p>
<audio id="player1" controls src="/audio/09.08.2026.m4a" preload="none"></audio>
<audio id="player2" controls src="/audio/music/09.08.2026.m4a" preload="none"></audio>
</div>
<div class="episode">
<p>Barakan Beat, 02.08.2026<br>full (<a href="/audio/02.08.2026.m4a" download>download</a>) · music only (<a href="/audio/music/02.08.2026.m4a" download>download</a>)</p>
<audio id="player3" controls src="/audio/02.08.2026.m4a" preload="none"></audio>
<audio id="player4" controls src="/audio/music/02.08.2026.m4a" preload="none"></audio>
</div>
<div class="episode">
<p>Barakan Beat, 31.05.2026<br>full (<a href="/audio/31.05.2026.m4a" download>download</a>) · music only (<a href="/audio/music/31.05.2026.m4a" download>download</a>)</p>
<audio id="player5" controls src="/audio/31.05.2026.m4a" preload="none"></audio>
<audio id="player6" controls src="/audio/music/31.05.2026.m4a" preload="none"></audio>
</div>
<div class="episode">
<p>Barakan Beat, 29.03.2026<br>full (<a href="/audio/29.03.2026.m4a" download>download</a>) · music only (<a href="/audio/music/29.03.2026.m4a" download>download</a>)</p>
<audio id="player7" controls src="/audio/29.03.2026.m4a" preload="none"></audio>
<audio id="player8" controls src="/audio/music/29.03.2026.m4a" preload="none"></audio>
</div>
<div class="episode">
<p>Barakan Beat, 28.12.2025<br>full (<a href="/audio/28.12.2025.m4a" download>download</a>) · music only (<a href="/audio/music/28.12.2025.m4a" download>download</a>)</p>
<audio id="player9" controls src="/audio/28.12.2025.m4a" preload="none"></audio>
<audio id="player10" controls src="/audio/music/28.12.2025.m4a" preload="none"></audio>
</div>
<div class="episode">
<p>Barakan Beat, 30.11.2025<br>full (<a href="/audio/30.11.2025.m4a" download>download</a>) · music only (<a href="/audio/music/30.11.2025.m4a" download>download</a>)</p>
<audio id="player11" controls src="/audio/30.11.2025.m4a" preload="none"></audio>
<audio id="player12" controls src="/audio/music/30.11.2025.m4a" preload="none"></audio>
</div>
<!-- [[[end]]] -->
