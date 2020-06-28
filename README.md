# TextQuiz
CLI Quiz generator from scratch. Not the most useful program, it was a very useful exercise in object-oriented programming.
I'm much more comfortable with linear, maths-style operations, so this was a welcome challenge.

**Features**
- Interactive mode creates JSON answer file. This is encoded with uu, since base 64 is pretty recognisable, however with an encoded pyc file the uu decoding won't be easily spotted.
- Offers scrambling of both answers and/or questions
- compiles .py into .pyc to try to make it harder for people to find the answers
- Any number of options,

**Todo**
- Now I'd like to add more customisation. Say a custom title screen.
- Possibly turn this into a quiz generator.
  - Custom start and end titles, custom positive and negative messages, custom questions, custom answers.
  - Output is a fuly functioning quiz. Make it fully contained within a single .py? use py2exe?
- Once CLI is totally finished, attempt to make a GUI version.
