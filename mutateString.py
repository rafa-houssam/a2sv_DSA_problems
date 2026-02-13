def mutate_string(string, position, character):
    liststring=list(string)
    liststring[position]=character
    return "".join(liststring)
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)