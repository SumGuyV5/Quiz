#!/usr/bin/env python
"""***************************************************************
**  Program Name:   Quiz					**
**  Version Number: V1.0                                        **
**  Copyright (C):  June 15, 2009 Richard W. Allen              **
**  Date Started:   April 20, 2009                              **
**  Date Ended:     June 15, 2009                               **
**  Author:         Richardn W. Allen                           **
**  Webpage:        http://richard-allen.homelinux.com/         **
**  IDE:            IDLE 2.6.2                                  **
**  Compiler:       Python 2.6.2                                **
**  Langage:        Python 2.6.2				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import random

class Question:
    """Holds the Question information for the game."""
    def __init__(self):
        self.text = "Error"
        self.answer = 0
        self.options = ["Error", "Error", "Error", "Error"]
        self.moreinfo = ""
        self.source = ""

    """We take the answer out of the 'options' list a random number
    and insert the answer back in to the 'options' list based on that
    random number we also change the 'answer' var to the random number
    so that we know were the anwer is at all times."""
    def CreateRandOptions(self):
        """CreateRandOptions():
        Input: None
        Output: None
        Side effects: We take the answer out of the
        self.options variable get a random number and insert
        the answer back into the self.options variable and
        change the self.answer to the random number."""
        random.seed()
        rand = random.randint(0, 3)

        opt = self.options[self.answer]
        self.options.remove(opt)

        self.options.insert(rand, opt)
        self.answer = rand

    def CheckInput(self, input):
        """CheckInput(input):
        Input: The number the user inputed.
        Output: A number
        Side effects: We take the input of the user
        and see if its the correct answer. 0 is return
        if the input is correct, 1 if the input is wrong and
        2 if the input is out of range."""
        inputnum = 0
        try:
            inputnum = int(input)
        except ValueError:
            print 'Digits only please.'
            inputnum = -1
            
        if inputnum > 4 or inputnum < 1:
            return 2
        
        if inputnum - 1 == self.answer:
            return 0
        else:
            return 1

if __name__ == "__main__":
    print "Testing Question Class\n"

    quest = Question()

    print "Testing CheckInput(input)...\n"
    
    print "Test 1. Checking if an input of 0 will return 2."
    if quest.CheckInput(0) != 2:
        print "Error in CheckInput(input) == 0 should be 2"
        print "input was 0, 0 should reutrn 2"
    else:
        print "Pass...\n"

    print "Test 2. Checking if an input of 5 will return 2."
    if quest.CheckInput(5) != 2:
        print "Error in CheckInput(input) == 0 should be 2"
        print "input was 0, 0 should reutrn 2"
    else:
        print "Pass...\n"
        
    print "Test 3. Checking if an input of 1 will return 0."
    if quest.CheckInput(1) != 0:
        print "Error in CheckInput(input) == 1 should be 0"
        print "input was 1, 1 should return 0"
    else:
        print "Pass...\n"

    print "Test 4. Checking if an input of 'a' will return 2"
    if quest.CheckInput('a') != 2:
        print "Error in CheckInput(input) == True should be False"
        print "input was 'a', 'a' should return False"
    else:
        print "Pass...\n"

    print "Testing CreateRandOptions()...\n"
    
    quest.options = ['Answer', 'Wrong1', 'Wrong2', 'Wrong3']
    quest.CreateRandOptions()

    print "Test 1. Checking if options are random."
    if quest.options == ['Answer', 'Wrong1', 'Wrong2', 'Wrong3']:
        print "Error in CreateRandOptions() Options not random"
        print str(quest.options)
    else:
        print "Pass..\n"
    
    
