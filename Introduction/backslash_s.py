# \s matches any whitespace character [ \r\n\t\f ].
# \S matches any non-white space character.

import re

pattern = r"(\S{2}\s){2}\S{2}" # equivalent of r"\S\S\s\S\S\s\S\S"
string = '12 11 15'

print(re.match(pattern, string))
