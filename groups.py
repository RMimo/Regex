# A groups() expression returns a tuple containing all the subgroups of the match.
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@introregex.com')
print(m.groups())