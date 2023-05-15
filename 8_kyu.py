'''
Basic Mathematical Operations
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
'''

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1+value2
    elif operator == "-":
        return value1-value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
     

'''
Calculate average
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
'''

def find_average(numbers):    
    return sum(numbers)/len(numbers)
  
  
'''
Simple multiplication
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
'''

def simple_multiplication(number) :
    if number % 2 == 0:
        number = number * 8
        return number
    else:
        number = number * 9
        return number
      

def simple_multiplication(number) :
   return number * 9 if number % 2 else number * 8
  
  
'''
Reversed sequence
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
'''

def reverse_seq(n):
    l = list(range(1, n+1))
    return l[:: -1]
  

'''
Calculate BMI
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    bm = weight / height **2
    if bm <= 18.5:
        return "Underweight"
    elif bm <= 25.0:
        return "Normal"
    elif bm <= 30.0:
        return "Overweight"
    else:
        return "Obese"


'''
You only need one - Beginner
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not.
'''

def check(seq, elem):
    return elem in seq

'''
Abbreviate a Two Word Name
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
patrick feeney => P.F
'''

def abbrev_name(name):
    a = name[0]
    b = name.find(' ')
    c = a+'.'+name[b+1]
    return c.upper()
  
  
'''
How good are you really?
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.
You receive an array with your peers' test scores. Now calculate the average and compare your score!
Return True if you're better, else False!
Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!
'''

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

  
'''
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'rock':
        return 'Player 2 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    elif p1 == 'paper' and p2 == 'scissors':
        return 'Player 2 won!'
    elif p1 == 'rock' and p2 == 'paper':
        return 'Player 2 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
      
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"      

  
'''
Is he gonna survive?
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! 
Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
Return true if yes, false otherwise :)
'''

def hero(bullets, dragons):
    return True if bullets / 2 >= dragons else False

  
'''
Are You Playing Banjo?
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.
'''

def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'

      
'''
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	                return
name equals owner	    'Hello boss'
otherwise	            'Hello guest'
'''

def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

