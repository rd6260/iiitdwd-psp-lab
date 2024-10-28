def bin2dec():
   bin = int(input("enter the number u want to conv from binary to decimal: "))
   str_bin = str(bin)
   len_bin = len(str_bin)
   n = int(len_bin)
   a = 0
   b = 0
   x = str_bin[::-1]
   for i in range (0, len_bin):
      a = (2**(i))*int(x[i])
      b += a
   print(b)
