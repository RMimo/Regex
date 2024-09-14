# These expressions return the indices of the start and end of the substring matched by the group.

import re
pattern = r'\d+' # a regular expression pattern  

# The r before the string makes it a raw string literal, meaning that escape sequences (like \) are treated as literal characters. 
# Without the r, Python would interpret \d as an escape sequence.
# \d represents any digit (0-9).
# + means "one or more" of the preceding element (digits in this case).
# So, \d+ means "one or more digits."

string = '1234'

m = re.search(pattern, string) # used to search for a match of the given pattern in the input string

print(m.start()) # if a match is found, m.start() returns the starting index of the match within the string
print(m.end()) # if a match is found, m.end() returns the ending index of the match within the string

