# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
import re
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','username@introregex.com')
print(m.groupdict())