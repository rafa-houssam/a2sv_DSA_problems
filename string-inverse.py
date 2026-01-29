

def swap_case(s):
    ss=''
    for digit in s:
        if (digit.upper()==digit):
            ss+=digit.lower()
        else:
            ss+=digit.upper()
    return ss

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)