#################################################
#################################################

import string

#################################################
#################################################



def rocAnswer():
    return "DAC\nBGk\tl"


def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
        print("bad case")
    if len(s1) == len(s2):
        for str in s1:
            one = 1
            count_matches_1= 0
            count_matches_2 = 0
            for i in range(len(s1)):
                if s1[i] == str:
                    count_matches_1 += one
            for i in range(len(s2)):
                if s2[i] == str:
                    count_matches_2 += one
            if count_matches_1 !=count_matches_2:
                return False
        return True


def applyCaesarCipher(message, shiftNum):
    word = message
    newWord = ""
    for letter in word:
        if(letter.isalpha()==False):
            newWord = newWord + letter
        else:
            letter = chr(ord(letter) + shiftNum)
            if(ord(letter) >= 97):
                if(ord(letter) > 122):
                    letter = chr(ord(letter) - 26)
            elif(ord(letter) >= 65):
                if(ord(letter) > 90):
                    letter = chr(ord(letter) - 26)
            newWord = newWord + letter
    return newWord


def readFile(path):
    with open(path, "rt") as f:
        return f.read()
        
def writeFile(path, content):
    with open(path, "wt") as f:
        f.write(contents)
        
def gradebookSummary(gradebookFilename):
    file = readFile(gradebookFilename)
    sum = 0
    count = 0
    empty = ""
    for line in file.splitlines():
        if(line.startswith("#") or line==("")):
            continue
        sum = 0
        count = 0
        for word in line.split(","):            
            if(word.isdigit()):
                number = int(word)
                count += 1
                sum += number
            else:
                if(word[0] == "-"):
                    number = int(word)
                    count += 1
                    sum += number
                else:
                    empty = empty + word + "\t"
        if(count > 0):
            average = "%0.2f" % (sum / count)
            usableAverage = str(average)
            empty = empty + usableAverage + "\n"
    empty = empty.strip()
    return empty 
                
print(gradebookSummary("hw3_files/small2.txt"))

def patternedMessage(message, pattern):
    newdrawing = ""
    start = 0
    message = message.replace(" ","")
    for i in pattern:
        if(i not in string.whitespace):
            newdrawing = newdrawing + message[start]
            start = (start + 1) % len(message)
        else:
            newdrawing = newdrawing + i
    return newdrawing



def greatestLetter(s):
    max = 0
    value = ""
    for character in s:
        if(character.isalpha() == True):
            character = character.lower()
            if(s.count(character) > max):
                max = s.count(character)
                value = character
            if(s.count(character) == max):
                if(ord(character) < ord(value)):
                    value = character
    return value

def testGreatestLetter():
    assert(greatestLetter("asdferwer") == "e")
    assert(greatestLetter("asDE234ferwer") == "e")
    
def mostFrequentLetters(s):
    s = s.lower()
    
    hopeString = ""
    for character in s:
        if(character.isalpha() == False):
            hopeString = hopeString + character.replace(character, "")
        else:
            hopeString = hopeString + character
            
    newString = ""
    while(hopeString != ""):
        newString = newString + greatestLetter(hopeString)
        hopeString = hopeString.replace(greatestLetter(hopeString),"")
    return newString

def longestCommonSubstring(first, second):
    m = []
    for j in range(len(first) + 1):
        m.append([])
        for i in range(len(second) + 1):
            m[-1].append(0)
    max_length = 0
    end = 0
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > max_length:
                    max_length = m[i + 1][j + 1]
                    end = i + 1
                elif m[i + 1][j + 1] == max_length and first[end - max_length:end] > first[i + 1 - max_length:i + 1]:
                    end = i + 1

    return first[end - max_length:end] 

def getEvalSteps(expr):
    return

import string
def roc(s):
    assert(type(s) == str)
    a = 0
    b = 0
    for i in range(1, len(s), 2):
        if s[i] in s[:i]:
            continue
        elif s[i] in string.whitespace:
            a += 1
        elif "A" <= s[i] <= "Z":
            b += 1
    return len(s) < 10 and a > 1 and a == b

def testRocAnswer():
    print("Testing rocAnswer()...", end="")
    answer = rocAnswer()
    assert(roc(answer) == True)
    print("Passed.")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) == \
        "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    print("Passed.")

