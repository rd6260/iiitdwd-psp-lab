def longest_common(l):
    str=[""]*(l)
    for i in range (0,l):
        str[i]=input()
    str=sorted(str, key=len)
    com_str=""
    for i in range(len(str[0])):
        check=str[0][i]
        for j in range(1,l):
            if(check!=str[j][i]):
                print(f"{com_str} is common")
                return
        com_str+=check
    print(f"{com_str} is common")
    return

while True:
    print("enter no of input strings")
    l=int(input())
    longest_common(l)




