#Convert numbers 1 to 99 into words

zero_nineteen = ['zero', 'one', 'two', 'three', 'four', 'five',
                 'six', 'seven', 'eight', 'nine', 'ten',
                 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                 'sixteen', 'seventeen', 'eighteen', 'nineteen']
zero_ninety   = ['zero', 'ten', 'twenty', 'thirty', 'fourty',
                'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def number(n):
#If the number is between 0 and 19 (inclusive),zero_nineteen list index
    if n>=0 and n <= 19:
        return (zero_nineteen[n])
#If the number is between 0 and 19 (inclusive),zero_ninety list index
    elif n >= 20 and n <= 99:
        if not n % 10: #if the number is a multiple of 10
            return (zero_ninety[n//10])
        return (zero_ninety[n//10]+" "+zero_nineteen[n % 10])
    else:
        print("Opps!!! Please enter a number between 0 and 99")

n = int(input("Please enter a number between 0 and 99: "))
print(n, number(n), sep="---->>> ")