# TextQuiz
A CLI 'quizlet' generator. Interactively lets you write your own questions and answers, with the option to add hints. Supports all types of multiple choice answers (including True or False), and creates an encoded .pyc application with obfuscated answers contained within. Uses no external libraries, so can be ran on any computer with python3.

## Features
- Interactive mode generates JSON answer file. This is encoded with rot_13, since base 64 is pretty recognisable, however with an encoded pyc file the decoding in-file won't be easily spotted.
- Offers scrambling of both answers and/or questions
- compiles .py into .pyc to try to make it harder for people to find the answers
- Any number of options, which allows for true/false and any multiple choice style questions.
- Entire generated quiz is contained within single small application.

## Use
Generator prefers to use colorama, but should still work without. The quizlet requires no external libraries.
**Install colorama**
```bash
pip install colorama
```
or
```bash
pip install -r "requirements.txt"
```
**Generate Quizlet**
Simply run application and follow prompts. When it finishes will generate the encoded final file.
```bash
python3 TextQuizGen.py
```
**Run Quizlet**
On the tester's computer can just be executed with python3
```bash
python3 *quizname*.pyc
```

##What's Next?
- Ensure running python3
- Option to list all correct answers at the end
- Multiple correct answers
- Test mode
  - Can only be run once, stronger obfuscation, json padding, timed
- Once CLI is totally finished, attempt to make a GUI version.

##Why?
I recognise this may not be the most useful program, but it was a very useful exercise in object-oriented programming. I'm much more comfortable with linear, maths-style operations, so this was a welcome challenge.
It's also not the worst application, and could be realistically used as a testing tool.
