# We can match a specific string X in a test string by making our regex pattern X. This is one of the simplest patterns. 

import re
match = r'match'
string = 'www.match_match.com'

print(len(re.findall(pattern=match, string=string)))
