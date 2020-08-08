playlist = {
	'title': 'Best Playlist Ever',
	'author': 'Rudy Martinez',
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['red'], 'duration': 3.5},
		{'title': 'song1', 'artist': ['orange'], 'duration': 2.0}
	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']
	print(total_length)
