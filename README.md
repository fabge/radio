# Barakan Beat

This is a collection of recordings of Barakan Beat, a radio show by [Peter Barakan](https://peterbarakan.net/), updated weekly.

{% for file in site.static_files %}
{% if file.extname == ".m4a" and file.path contains "/audio/" %}
<p>Barakan Beat, {{ file.basename }} (<a href="{{ file.path }}" download>download</a>)</p>
<audio id="player{{ forloop.index }}" controls src="{{ file.path }}" preload="none"></audio>
{% endif %}
{% endfor %}
