# The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
import re
print(re.findall(r'\w','http://www.introregex.com/'))
print(re.findall(r'(\W)','http://www.introregex.com/'))
print(re.findall(r'(\w+)','http://www.introregex.com/'))
print(re.findall(r'(\W+)','http://www.introregex.com/'))