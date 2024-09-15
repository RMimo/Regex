# The ^ symbol matches the position at the start of a string.
# Suppose that our string must start with a digit, has 6 characters, 5 of them word characters

import re
start_pattern = r'^\d\w{5}'
string = '1abcde'

print(re.match(pattern=start_pattern, string=string))
