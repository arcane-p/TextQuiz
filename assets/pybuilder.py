#!/usr/bin/env python3
import string

class PiBuilder():
    def __init__(self):
        self.QuizBody = '''
class Question():
    def __init__(self, number):
        self.number = number
        self.questionData = data["Question" + str(number)]
        ###
        self.questionText = self.questionData["question"]
        self.possibleAnswers = self.questionData["options"]
        self.answerNum = self.questionData["answerNum"]

    def ask(self):
        print(self.questionText)
        for i in range(0,len(self.possibleAnswers)):
            print(f"{i+1}: {self.possibleAnswers[i]}")
        # Loop until valid input
        while True:
            try:
                self.givenAnswer = input("Input number of answer (or '0' for hint: ")
            except ValueError:
                print("Please input a number.")
                continue

            if self.givenAnswer == 0:
                if int(questionData["hintAvailable"]) == 1:
                    print(questionData["hintMessage"])
                else:
                    print("No hint available.")

            if int(self.givenAnswer) > len(self.possibleAnswers):
                print("Doesn't seem to be a valid answer.")
                continue
            else:
                #answer was successfully parsed, and we're happy with its value.
                #we're ready to exit the loop.
                break
        if int(self.givenAnswer) == int(self.answerNum):
            #Correct!
            return True
            print("True")
        else:
            return False
            print("False")

def EndQuiz():
    print(answerList)
    correctAnswers = 0
    incorrectAnswers = 0
    for value in answerList:
        if value == "T":
            correctAnswers += 1
        elif value == "F":
            incorrectAnswers += 1
    print(f"You got {(correctAnswers/(correctAnswers+incorrectAnswers))*100}% correct. That is {correctAnswers} correct, {incorrectAnswers} incorrect.")

def LoadQuiz():
    #Gather "data", either from file or from within.
    global data
    data = json.loads(questionFileContent)
    #Create list with right or wrong
    global answerList
    answerList = []

def StartQuiz():
    #Proceed to ask questions. Find total number then ask iteratively
    totalQuestions = data["totalQuestions"]
    for i in range(1, totalQuestions+1):
        if Question(i).ask() == True:
            answerList.append("T")
        else:
            answerList.append("F")

LoadQuiz()
StartQuiz()
EndQuiz()
'''
        self.QuizHead = '''
#!/usr/bin/env python3
import json
'''
    def build(self,name):
        #Validate filename
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        valid_chars = frozenset(valid_chars) #speed optimization :)
        filename = ''.join(c for c in name if c in valid_chars)
        filename = filename.replace(' ','_') # I don't like spaces in filenames.
        #Create .py file
        with open(filename+".py", 'w') as finalfile:
            finalfile.write(self.QuizHead) # quiz head
            with open("temp_questions.json", 'r') as tempjson:
                jsonquestions = tempjson.read()
            finalfile.write(f'questionFileContent = """{jsonquestions}"""')
            finalfile.write(self.QuizBody)
        #python written
