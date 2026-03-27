s1 = input()
s2 = input()
send = 0
for i in s1:
    if i == '+':
        send += 1
    else:
        send -= 1
rec = 0
for i in s2:
    if i == '+':
        rec += 1
    elif i == '-':
        rec -= 1

q = s2.count('?')
if q == 0:
    if send == rec:
        print(1.0)
    else:
        print(0.0)
else:
    success = 0
    def backtrack(i, pos):
        global success
        if i == q:
            if pos == send:
                success += 1
            return
        backtrack(i + 1, pos + 1)
        backtrack(i + 1, pos - 1)
    backtrack(0, rec)

    total = 2 ** q
    print(success / total)