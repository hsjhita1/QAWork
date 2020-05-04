singleDigit = [ "", 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
doubleDigit = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
            'Eighteen', 'Nineteen', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 
            'Seventy', 'Eighty', 'Ninety']
hundredsList = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

def singleFunc(num):
    word = ''
    digit = singleDigit[int(num[0])]
    word = digit
    return word

def tenFunc(num) :
    word = ''
    if num[0] == '1':
        tens = doubleDigit[int(num[1])]
        word = tens
    elif num[0] != '1' and num[0] != '0':
        tens = doubleDigit[int(num[0])+8]
        digit = singleFunc(num[1])
        word = tens + " " + digit
    return word

def hundredFunc(num):
    word = ''
    ten = tenFunc(num[1:])
    hundred = hundredsList[int(num[0])]
    word = hundred + " Hundred " + ten
    if num[1] == 0:
        digit = singleDigit[int(num[2])]
        word = hundred + " Hundred " +  digit
    return word
    
def thousandFunc(num):
    word = ''
    if len(num) == 4:
        hundred = hundredFunc(num[1:])
        thousand = singleFunc(num[0])
        word = thousand + " Thousand " + hundred
    elif len(num) == 5:
        hundred = hundredFunc(num[2:])
        thousand = tenFunc(num[:2])
        word = thousand + " Thousand " + hundred
    elif len(num) == 6:
        hundred = hundredFunc(num[3:])
        thousand = hundredFunc(num[:3])
        word = thousand + " Thousand " + hundred
    return word

def millionFunc(num):
    word = ''
    if len(num) == 7:
        thousand = thousandFunc(num[1:])
        million = singleFunc(num[0])
        word = million + " Million " + thousand
    elif len(num) == 8:
        thousand = thousandFunc(num[2:])
        million = tenFunc(num[:2])
        word = million + " Million " + thousand
    elif len(num) == 9:
        thousand = thousandFunc(num[3:])
        million = hundredFunc(num[:3])
        word = million + " Million " + thousand
    return word

def billionFunc(num):
    word = ''
    if len(num) == 10:
        million = millionFunc(num[1:])
        billion = singleFunc(num[0])
        word = billion + " Billion " + million
    elif len(num) == 11:
        million = millionFunc(num[2:])
        billion = tenFunc(num[:2])
        word = billion + " Billion " + million
    elif len(num) == 12:
        million = millionFunc(num[3:])
        billion = hundredFunc(num[:3])
        word = billion + " Billion " + million

    return word

choice = int(input("\nEnter a number: "))
text = str(choice)
if choice == 0:
    number = 'Zero'
elif len(text) <= 1:
    number = singleFunc(text)
elif len(text) <= 2 and choice <=99:
    number = tenFunc(text)
elif len(text) <= 3:
    number = hundredFunc(text)
elif len(text) >= 4 and len(text) <=6:
    number = thousandFunc(text)
elif len(text) >= 7 and len(text) <= 9:
    number = millionFunc(text)
elif len(text) >=10 and len(text) <=12:
    number = billionFunc(text)

print(number)

