
import cs112_f18_week1_linter
import math


def syllabusAnswer():
    return """1:
2:
3:
4:
5: """

def codeDescriptionAnswer():
    return "Your answer here"

def rocAnswer():
    return 55

def isEvenPositiveInt(n):
    if(n % 2 == 0 and n > 0 and isinstance(n,int)):
        return False
    return True

def getTheCents(n):
    if(isinstance(n,int)):
        return 0
    elif(isinstance(n, float)):
        math.ceil(n * 100 % 100)
    else:
        return None
        
def playGuessingGame():
    print("Let's play a guessing game! Think of a type of pet.")
    x = input("Does it have fur?")
    if(x == "Yes"):
        y = input("Can you teach it to play fetch?")
        if(y == "Yes"):
            return "It's a dog! "
        if(y == "No"):
            return "It's a cat!"
    if(x == "No"):
        y = input("Can it swim?")
        if(y == "Yes"):
           return "It's a fish!"
        if(y == "No"):
           return "It's a bird!"

#### the following four functions go together ####

def lineIntersection(m1, b1, m2, b2):
    if(m1 == m2):
        return none
    return (b1 - b2) / (m1 - m2)

def distance(x1, y1, x2, y2):
    return ((x1 - x2)^2 + (y1 - y2)^2)^(1/2)

def triangleArea(s1, s2, s3):
    s = s1 + s2 + s3
    return (s * (s - s1) * (s - s2) * (s - s3))**(1/2)

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    return

#### the following two functions go together ####

def getKthDigit(n, k):
    return n // (10**k)%10 

def setKthDigit(n, k, d = 1):
    return n - getKthDigit(n,k) * (10 ** k) + d * (10 ** k)

#### colorBlender is a COLLABORATIVE problem ####

# Collaborators: 
def colorBlender(rgb1, rgb2, midpoints, n):
    return

#### bonusFindIntRootsOfCubic is a bonus problem, and therefore optional ####
    
def bonusFindIntRootsOfCubic(a, b, c, d):
    return

#################################################
# Hw1 Test Functions
# ignore_rest
#################################################

def testSyllabusAnswer():
    print("Your answer to the syllabus question is:")
    print(syllabusAnswer())
    print("The TAs will grade this later.")
    print()

def testCodeDescriptionAnswer():
    print("Your answer to the code description question is:")
    print(codeDescriptionAnswer())
    print("The TAs will grade this later.")
    print()

def roc(x):
    if type(x) != int:
        return False
    elif x <= 0:
        return False
    elif x % 100 == x:
        a = x // 10
        b = x % 10
        if a != b:
            return False
        return True
    else:
        return x == 42

def testRocAnswer():
    print("Testing rocAnswer()...", end="")
    answer = rocAnswer()
    assert(roc(answer) == True)
    print("Passed.")

def testIsEvenPositiveInt():
    print("Testing isEvenPositiveInt()... ", end="")
    assert(isEvenPositiveInt(4) == True)
    assert(isEvenPositiveInt(7) == False)
    assert(isEvenPositiveInt(-2) == False)
    assert(isEvenPositiveInt("6") == False)
    assert(isEvenPositiveInt(None) == False)
    assert(isEvenPositiveInt(8.0) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt(8) == True)
    assert(isEvenPositiveInt(22) == True)
    print("Passed.")

def testGetTheCents():
    print("Testing getTheCents()...", end="")
    assert(getTheCents(10.95) == 95)
    assert(getTheCents(0.25) == 25)
    assert(getTheCents(10.5) == 50)
    assert(getTheCents(4.0) == 0)
    assert(getTheCents(2) == 0)
    assert(getTheCents(3.299) == 30)
    assert(getTheCents(2.961) == 97)
    assert(getTheCents("money") == None)
    assert(getTheCents(None) == None)
    print("Passed.")

def ioTest(test):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    playGuessingGame()
    return myOut.getvalue()

def testPlayGuessingGame():
    import sys
    print("Testing playGuessingGame()...", end="")
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    dogTest = ioTest("Yes\nYes\n")
    catTest = ioTest("Yes\nNo\n")
    fishTest = ioTest("No\nYes\n")
    birdTest = ioTest("No\nNo\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn
    assert(dogTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can you teach it to play fetch?It's a dog!\n")
    assert(catTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can you teach it to play fetch?It's a cat!\n")
    assert(fishTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can it swim?It's a fish!\n")
    assert(birdTest == "Let's play a guessing game! Think of a type of pet.\n"+\
            "Does it have fur?Can it swim?It's a bird!\n")
    print("Passed.")

def testLineIntersection():
    import math
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(math.isclose(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(math.isclose(lineIntersection(10,0,-4,35), 2.5))
    print("Passed.")

def testDistance():
    import math
    print("Testing distance()...", end="")
    assert(math.isclose(distance(0, 0, 1, 1), 2**0.5))
    assert(math.isclose(distance(3, 3, -3, -3), 6*2**0.5))
    assert(math.isclose(distance(20, 20, 23, 24), 5))
    print("Passed.")

def testTriangleArea():
    import math
    print("Testing triangleArea()...", end="")
    assert(math.isclose(triangleArea(3,4,5), 6))
    assert(math.isclose(triangleArea(2**0.5, 1, 1), 0.5))
    assert(math.isclose(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed.")

def testThreeLinesArea():
    import math
    print("Testing threeLinesArea()...", end="")
    assert(math.isclose(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(math.isclose(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(math.isclose(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(math.isclose(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(math.isclose(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed.")

def testGetKthDigit():
    print("Testing getKthDigit()...", end="")
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print("Passed.")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    assert(setKthDigit(809, 0) == 800)
    print("Passed.")

def testColorBlender():
    print("Testing colorBlender()...", end="")
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print("Passed.")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    import math
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(math.isclose(m1, result1))
    assert(math.isclose(m2, result2))
    assert(math.isclose(m3, result3))

def testBonusFindIntRootsOfCubic():
    print("Testing bonusFindIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print("Passed.")

#################################################

#################################################

def testAll():
    testSyllabusAnswer()
    testCodeDescriptionAnswer()
    testRocAnswer()
    testIsEvenPositiveInt()
    testGetTheCents()
    testPlayGuessingGame()
    testLineIntersection()
    testDistance()
    testTriangleArea()
    testThreeLinesArea()
    testGetKthDigit()
    testSetKthDigit()
    testColorBlender()
    testBonusFindIntRootsOfCubic()

def main():
    
    cs112_f18_week1_linter.lint() # check style rules
    testAll()
    

if __name__ == '__main__':
    main()
