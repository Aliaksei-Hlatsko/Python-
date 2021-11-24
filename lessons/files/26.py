import re
text="To be, or not to be, that is the question"
words = len(re.findall("\w+",text))
print(f"Number of words = {words}")