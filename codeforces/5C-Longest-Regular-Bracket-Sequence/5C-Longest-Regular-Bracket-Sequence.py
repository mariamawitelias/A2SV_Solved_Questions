s = input()
stack = [-1]
res = 0
count = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            if length > res:
                res = length
                count = 1
            elif length == res:
                count += 1
if res == 0:
    print(0, 1)
else:
    print(res, count)