#match a word starting with "a" and end with "e"
import re
pattern = r'\ba\w*e\b'
text = "apple ace axe are ample"
print(re.findall(pattern,text))


