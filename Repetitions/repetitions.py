# The tool {x} will match exactly x repetitions of character/character class/groups.

# w{3} will match the character w exactly 3 times.
# [xyz]{5} will match the string of length 5 consisting of characters {x, y, z}. For example it will match xxxxx, xxxyy and xyxyz.
# \d{4} will match any digit exactly 4 times.

# For example: write a regex that will match the string S using the following conditions:

# S must be of length equal to 45.
# The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
# The last 5 characters should consist of odd digits or whitespace characters.

import re 

pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'

S1 = '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13' # 42
S2 = '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57' # 45

print(re.match(pattern, S1))
print(re.match(pattern, S2))