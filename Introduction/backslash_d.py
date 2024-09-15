# The expression \d matches any digit [0 - 9].
# The expression \D matches any character that is not a digit.

import re

pattern1 = r'\d{3}' # equivalent of r'\d\d\d'
pattern2 = r'\D{5}' # equivalent of r'\D\D\D\D\D'
pattern3 = r'(\d{2}\D){2}' # equivalent of r'\d\d\D\d\d\D'
pattern4 = r'((\d{2}\D){2})\d{4}' # equivalent of r"\d\d\D\d\d\D\d\d\d\d"

string = 'Intro001'
string2 = '06-11-2015'
string3 = '6-11-2015'

print(re.search(pattern1, string))
print(re.search(pattern2, string))
print(re.search(pattern3, string2))
print(re.search(pattern4, string2))
print(re.search(pattern4, string3))
