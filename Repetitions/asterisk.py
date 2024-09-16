# The * tool will match zero or more repetitions of character/character class/group.

# For Example:
# w* match the character w  or more times.
# [xyz]* match the characters x, y or z  or more times.
# \d* match any digit  or more times.

# Example: write a regex that will match the string S using the following conditions:

# S should begin with 2 or more digits.
# After that, S should have 0 or more lowercase letters.
# S should end with 0 or more uppercase letters

import re
pattern = r'^\d{2,}[a-z]*[A-Z]*$'

S1 = '14'
S2 = '1'

print(re.match(pattern, S1))
print(re.match(pattern, S2))
