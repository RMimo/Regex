# use re.split() to split a string at all of its , and . symbols:
regex_pattern = r"\,|\."	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
