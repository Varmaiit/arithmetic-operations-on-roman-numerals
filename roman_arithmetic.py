## python 2.7

import unittest
import operator
from utils import print_test_time_elapsed


def romanToInt(roman):
    romanDict = { "I" : 1, "V" : 5, "X" : 10,"L" : 50 , "C" : 100, "D" : 500, "M" : 1000 }
    newlist =[]
    newlist[:0] = roman
    # defining intial previous value = 0 
    preValue = 0
    result = 0
    for item in reversed(newlist):
        if romanDict[item] < preValue:
            result -= romanDict[item]
        else:
            result += romanDict[item]
        preValue = romanDict[item]
    return result

def intToRoman(integer):
    romanDict = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
    resultString = ""
    for romanValue, romanNumber in sorted(romanDict.items(), reverse=True):
        # print "romanValue : %s, romanNumber: %s" % (romanValue, romanNumber) 
        while integer >= romanValue:
            # print "number : %s" % number
            # print "value : %s" % value
            resultString += romanNumber
            # print "result : %s" % result
            integer -= romanValue
            # print "number : %s" % number
    return resultString


def mathOPeration(num1, oper, num2):
    operatorsDict = {'+': operator.add, '-':operator.sub, '/':operator.div, '*':operator.mul }
    return operatorsDict[oper](num1, num2)


def mathOPerationOnRoman(romanNum1, oper, romanNum2):
    # Convert roman to Integer
    romanNum1Value = romanToInt(romanNum1)
    romanNum2Value = romanToInt(romanNum2)

    # Perform mathetical operation
    resultValue  = mathOPeration(romanNum1Value, oper, romanNum2Value)
    # print resultValue

    # check whether result is integer
    if (type(resultValue) is int) and (resultValue > 0):
        return intToRoman(resultValue)
    else:
        return "Operation for this combination of Roman Numbers is not possible"



class TestRomanArithmetic(unittest.TestCase):
    def setUp(self):
        self.romanNumbers = [(1, 'I'), (4, 'IV'), (2, 'II'), (19, 'XIX'), (28, 'XXVIII'), (63, 'LXIII'), (235, 'CCXXXV'), (838, 'DCCCXXXVIII'), (1134, 'MCXXXIV')]
        self.romanArithmetic = [('XL', '+', 'X', 'L'), ('C','-', 'I', 'XCIX'), ('C','/', 'X' ,'X'), ('X','*','X','C'),
                                ('XV', '+', 'V', 'XX'), ('XV', '-', 'V', 'X'), ('XV', '/', 'V', 'III'), ('XV', '*', 'V', 'LXXV')]

    @print_test_time_elapsed
    def test_int_to_roman(self):
        for item in self.romanNumbers:
            self.assertEqual(intToRoman(item[0]), item[1])

    @print_test_time_elapsed
    def test_roman_to_int(self):
        for item in self.romanNumbers:
            self.assertEqual(romanToInt(item[1]), item[0])

    @print_test_time_elapsed
    def test_arithmetic_on_roman(self):
        for item in self.romanArithmetic:
            self.assertEqual(mathOPerationOnRoman(item[0],item[1], item[2]), item[3])
    
    

if __name__ == '__main__':
    roman1, operation, roman2 = [str(x) for x in raw_input("Please enter RomanNumber1 operation RomanNumber2 seperated by spaces (Eg: XL + X ) ").strip().split(' ')]
    print "Result: %s %s %s = %s" % (roman1, operation, roman2,mathOPerationOnRoman(roman1, operation, roman2))
    print "Also printing Unit test Results"
    unittest.main()