def testGradebookSummary():
    print("Testing gradebookSummary()...", end="")
    import os
    if not os.path.exists("hw3_files"):
        assert False,"You need to unzip hw3_files.zip to test gradebookSummary"

    assert(gradebookSummary("hw3_files/gradebook1.txt") == 
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("hw3_files/gradebook2.txt") == 
            "wilma\t92.67\nfred\t90.40\nbetty\t88.00")
    assert(gradebookSummary("hw3_files/small1.txt") == 
            "fred\t0.00")
    assert(gradebookSummary("hw3_files/small2.txt") == 
            "fred\t-1.00\nwilma\t-2.00")
    assert(gradebookSummary("hw3_files/small3.txt") == 
            "fred\t100.50")
    assert(gradebookSummary("hw3_files/small4.txt") == 
            "fred\t49.00\nwilma\t50.00")
    print("Passed.")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    pattern1 = """
***************
******   ******
***************
"""
    result1 = """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
    assert(patternedMessage("Go Pirates!!!", pattern1).strip("\n") == result1.strip("\n"))

    pattern2 = """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""
    result2 = """
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
    assert(patternedMessage("Three Diamonds!",pattern2).strip("\n") == 
            result2.strip("\n"))

    pattern3 = """
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
"""
    result3 = """
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    assert(patternedMessage("Go Steelers!",pattern3).strip("\n") == 
            result3.strip("\n"))
    print("Passed.")

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("We attack at Dawn") == "atwcdekn")
    s = "Note that digits, punctuation, and whitespace are not letters!"
    assert(mostFrequentLetters(s) == "teanioscdhpruglw")
    assert(mostFrequentLetters("") == "")
    print("Passed.")

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed.")

def testJustifyText():
    print("Testing justifyText()...", end="")
    text1 = """\
We hold these truths to be self-evident:  that all men are created equal;
that they are endowed by their Creator with certain unalienable rights;
that among these are life, liberty, and the pursuit of happiness."""
    text1Result = """\
We  hold  these  truths  to be
self-evident: that all men are
created  equal;  that they are
endowed  by their Creator with
certain   unalienable  rights;
that  among  these  are  life,
liberty,  and  the  pursuit of
happiness."""
    assert(justifyText(text1, 30) == text1Result)
    text2 = """\
Though, in reviewing the incidents of my administration,
I am unconscious of intentional error, I am nevertheless too sensible of my
defects not to think it probable that I may have committed many errors.
I shall also carry with me the hope that my country will view them with
indulgence; and that after forty-five years of my life dedicated to its service
with an upright zeal, the faults of incompetent abilities will be consigned to
oblivion, as I myself must soon be to the mansions of rest.

I anticipate with pleasing expectation that retreat in which I promise myself
to realize the sweet enjoyment of partaking, in the midst of my fellow-citizens,
the benign influence of good laws under a free government,
the ever-favorite object of my heart, and the happy reward,
as I trust, of our mutual cares, labors, and dangers."""
    text2Result = """\
Though,  in  reviewing  the  incidents  of  my  administration,  I  am
unconscious of intentional error, I am nevertheless too sensible of my
defects  not  to  think  it  probable  that  I may have committed many
errors.  I shall also carry with me the hope that my country will view
them  with  indulgence;  and  that  after  forty-five years of my life
dedicated  to  its  service  with  an  upright  zeal,  the  faults  of
incompetent  abilities will be consigned to oblivion, as I myself must
soon   be  to  the  mansions  of  rest.  I  anticipate  with  pleasing
expectation  that  retreat  in  which  I promise myself to realize the
sweet  enjoyment of partaking, in the midst of my fellow-citizens, the
benign   influence   of   good  laws  under  a  free  government,  the
ever-favorite object of my heart, and the happy reward, as I trust, of
our mutual cares, labors, and dangers."""
    assert(justifyText(text2, 70) == text2Result)
    print("Passed.")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed.")

#################################################
# Hw3 Main
#################################################

def testAll():
    testRocAnswer()
    testApplyCaesarCipher()
    testGradebookSummary()
    testPatternedMessage()
    testMostFrequentLetters()
    testLongestCommonSubstring()
    testJustifyText()
    testBonusGetEvalSteps()

def main():
    cs112_f18_week3_linter.lint() # check for forbidden syntax
    testAll()

if __name__ == '__main__':
    main()
