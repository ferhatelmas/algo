class LeaguePicks:
	def returnPicks(self, position, friends, picks):
		ls, d, r, i = [], True, friends - position + 1, 0
		while (d and picks >= position) or (not d and picks >= r):
			ls.append(i + (position if d else r))
			i += friends
			picks -= friends
			d = not d
		return ls
