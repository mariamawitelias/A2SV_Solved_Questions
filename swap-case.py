def swap_case(s):
    for i in s:
        if i == i.upper():
            i.lower()
        else:
            i.upper()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
