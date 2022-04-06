# Costy
isPoz_Neg = 'NaN'
isEven_Odd = 'NaN'

myNum = int(input('Please enter your number: '))
rem = myNum % 2
if (myNum == 0):
    print('Your number is ZERO')
if (myNum > 0):
    isPoz_Neg = 'Positive'
if (myNum < 0):
    isPoz_Neg = 'Negative'
if (rem == 0):
    isEven_Odd = 'Even'
if (rem == 1):
    isEven_Odd = 'Odd'
if (myNum != 0):
    print('Your number is', isPoz_Neg, 'and', isEven_Odd)

# Intended
myNumber = int(input('Please enter your number: '))
remainder = myNumber % 2
if (myNumber > 0 and remainder == 0):
    print('Your number is Positive and Even')
if(myNumber < 0 and remainder == 0):
    print('Your number is Negative and Even')
if (myNumber > 0 and remainder == 1):
    print('Your number is Positive and Odd')
if (myNumber < 0 and remainder == 1):
    print('Your number is Negative and Odd')
if(myNumber == 0):
    print('Your number is ZERO')
