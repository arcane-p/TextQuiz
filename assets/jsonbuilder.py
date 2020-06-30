#!/usr/bin/env python3
import json
from codecs import decode, encode
import uu
from .PP import PPrint  # Pretty printing

main = {}


class QuestionGen:
    def __init__(self, questionNum, question, options, answerNum, hintAvailable=0, hintMessage=0):
        self.questionNum = questionNum
        self.question = question
        self.options = options
        self.answerNum = answerNum
        self.hintAvailable = hintAvailable
        self.hintMessage = hintMessage

    def write(self):
        main[f"Question{str(self.questionNum)}"] = {"question": self.question, "options": self.options,
                                                    "answerNum": self.answerNum, "hintAvailable": self.hintAvailable, "hintMessage": self.hintMessage}


def BuildJSON(filename):
    # Validate filename
    if ".json" not in filename:
        filename = filename + ".json"
    #
    totalQuestions = 0
    PPrint("Write question you wish to ask, or 'stop' to signify end of quiz", "module")
    question = ""
    while True:  # stops chain when input = stop
        # QUESTION
        question = input(f"Question {str(totalQuestions+1)}: ")
        if "stop" in question:
            break
        # Increase questionNum and totalQuestions - they effectively work the same
        totalQuestions += 1
        # OPTIONS
        PPrint(
            "Write available answers. Can put as many as you want, write 'stop' to finish", "module")
        i = 0
        options = []
        answer = ""
        while "stop" not in answer:
            i += 1  # for beauty haha
            answer = input(f"{i}: ")
            options.append(answer)
        # side effect of while list. using while true makes me uncomfy
        options = options[:-1]
        # ANSWERNUM
        try:
            answerNum = int(
                input("What QUESTION number is the correct answer? "))
            if answerNum > len(options):
                PPrint("Not a valid answer! One more chance", "minus")
                answerNum = int(
                    input("What QUESTION number is the correct answer? "))
        except Exception:
            PPrint("Not a number! One more chance", "minus")
            answerNum = int(
                input("What QUESTION number is the correct answer? "))
        # HINT?
        if input("Hint (Y/N)? ")[0].upper() == "Y":
            hintAvailable = 1
            hintMessage = input("Hint message: ")
        else:
            hintAvailable = 0
            hintMessage = 0
        # Done! send to json
        QuestionGen(totalQuestions, question, options, answerNum,
                    hintAvailable, hintMessage).write()
        PPrint("Question completed. \n", "module")

    main["totalQuestions"] = totalQuestions
    # Write this stuff
    all_json = json.dumps(main)
    enc_json = encode(all_json, "rot_13")
    with open(filename, 'w') as f:
        f.write(enc_json)
