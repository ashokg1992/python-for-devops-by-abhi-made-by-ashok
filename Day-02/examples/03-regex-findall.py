import re  # 

text = "The quick brown fox"
pattern = r"brown"  # it means in the above data that is assigned to variable "text", if any string is matched with "brown " print it

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
