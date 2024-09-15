# The dot (.) matches anything (except for a newline).
# If you want to match (.) in the test string, you need to escape the dot by using a slash \..
# In Java, use \\. instead of \..

import re
import sys

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	

# ^ asserts the start of the string.
# .{3} matches exactly 3 characters (any character except newline).
# \. matches a literal dot (.).
# This pattern (.{3}\.) repeats for the other segments of the string, and .{3} matches the last 3 characters after the final dot.
# $ asserts the end of the string.
# This ensures that the string is exactly in the format abc.def.ghi.jkx.

test_strings = ['abc.def.ghi.jkx', 'abc.def.ghi.jkx1']
for string in test_strings:
    print(string)
    match = re.match(regex_pattern, string) is not None
    print(str(match).lower())
