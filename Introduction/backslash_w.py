# The expression \w will match any word character.
# Word characters include alphanumeric characters (a-z,A-Z and 0-9) and underscores (_).

# \W matches any non-word character.
# Non-word characters include characters OTHER THAN alphanumeric characters (a-z,A-Z and 0-9) and underscores (_).

import re
pattern = r"\w{3}\W\w{12}\W\w{3}"
string = 'www.introtoregex.com'

print(re.match(pattern, string))
