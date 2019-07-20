

import math
import string
import copy


"""
Fill in your answers to the List Function Table problem here.

c = a + b non-destructive
a += b    destructive
a.append(x) destructive
a.insert(0, x)  destructive
b = a[:i] + [x] + a[i:]  non-destructive
a.remove(x)  destructive
a.pop(0)     destructive
b = a * 3    destructive
a.reverse()  destructive
reversed(a)  non-destructive
a.sort()    destructive
sorted(a)   non-destructive
copy.copy(a) non-destructive
"""

def lookAndSay(list):
    count = 1
    newList = []
    if(list == []):
        return []
    for index in range(len(list)-1):
        #if the two adjacent one are the same, then increase count by one
        if(list[index] == list[index + 1]):
            count += 1
        #if the two adjacent lines are not equal, then put them into a tuple
        if(list[index] != list[index + 1]):
            listElement = [count,list[index]]
            t = tuple(listElement)
            newList.append(t)
            count = 1
    listElement = [count, list[len(list)-1]]
    t = tuple(listElement)
    newList.append(t)
    return newList



def inverseLookAndSay(list):
    newList = []
    #list[index] refers to that specific tuple,list[index][1] means the second element of the tuple
    for index in range(len(list)):
        newList = newList + [list[index][1]] * list[index][0]
    return newList



orderList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
             "q","r","s","t","u","v","w","x","y","z"]
             
def bestScrabbleScore(dictionary, letterScores, hand):
    ultimateList = sumOfScore(newDictionary(dictionary,hand),letterScores)
    max = 0
    subEmpty = []
    ultimateEmpty = []
    count = 0
    if(newDictionary(dictionary,hand) == []):
        return None
    for item in ultimateList:
        if(item > max):
            max = item
    for i in range(len(ultimateList)):
        if(ultimateList[i] == max):
            count += 1
            position = ultimateList.index(ultimateList[i],i)
            subEmpty.append(newDictionary(dictionary,hand)[position])
    if(count == 1):
        ultimateEmpty = ultimateEmpty + subEmpty + [max]
    if(count > 1):
        ultimateEmpty.append(subEmpty)
        ultimateEmpty.append(max)
        
    t = tuple(ultimateEmpty)
    return t
    
def sumOfScore(newList, letterScores):
    sum = 0
    newerList = []
    for item in newList:
        for character in item:
            position = orderList.index(character)
            number = letterScores[position]
            sum += number
        newerList.append(sum)
        sum = 0
    return newerList
    
def newDictionary(dictionary, hand):
    newList = []
    for item in dictionary:
        if(isWordTrue(item,hand) == True):
            newList.append(item)
        else:
            continue
            
    return newList    

def isWordTrue(s1,hand):
    for character in s1:
        if(s1.count(character) <= hand.count(character)):
            continue
        else:
            return False
    return True


def runSimpleProgram(program, args):
    return 42


from tkinter import *



def drawStar(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    #Replace this next line with your code!
    magnifyRate = 3/8 
    newList = []
    for i in range(numPoints):
        #the angle of the points on the outside circle
        outerAngle = math.radians(90) + i * math.radians(360 / numPoints)
        innerAngle = math.radians(90) + math.radians(360/(2 * numPoints)) + i * math.radians(360 / numPoints)
        xOuterPoint = centerX + (diameter / 2) * math.cos(outerAngle)
        yOuterPoint = centerY - (diameter / 2) * math.sin(outerAngle)
        xInnerPoint = centerX + (diameter / 2 * magnifyRate) * math.cos(innerAngle)
        yInnerPoint = centerY - (diameter / 2 * magnifyRate) * math.sin(innerAngle)
        newList = newList + [xOuterPoint, yOuterPoint,xInnerPoint,yInnerPoint]
    canvas.create_polygon(newList,fill = color)
    root.mainloop()
  



def drawCircle(canvas, x, y, width, color, min_width=1, rate=2/3):

    while width >= min_width:
        canvas.create_oval(x, y, x + width, y + width, fill=color)
        x += width*(1-rate)*0.5
        y += width*(1-rate)*0.5
        width *= rate



def drawCirclePattern(n, winWidth=500, winHeight=500):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    canvas.create_rectangle(0,0,winWidth,winHeight,fill="aqua")
    radius = 25
    place = []
    for r_index in range(n):
        place.append([])
        for c_index in range(n):
            place[-1].append(True)

    for r_index in range(n):
        red_start_column = ((r_index-1)//4+1)*4 - r_index
        for c_index in range(red_start_column, n, 4):
            x, y = radius*2*c_index, radius*2*r_index
            drawCircle(canvas, x, y, 2 * radius, "red")
            place[r_index][c_index] = False
        if r_index % 3 == 0:
            for c_index in range(n):
                if place[r_index][c_index]:
                    x, y = radius * 2 * c_index, radius * 2 * r_index
                    drawCircle(canvas, x, y, 2 * radius, "green")
                    place[r_index][c_index] = False
        for c_index in range(1, n, 2):
            if place[r_index][c_index]:
                x, y = radius * 2 * c_index, radius * 2 * r_index
                drawCircle(canvas, x, y, 2 * radius, "yellow")
                place[r_index][c_index] = False
        for c_index in range(n):
            if place[r_index][c_index]:
                x, y = radius * 2 * c_index, radius * 2 * r_index
                drawCircle(canvas, x, y, 2 * radius, "blue")
                place[r_index][c_index] = False
                       
    root.mainloop()


def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    command = program.split("\n")

    line_width = 3
    start_x, start_y = 100, 300
    angle = 0
    color = "none"

    for line in command:
        if len(line) == 0:
            continue
        values = line.split()
        if values[0] == 'color':
            color = values[1]
        elif values[0] == 'left':
            angle -= (int(values[1])/180)*math.pi
        elif values[0] == 'right':
            angle += (int(values[1])/180)*math.pi
        elif values[0] == 'move':

            length = int(values[1])
            end_x = start_x + length*math.cos(angle)
            end_y = start_y + length*math.sin(angle)
            if color != "none":
                canvas.create_line(start_x, start_y, end_x, end_y,
                                   fill=color, width=line_width)
            start_x = end_x
            start_y = end_y
                       
    root.mainloop()


def drawNiceRobot(winWidth=500, winHeight=500):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    #Replace this next line with your code!
    canvas.create_text(winWidth/2, winHeight/2,
                       text="return 42", font="Arial 20 bold")
                       
    root.mainloop()



def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")


def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStar(250, 250, 500, 5, "gold")
    drawStar(300, 400, 100, 4, "blue")
    drawStar(300, 200, 300, 9, "red")
    print("Done!")
    
def testDrawCirclePattern():
    print("Testing drawCirclePattern()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawCirclePattern(5)
    drawCirclePattern(10)
    print("Done!")
    
def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

def testDrawNiceRobot():
    print("Testing drawNiceRobot()...")
    print("Since this is graphics, this test is not interactive.")
    print("Check out this nice robot!")
    drawNiceRobot()
    print("Done!")


def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testBestScrabbleScore()
    testDrawStar()
    testDrawCirclePattern()
    testRunSimpleTortoiseProgram()
    testDrawNiceRobot()
    testRunSimpleProgram()

def main():
    testAll()

if __name__ == '__main__':
    main()
