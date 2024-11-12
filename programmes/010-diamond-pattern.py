
def diamond_patt():
    '''   *
         *
        ***
       ***'''
    n = int(input("enter the rows in which diamond should be made: "))
    if n%2 == 0:
        print("no diamond pattern can be made in the given number of rows")
    else:
        for j in range (0,n//2):
                print(" "*(n//2-(j)), end = "")
                print(""((2*j)+1))
        for i in range ((n//2)+1,(n//2)+2):
            print("*"*n)
        for j in range (0,n//2):
                print(" "*(j+1), end = "")
                print(""(n-((2*j)+2)))
