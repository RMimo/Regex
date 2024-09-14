# A group() expression returns one or more subgroups of the match.
import re
pattern = r'(\w+)@(\w+)\.(\w+)'

# r'': This means the string is a raw string in Python. Raw strings treat backslashes (\) as literal characters, so you don't need to escape them. Without the r, you'd need to double the backslashes in the pattern to avoid Python treating them as escape characters.

# \w matches any word character, which includes alphanumeric characters (letters, digits) and underscores (_).

# + means "one or more" of the preceding character, so \w+ will match one or more word characters.

# The parentheses () around \w+ create a capturing group. This allows you to extract the part of the string that matches this portion of the pattern.

# @: This is a literal @ symbol, as found in email addresses.

# (\w+): Another capturing group for the domain part of the email, just like the first (\w+). 

# \.: This matches a literal dot (.). Because the dot has a special meaning in regex (it matches any character), it is escaped with a backslash (\.) to make it match an actual dot.

# (\w+): The final capturing group that matches the domain extension (e.g., com, net, org), similar to the previous groups, matching one or more word characters.


m = re.match(pattern, 'username@introregex.com')
print(m.group(0))      # The entire match 
print(m.group(1))      # The first parenthesized subgroup.
print(m.group(2))      # The second parenthesized subgroup.
print(m.group(3))      # The third parenthesized subgroup.
print(m.group(1,2,3))  # Multiple arguments give us a tuple.
