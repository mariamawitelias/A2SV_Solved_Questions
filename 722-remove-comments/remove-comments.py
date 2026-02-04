class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block = False
        res = []
        new = []
        for code in source:
            i  = 0
            while i < len(code):
                if not block:
                    if i + 1 < len(code) and code[i] == '/' and code[i + 1] == '*':
                        block = True
                        i += 2
                    elif i + 1 < len(code) and code[i] == '/' and code[i + 1] == '/':
                        break
                    else:
                        new.append(code[i])
                        i += 1
                else:
                    if i + 1 < len(code) and code[i] == '*' and code[i + 1] == '/':
                        block = False
                        i += 2
                    else:
                        i += 1
            if new and not block:
                res.append("". join(new))
                new = []
        return res


        