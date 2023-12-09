v = "12"
w = "13"
u = "14"
s = "1" + "2" * 33 + "3" * 15 + "4" * 6
while w in s or v in s:
    if v in s:
        s = s.replace(v,"31",1)
    while w in s:
        s = s.replace(w, "441", 1)
    while u in s:
        s = s.replace(u, "221", 1)
s = s.replace("1", "333", 1)
sum = 0
for i in range(len(s)):
    sum = sum + int(s[i])
print(sum)
