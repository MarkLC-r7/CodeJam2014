import sys
from collections import Counter

BAD = 'Bad Magician!'
CHEATED = 'Volunteer cheated!'

T = int(sys.stdin.readline())

for case in range(1, T + 1):
	# Convert to row index
	first_choice = int(sys.stdin.readline()) - 1
	first_rows = [
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split()
	]
	# Convert to row index
	second_choice = int(sys.stdin.readline()) - 1
	second_rows = [
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split()
	]
	possibles = first_rows[first_choice]
	location = second_rows[second_choice]

	# Find duplicate values in both rows
	dupes = [x for x, y in Counter(possibles + location).items() if y > 1]

	# No number in both rows	
	if len(result) == 0:
		text = CHEATED
	# Multiple numbers in both rows. Magician Fail
	elif len(result) > 1:
		text = BAD
	# 1 Match
	else:
		text = str(result[0])
	
	sys.stdout.write('Case #%d: %s\n' % (case, text))

