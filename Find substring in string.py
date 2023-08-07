# function to check if small string is
# there in big string
 
 
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
 
 
# driver code
string = "geeks for geeks"
sub_str = "geek"
check(string, sub_str)

def check(s2, s1):
    if (s2.count(s1) > 0):
        print("YES")
    else:
        print("NO")
 
 
s2 = "A geek in need is a geek indeed"
s1 = "geeks"
check(s2, s1)


