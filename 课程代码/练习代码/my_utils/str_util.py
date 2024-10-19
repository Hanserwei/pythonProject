def str_reverse(s):
    s1 = s[::-1]
    return s1

def substr(s,x,y):
    s2 = s[x:y:]
    return s2

if __name__ == '__main__':
    print(str_reverse('0123456789'))
    print(substr('0123456789',0,5))