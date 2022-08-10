#inputting values

print("Enter the Dividend")
dividend = int(input())

print("Enter the Divisor")
divisor = int(input())

print("Enter the number of Digits")
digit = int(input())

#defining function

def give_remainder_dict(dividend, divisor, digit):

    #creating the format for the format function
    decimalformat = "."+str(digit+1)+"f"

    #finding the whole value i.e after and before decimal.
    #format function -> (22/7,".10f") for first example.
    ans = format(dividend/divisor,decimalformat)
    strans = str(ans)
    # print(ans)
    #taking only the digits after decimal in string format

    decimalvalues = strans.split('.')[1]
    #excluding the last digit as the total length was taken digit+1, to avoid rounding in the format function
    decimalvalues = decimalvalues[:-1]
    
    #filling the count of each digit in the dictionary.
    #initialising the dictionary.
    values = {}
    for a in range(0,10):
        values[a] = 0

    for a in decimalvalues:
        values[int(a)] += 1

    print(values)

#calling the function with the given values.

give_remainder_dict(dividend, divisor, digit)    