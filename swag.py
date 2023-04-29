ones = {'0' : 'zero', '1' : 'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', "10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen", "17":"Seventeen","18":"Eighteen","19":"Nineteen"}
tens = {"2":"Twenty","3":"Thirty","4":"Fourty","5":"Fifty","6":"Sixty", "7":"Seventy","8":"Eighty","9":"Ninety"}

tests = int(input())

for test in range(tests):
    final = ""
    intnum = int(input())
    changenum = 0

    def getword(num):
        ret = ""
        if num >= 100:
            ret += ones[str(num // 100)]
            num -= num // 100 *100
            ret += " hundred "
        if num >= 10:
            if num < 20:
                ret += ones[str(num)]
            else:
                ret += tens[str(num // 10)]
                num -= num // 10 *10
                ret += "-"
        if num < 10:
            ret += ones[str(num)]
            num -= num
        return ret

    if intnum == 0:
        final = "zero"
    else:

        if intnum < 0:
            final += "negative "
            intnum = abs(intnum)
        if intnum >= 1000000:
            final += getword(intnum // 1000000)
            intnum -= intnum // 1000000 *1000000
            final += " million "
        if intnum >= 1000:
            final += getword(intnum // 1000)
            intnum -= intnum // 1000 *1000
            final += " thousand "
        if intnum >= 100:
            final += getword(intnum // 100)
            intnum -= intnum // 100 *100
            final += " hundred "
        if intnum >= 10:
            if intnum < 20:
                final += ones[str(intnum)]
            else:
                final += tens[str(intnum // 10)]
                intnum -= intnum // 10 *10
                final += "-"
        if intnum < 10 and intnum >0:
            final += ones[str(intnum)]
            intnum -= intnum

        if(final[-1] == '-'):
            final = final[0:len(final) - 1]
    
    print(final.lower())