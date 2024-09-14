# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
import re
print(re.finditer(r'\w','http://www.introregex.com/'))
print(*map(lambda x: x.group(), re.finditer(r'\w','http://www.introregex.com/')))
