# questionnaire

Documentation for Questionnaire

Purpose:
    The purpose of Questionnaire is to add some fun to writing a program. Instead of
  using the familiar statements, variables, loops, etc., we wanted a programming
  language that made all of that into questions. Did you want to execute these
  statements maybe with these conditions? What is the variable and its associated
  value? It is up to you to decide how you want to question yourself and answer it
  with your code.

How to program in our language:
1. Spaces are what determines how the language interprets the code:
    ex. "whatis var1 its 2" is different from "whatisvar1its2"
2. Numbers cannot be anything but whole numbers
3. Only mathematical operators are '+', '-', '*', and '/'
4. Capitalization is very important when writing statements and
    operators. If you have an uppercase 'W' in 'saywhat', the language
    will not understand what you have asked.
5. You do not need to worry about indentation for maybe statements, etc.
    As long as you place the appropriate start and end identifiers with
    the statement, the program will run.
6. You do not need to use semicolons or anything to indicate the signal
    end of statement.
7. Important to keep your maybe statement block between '?' and '!', otherwise
    the block runs regardless of your condition.

Keywords:
  = - its
    '=' in programming languages usually denotes what a statement or
    expression is assigned to (ex. num = 1, num3 = 1 + 2, a = b). In
    Questionnaire, we switch '=' with 'its'.
  == - itsits
    '==' in programming languages is the equality operator that checks
    if the values of symbols are exactly equal to each other (ex. 1 == 1,
    num1 = 2; num1 == 2). If both are not equal to each other, the program
    usually errors. Questionnaire uses 'itsits' to express '=='.
  VARIABLE - whatis
    A variable is a storage location paired with an associated
    symbolic name (an identifier), which contains some known or unknown
    quantity of information referred to as a value (ex. num = 1 is a variable).
    We use 'whatis' to express a symbol as a variable.
  if - maybe
    The if statement is used to check a condition and if the condition is true,
     we run a block of statements.
     ex.
        if(1 == 1)
          This is true!
     We use 'maybe' to express an if statement in Questionnaire.
  Then - ?
    The startIf or Then identifier is the when an if statement block begins if the
    condition turned out to be true. This is usually denoted as being the start of
    brackets (ex. {) or being indented beneath the if statement. In Questionnaire,
    'then' is expressed as '?'.
  endIf - !
    The endIf is the identifier that indicates when an if statement block is complete
    and closes the statement. This is usually denoted as the ending brackets (ex. }).
    In Questionnaire, we express the endIf with '!'.
