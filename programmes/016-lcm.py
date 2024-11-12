def hcf(a, b):
    x = 1
    highest_common_factor = 1

    while x <= a and x <= b:
        if (a % x == 0) and (b % x == 0):
            highest_common_factor = x

        x += 1


    return highest_common_factor


def lcm(num1,num2):
    a = (num1*num2) / hcf(num1,num2)
    print(f"The LCM of {num1}, {num2} is {a}")



