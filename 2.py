text = "  Hello, World! Welcome to Python programming Language.  "

print(f"Text after stripping spaces: {text.strip()}")

print(f"\nText in uppercase: {text.upper()}")

print(f"\nText in lowercase: {text.lower()}")

print(f"\nNumber of occurrences of 'o': {text.count('o')}")

print(f"\nText after replacing 'Python' with 'HTML': {text.replace("Python", "Data HTML")}")

print(f"\nPosition of 'World' in the text: {text.find("World")}")

words = text.split() 
print(f"\nList of words in the text: {words}")

join = " ".join(words)  
print(f"\nText after joining words: {join}")     

print(f"\nDoes the text start with 'Hello'? {join.startswith("Hello")}")

print(f"\nDoes the text ends with 'Hello'? {join.endswith("Hello")}")

import re

text = """ John's email is [warrnerjhon@gmail.com]. He said, "Python is awesome!!"    It's a     great   language.
Another email: [xyz@gmail.com]. """

print(f"Text after removing special characters:{re.sub(r"[^a-zA-Z0-9@\.\s]", "", text)}")

print(f"\nText after replacing multiple spaces:{re.sub(r"\s+", " ", text)}")

print(f"\nWords starting with a vowel:{re.findall(r"\b[aeiouAEIOU]\w+", text)}")
 
print(f"\nText after replacing emails:{re.sub(r"\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b", "[abc@gmail.com]", text)}")
