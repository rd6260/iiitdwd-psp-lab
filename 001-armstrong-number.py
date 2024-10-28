
num=int(input("enter input\n"))
num_copy=num
leng=0

while num>0:
    leng+=1
    num = num//10
print(leng)
num=num_copy
chek=0

for i in range(0,leng):
    chek += (num%10)**leng
    num = num//10
    print(chek)

if num_copy==chek:
    print("is armstrong")
else:
    print("is not armstrong")

