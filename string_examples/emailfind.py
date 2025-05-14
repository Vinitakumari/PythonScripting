
# extact the email addrees
import re

pattern = r'[\w\.-]+@[\w\.-]+\.(?:com|org|net)'
text = "vinitakumari1159@gmail.com or vinita@test.org"

print(re.findall(pattern, text))