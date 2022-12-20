#Recursive Conversion Function
def biConv(binnum, dec):
    #So long as their a remainder we will continue to divide by 2
    if dec != 0:
        x = dec%2
        binnum.append(x)
        #Recursion
        biConv(binnum, dec//2)
    #Add extra 0 to append if not base 4
    if (len(binnum)%4 != 0):
        binnum.append(0)
    return binnum
    
#Binary Conversion
#Prompt User for input
print("\nDecimal to Binary")
dec = input('Please provide a number to be converted\n')
binnum = []

#Run recursive conversion function
binnum = (biConv(binnum, int(dec)))

#Reverse array
binnum.reverse()


final = ""

#Concatenate into string
for x in binnum:
    final += str(x)

#Print String
print("Binary: {}".format(final))
