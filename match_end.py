# The $ symbol matches the position at the end of a string.
# Suppose that our string must end with a digit, has 6 characters, 5 of them word characters

import re
start_pattern = r'\w{5}\d$'
string = 'abcde1'

print(re.match(pattern=start_pattern, string=string))