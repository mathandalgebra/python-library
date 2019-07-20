#################################################
# Hw2
# Your andrewID:
# Your section: 
#################################################

import cs112_f18_week2_linter
import math

def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

#################################################
# Hw2 problems
#################################################


### Part 1: Group sessions [10pts]
# Attendance will be graded by the TAs! Nothing needed here!

### Part 2: Piazza post [5pts]
# Participation will be graded by the TAs! Nothing needed here!

### Part 3: Debugging code [10pts]
# NOTE: remove the triple-quotes before you start debugging. ###

def countEvenDigits(n):
    if n < 0:
        return countEvenDigits(-n)
    elif n == 0:
        return 1
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n = n // 10
    return count
    
def factorial(n):
    if n==0:
        return 1
    result=n
    for smallerInteger in range(1,n):
        result=result*smallerInteger
    return result
    
def intHasRepeatedDigits(n):
    if n>0:
        remainingDigits=n
    else:
        remainingDigits = -n
    while remainingDigits//10>0:
        firstDigit=remainingDigits%10
        tensDigit=(remainingDigits//10)%10
        if firstDigit==tensDigit:
            print(n,"has repeated digits!")
            return True
        remainingDigits=remainingDigits//10
    print(n,"has no repeated digits...")
    return False
    
### Part 4: Testing: Equidigal! [5pts]
    
# def testIsEquidigital(isEquidigital):
#     count = 0
#     count2 = 0
#     
#     for num in range(2, isEquidigital):
#         if(isEquidigital % num == 0):
#             count += 1
#     
#     while(isEquidigital > 0):
#         isEquidigital //= 10
#         count2 += 1
# 
#     if(count == count2):
#         return True
#     else:
#         return False

def testIsEquidigital(isEquidigital):
    assert(isEquidigital(10) == True)
    assert(isEquidigital(0) == False)
    assert(isEquidigital(2) == False)
    assert(isEquidigital(2.25) == False)
        
    
### Part 5: Code writing: Happy Primes ^____^ [15pts]

def sumOfSquaresOfDigits(n):
    number  =0
    while(n > 0):
        n = n % 10
        print(n)
        number = number + (n ** 2)
        print(number)
        n = n // 10
    return number


def isHappyNumber(x):
    cycle = 0
    if(x < 1):      
        return False
    while(x >= 1 and cycle <= 50):
        if (x == 1):
            return True
        if (x == 4):
            return False
        x = sumOfSquaresOfDigits(x)
        cycle += 1
    return False
    

def nthHappyPrime(n):
    counting = 0
    guess = 0
    while(counting <= n):
        guess += 1
        if(isPrime(guess) and isHappyNumber(guess)):
            counting += 1
    return guess

###Part 6: Code writing: Number triangles [5pts]

def printNumberTriangle(n):
    count = 0
    number = 0
    for num in range(0,n):
        count += 1
        number = number + (10**num) * count
        print(number)        


###Part 7: COLLABORATIVE Code writing: Two player eggs game [10pts]
#Collaborators: [List here]
def twoPlayerEggsGame():
    print("Let's play the egg game! There are 21 eggs left.")
    
    player1 = 21
    turn = 1 
    
    while(player1 > 0):
        if(turn == 1):
            x = input("Player 1, how many eggs will you remove?")
            if(x == "1" or x == "2" or x == "3"):
                x = int(x)
                player1 = player1 - x
                turn = turn + 1
                if(player1 <= 0):
                    print("Player 1 took the last egg! Player 2 wins!")
                    break
                if(player1 == 1):
                    print("There is 1 egg left.")
                else:
                    print("There are",player1,"eggs left.")
                
            else:
                print("Each player must take either 1, 2, or 3 eggs!")
                turn = 1
            
        if(turn == 2):    
            y = input("Player 2, how many eggs will you remove?")
            if(y == "1" or y == "2" or y == "3"):
                y = int(y)
                player1 = player1 - y
                turn = turn - 1 
                if(player1 <= 0):
                    print("Player 2 took the last egg! Player 1 wins!")
                    break
                if(player1 == 1):
                    print("There is 1 egg left.")
                else:
                    print("There are",player1,"eggs left.")
            else:
                print("Each player must take either 1, 2, or 3 eggs!")
                turn = 2
           
            
    
    
###Part 8: COLLABORATIVE Code writing: One player eggs game [10pts]
#NOTE:  If you get an EOF error when testing, it probably means
#       that your code is calling input() but the test case has 
#       already provided its entire input string!  In other
#       words, the test expects the game to be over, but your code
#       is asking for more moves.  

def eggBot(n):
    if(n == 3):
        return 1
    if(n == 2):
        return 2
    if(n == 1):
        return 3 
    

def onePlayerEggsGame():
    print("Let's play the egg game! There are 21 eggs left.")
    
    player1 = 21
    turn = 1 
    
    while(player1 > 0):
        if(turn == 1):
            x = input("Player 1, how many eggs will you remove?")
            if(x == "1" or x == "2" or x == "3"):
                x = int(x)
                player1 = player1 - x
                turn = turn + 1
                if(player1 <= 0):
                    print("Player 1 took the last egg! The computer wins!")
                    break
                print("There are",player1,"eggs left.")
            else:
                print("Each player must take either 1, 2, or 3 eggs!")
                turn = 1
        
        if(turn == 2):    
            y = eggBot(x)
            if(y == 1):
                print("The computer takes 1 egg.")
            if(y == 2 or y == 3):
                print("The computer takes",y,"eggs.")
            player1 = player1 - y
            turn = turn - 1
            if(player1 <= 0):
                print("Player 2 took the last egg! Player 1 wins!")
                break
            if(player1 == 1):
                print("There is 1 egg left.")
            else:
                print("There are",player1,"eggs left.")
            
    
###Part 9: COLLABORATIVE Code writing: nth Kaprekar number [15pts]
def countDigit(n):
    count = 0
    while(n > 0):
        n = n // 10
        count += 1
    return count

def isKaprekarNumber(n):
    square = n ** 2
    numberDigit = countDigit(square)
    if(n == 1):
        return True
    if(n == 9):
        return True
    for i in range(1,numberDigit - 1):
        if(n == (square // (10 ** (numberDigit-i)) + square % (10 ** (numberDigit-i))) and
        square % (10 ** (numberDigit-i)) != 0):
            return True
    return False
    
def nthKaprekarNumber(k):
    count = 0
    value = -1
    while(count <= k):
        value += 1
        if(isKaprekarNumber(value)):
            count += 1
    return value

###Part 10: Code writing: Nearest Kaprekar number [15pts]
def roundHalfUp(n):
    x = n * 10 % 10
    if(x >= 5):
        return math.ceil(n)
    else:
        return math.floor(n)
        
def nearestKaprekarNumber(n):
    if(n <= 2):
        return 1
    if(isKaprekarNumber(n) == True):
        return n
    a = math.floor(n)
    b = math.ceil(n)
    while(isKaprekarNumber(n) == False):
        a = a - 1
        b = b + 1
        if(isKaprekarNumber(a) == True and isKaprekarNumber(b) == True):
            if(abs(a-n) > abs(b-n)):
                return b
            if(abs(a-n) < abs(b-n)):
                return a
            if(abs(a-n) == abs(b-n)):
                return a
        if(isKaprekarNumber(a) == True):
            return a
        if(isKaprekarNumber(b) == True):
            return b
    
###OPTIONAL BONUS: Fun with Generators[3pts; 1pt each]

def squaresGenerator():
    return
    
def nswGenerator():
    return
    
def nswPrimesGenerator():
    return

#################################################
# Hw2 Test Functions
# ignore_rest
#################################################
    
def testCountEvenDigits():
    print("Testing countEvenDigits()...", end="")
    assert(countEvenDigits(5) == 0)
    assert(countEvenDigits(8) == 1)
    assert(countEvenDigits(83) == 1)
    assert(countEvenDigits(94) == 1)
    assert(countEvenDigits(1234567890) == 5)
    assert(countEvenDigits(0) == 1)
    print("Passed!")
    
def testFactorial():
    print("Testing factorial()...", end="")
    assert(factorial(2) == 2)
    assert(factorial(4) == 24)
    assert(factorial(6) == 720)
    assert(factorial(0) == 1)
    print("Passed!")
    
def testIntHasRepeatedDigits():
    print("Testing intHasRepeatedDigits()...", end="")
    assert(intHasRepeatedDigits(0) == False)
    assert(intHasRepeatedDigits(5) == False)
    assert(intHasRepeatedDigits(44) == True)
    assert(intHasRepeatedDigits(-6) == False)
    assert(intHasRepeatedDigits(-33) == True)
    assert(intHasRepeatedDigits(124456) == True)
    assert(intHasRepeatedDigits(-124456) == True)
    assert(intHasRepeatedDigits(124) == False)
    assert(intHasRepeatedDigits(-124) == False)
    print("Passed!")
    
def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

def isEquidigital1(n):
    if n < 2:
        return False
    digitsInN = len(str(n))
    digitsInFactors = 0
    for factor in range(2, n):
        if n % factor == 0 and isPrime(factor):
            digitsInFactors += len(str(factor))
    return digitsInN == digitsInFactors


def digitCount2(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def isEquidigital2(n):
    numDigits = digitCount2(n)
    primeFactorDigitCount = 0
    for potentialFactor in range(2,n+1):
        if n % potentialFactor == 0:
            if isPrime(potentialFactor):
                primeFactorDigitCount += digitCount2(potentialFactor)
    return numDigits == primeFactorDigitCount


def digitCount3(n):
    return len(str(n))

def isEquidigital3(n):
    if n < 3:   return False
    numDigits = digitCount3(n)
    primeDigits = 0

    for factor in range(2, n):
        if n % factor == 0 and isPrime(factor):
            primeDigits += digitCount3(factor)
    if isPrime(n):
        primeDigits += digitCount3(n)

    return primeDigits - numDigits <= 1


def digitCount4(n):
    n = abs(n)
    count = 1
    while(n > 9):
        count += 1
        n //= 10
    return count

def isEquidigital4(n):
    factorDigits = 0
    for factor in range(2, n + 1):
        if(n%factor == 0 and isPrime(factor)):
            factorDigits += digitCount4(factor)
    return factorDigits == digitCount4(n)

def testTestIsEquidigital():
    print("Testing testIsEquidigital()...")

    successCount = 0
    try:
        testIsEquidigital(isEquidigital1)
        print("isEquidigital1: passed")
        successCount += 1
    except:
        print("isEquidigital1: failed")

    try:
        testIsEquidigital(isEquidigital2)
        print("isEquidigital2: passed")
        successCount += 1
    except:
        print("isEquidigital2: failed")

    try:
        testIsEquidigital(isEquidigital3)
        print("isEquidigital3: passed")
        successCount += 1
    except:
        print("isEquidigital3: failed")

    try:
        testIsEquidigital(isEquidigital4)
        print("isEquidigital4: passed")
        successCount += 1
    except:
        print("isEquidigital4: failed")

    # Only one isEquidigital function should pass the test cases, and it should
    # be the correct one!
    assert(successCount == 1)
    print("Passed!")


def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    print('Passed!')
    

def testPrintNumberTriangle():
    import sys, io
    print('Testing printNumberTriangle()... ', end='')
    tmpOut = sys.stdout

    oneOutput = io.StringIO()
    sys.stdout = oneOutput
    printNumberTriangle(1)
    oneCheck = oneOutput.getvalue()

    fourOutput = io.StringIO()
    sys.stdout = fourOutput
    printNumberTriangle(4)
    fourCheck = fourOutput.getvalue()

    sevenOutput = io.StringIO()
    sys.stdout = sevenOutput
    printNumberTriangle(7)
    sevenCheck = sevenOutput.getvalue()

    sys.stdout = tmpOut

    assert(oneCheck == "1\n")
    assert(fourCheck == "1\n21\n321\n4321\n")
    assert(sevenCheck == "1\n21\n321\n4321\n54321\n654321\n7654321\n")
    print('Passed!')


def ioTestTwoPlayer(test):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    twoPlayerEggsGame()
    return myOut.getvalue()

def testTwoPlayerEggsGame():
    import sys
    print("Testing twoPlayerEggsGame()...", end="")
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    threesTest = ioTestTwoPlayer("3\n3\n3\n3\n3\n3\n3\n")
    countingTest = ioTestTwoPlayer("1\n2\n3\n1\n2\n3\n1\n2\n3\n1\n5\n2\n")
    altCountingTest = ioTestTwoPlayer("EGGS!\n1\n3\n2\n2\n3\n1\n1\n3\n2\n2\n3\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn

    assert(threesTest == "Let's play the egg game! There are 21 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 18 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 15 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 12 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 9 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 6 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 3 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "Player 1 took the last egg! Player 2 wins!\n")
            
    assert(countingTest == "Let's play the egg game! There are 21 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 20 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 18 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 15 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 14 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 12 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 9 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 8 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 6 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 3 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 2 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "Each player must take either 1, 2, or 3 eggs!\n"+\
            "Player 1, how many eggs will you remove?"+\
            "Player 1 took the last egg! Player 2 wins!\n")
            
    assert(altCountingTest == "Let's play the egg game! There are 21 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "Each player must take either 1, 2, or 3 eggs!\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 20 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 17 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 15 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 13 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 10 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 9 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 8 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There are 5 eggs left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "There are 3 eggs left.\n"+\
            "Player 2, how many eggs will you remove?"+\
            "There is 1 egg left.\n"+\
            "Player 1, how many eggs will you remove?"+\
            "Player 1 took the last egg! Player 2 wins!\n")
    print("Passed!")
    

def ioTestOnePlayer(test):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    onePlayerEggsGame()
    return myOut.getvalue()

def testIfComputerWins(s):
    g=s.split('\n')
    assert(g[-2]=="Player 1, how many eggs will you remove?Player 1 took the last egg! Player 2 wins!" 
        or g[-2]=="Player 1, how many eggs will you remove?Player 1 took the last egg! The computer wins!")
    assert(g[-3]=="There is 1 egg left.")
    return 

def testOnePlayerEggsGame():
    import sys
    print("Testing onePlayerEggsGame()...", end="")
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    threesTest = ioTestOnePlayer("3\n3\n3\n3\n3\n3\n")
    countingTest = ioTestOnePlayer("1\n2\n3\n1\n2\n3\n")
    altCountingTest = ioTestOnePlayer("EGGS!\n1\n3\n2\n2\n3\n1\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn

    testIfComputerWins(threesTest)
    testIfComputerWins(countingTest)
    testIfComputerWins(altCountingTest)
    print("Passed!")

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")
    
def testSquaresGenerator():
    print("Testing squaresGenerator()...")
    # This time, we'll test twice.  First with next(),
    # then with a "for" loop
    g = squaresGenerator()
    assert(next(g) == 1)
    assert(next(g) == 4)
    assert(next(g) == 9)
    assert(next(g) == 16)

    # ok, now with a for loop.
    squares = ""
    for square in squaresGenerator():
        # we'll check the concatenation of the str's,
        # since we cannot use lists on this hw!
        if (squares != ""): squares += ", "
        squares += str(square)
        if (square >= 100): break
    assert(squares == "1, 4, 9, 16, 25, 36, 49, 64, 81, 100"
          )
    print("Passed!")


def testNswGenerator():
    print("Testing nswGenerator()...")
    nswNumbers = ""
    for nswNumber in nswGenerator():
        # we'll check the concatenation of the str's,
        # since we cannot use lists on this hw!
        if (nswNumbers != ""): nswNumbers += ", "
        nswNumbers += str(nswNumber)
        if (nswNumber >= 152139002499): break
    # from: http://oeis.org/A001333
    assert(nswNumbers == "1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119, "
                         "19601, 47321, 114243, 275807, 665857, 1607521, 3880899, "
                         "9369319, 22619537, 54608393, 131836323, 318281039, "
                         "768398401, 1855077841, 4478554083, 10812186007, "
                         "26102926097, 63018038201, 152139002499"
          )
    print("Passed!")
    
def testNswPrimesGenerator():
    print("Testing nswPrimesGenerator()...")
    nswPrimes = ""
    for nswPrime in nswPrimesGenerator():
        # again, we'll check the concatenation of the str's,
        # since we cannot use lists on this hw!
        if (nswPrimes != ""): nswPrimes += ", "
        nswPrimes += str(nswPrime)
        if (nswPrime >= 63018038201): break
    # from: http://oeis.org/A088165
    # print nswPrimes
    assert(nswPrimes == "7, 41, 239, 9369319, 63018038201"
                        #"489133282872437279"
          )
    print("Passed!")

#################################################
# Hw2 Main
#################################################

def testAll():
    # testCountEvenDigits()
    # testFactorial()
    # testIntHasRepeatedDigits()
    testTestIsEquidigital()
    testSumOfSquaresOfDigits()
    # testIsHappyNumber()
    testNthHappyPrime()
    testPrintNumberTriangle()
    testTwoPlayerEggsGame()
    testOnePlayerEggsGame()
    testNthKaprekarNumber()
    testNearestKaprekarNumber()
    testSquaresGenerator()
    testNswGenerator()
    testNswPrimesGenerator()
    

def main():
    cs112_f18_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()