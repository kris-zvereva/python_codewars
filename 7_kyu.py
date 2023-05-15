'''
Friend or Foe?
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
'''

def friend(x):
    friend = []
    for i in x:
        if len(i) == 4:
            friend.append(i)
    return friend 
  

'''
Sum of two lowest positive integers
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


'''
Isograms
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)
"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''

def is_isogram(string):
    return len(string) == len(set(string.lower()))


'''
Reverse words
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    list=[]
    for i in text.split(' '):
        list.append(i[::-1])
    return ' '.join(list)


'''
Small enough? - Beginner
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. 
If they are, return true. Else, return false.
You can assume all values in the array are numbers.
'''

def small_enough(array, limit):
    return max(array)<=limit
  

'''
Digit*Digit
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
Note: The function accepts an integer and returns an integer.
Happy Coding!
'''

def square_digits(num):
    r = ''
    for l in str(num):
        r = r + str((int(l))**2)
    return int(r) 


'''
String ends with?
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

def solution(string, ending):
        return string.endswith(ending)


'''
Exes and Ohs
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. 
The string can contain any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def xo(s):
    a = s.lower()
    return a.count('x') == a.count('o')


'''
Heron's formula
Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).
Output should have 2 digits precision.
'''

def heron(a, b, c):
    s = (a + b + c)/2
    form = (s * (s - a)*(s - b)*(s - c))** 0.5
    return round(form, 2)

  

'''
Get the Middle Character
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"

#Input
A word (string) of length 0 < str < 1000 
(In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). 
You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output
The middle character(s) of the word represented as a string.
'''

def get_middle(s):
    if len(s)%2==0:
        i = int(len(s)/2)-1
        return s[i]+s[i+1]
    else:
        return s[int(len(s)/2)]

      
      
