# The + tool will match one or more repetitions of character/character class/group.

# w+ will match the character w 1 or more times.
# [xyz]+ will match the character x, y or z 1 or more times.
# \d+ will match any digit 1 or more times.

# Writing a regex that will match the string S using the following conditions:

# S should begin with 1 or more digits.
# After that, S should have 1 or more uppercase letters.
# S should end with  or more lowercase letters.

import re
pattern = r'^\d+[A-Z]+[a-z]+$'

S1 = '1Qa'
S2 = '1Q'

print(re.match(pattern, S1))
print(re.match(pattern, S2))