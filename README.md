# Peter Barakan radio recordings

This is a collection of radio recordings of Barakan Beat, a radio show by [Peter Barakan](https://peterbarakan.net/).

{% for file in site.static_files %}
{% if file.extname == ".m4a" and file.path contains "/audio/" %}
<p>Barakan Beat, {{ file.basename }} (<a href="{{ file.path }}">download</a>)</p>
<audio id="player{{ forloop.index }}" controls src="{{ file.path }}"></audio>
{% endif %}
{% endfor %}
