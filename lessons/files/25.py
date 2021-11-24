import re
vowels = ['a','e','i','o','u','y']
text="To be, or not to be, that is the question"
num = len(re.findall("[vowels]",text))
print(f"Number of vowels = {num}")