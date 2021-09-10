# DEFINE ROMAN TO INT FUNCION:
def roman_to_int(sample):

    # DEFINE THE ROMAN NUMBERS
    dictRoman = {}
    dictRoman["I"] = 1
    dictRoman["V"] = 5
    dictRoman["X"] = 10
    dictRoman["L"] = 50
    dictRoman["C"] = 100
    dictRoman["D"] = 500
    dictRoman["M"] = 1000

    i = 0
    ans = 0
    for i in range(len(sample)):
        value = dictRoman[sample[i]]
        if i+1 < len(sample):
            if value >= dictRoman[sample[i+1]]:
                ans = ans + value
            else:
                ans = ans - value
        else:
            ans = ans + value
    return ans


# DEFINE INT TO FUNCION:
def int_to_roman(sample):
    # DEFINE THE ROMAN NUMBERS
    dictRoman = {}
    dictRoman["M"] = 1000
    dictRoman["CM"] = 900
    dictRoman["D"] = 500
    dictRoman["CD"] = 400
    dictRoman["C"] = 100
    dictRoman["XC"] = 90
    dictRoman["L"] = 50
    dictRoman["XL"] = 40
    dictRoman["X"] = 10
    dictRoman["IX"] = 9
    dictRoman["V"] = 5
    dictRoman["IV"] = 4
    dictRoman["I"] = 1

    answRoman = ""
    number = sample
    for roman in dictRoman.keys():
        if number > 0:
            quotient = number // dictRoman[roman]
            if quotient == 0:
                continue

            if roman not in ["D", "L", "V"]:
                answRoman = answRoman + roman * quotient
                number = number - dictRoman[roman] * quotient
            else:
                answRoman = answRoman + roman
                number = number - dictRoman[roman]
        else:
            break

    return answRoman

def main():

    # READ TEXT
    file = open("/Users/alfredosone/Desktop/Alfredo/Kellogg/Fall Pre-term 2021/AI Leaders/Python Scripts/python_-hackathon_group_13/roman.txt", "r")
    numbers = file.read().split("\n")

    # TRANSFORM NUMBERS
    for initialRoman in numbers:
        initialLength   = len(initialRoman)
        intRoman        = roman_to_int(initialRoman)
        effectiveRoman  = int_to_roman(intRoman)
        finalLenght = len(effectiveRoman)

        print("Input: " + initialRoman + " || Output: " + effectiveRoman)
        print("We saved " + str(initialLength-finalLenght) + " characters.")

main()
