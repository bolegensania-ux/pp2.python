# task 1

import re
string = input()
exp = r'ab*'
if re.fullmatch(exp, string):
    print("match found:", string)
else:
    print("match was not found")

# task 2

s = input()
p = r'ab{2,3}'
if re.fullmatch(p, s):
    print("match is:", s)
else:
    print("match was not found")

# task 3
t = input()
pat = r'[a-z]+_[a-z]+'
match = re.findall(pat, t)
print(match)

# task 4
y = input()
patt = r'[A-Z][a-z]+'
matches = re.findall(patt, y)
print(matches)

# task 5
u = input()
d = r'a.*b\b'
if re.fullmatch(d, u):
    print("match is found:", u)
else:
    print("match is not found")

# task 6
i = input()
f = re.sub(r'[ ,.]', ':', i)
print(i)

# task 7
text = input()
words = text.split("_")
camel = words[0] + "".join(word.capitalize() for word in words[1:])
print(camel)

# task 8
txt = input()
res = re.split(r"(?=[A-Z])", txt)
print(res)

# task 9
tx = input()
rs = re.sub(r"([A-Z])", r"\1", tx)
print(rs)

# task 10
c = "helloWorldTest"

sn = re.sub(r"([A-Z])", r"_\1", c).lower()

print(sn)