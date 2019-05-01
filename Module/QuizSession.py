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
from Question import Question

class QuizSession:
    """Runs the main control for the game."""
    def __init__(self, questions = []):
        """init the variables """
        self.score = 0
        self.questions = questions

    def RunSession(self):
        """RunSession():
        Input: None
        Output: None
        Side effects: Runs the Quiz Session using the
        questions stored in self.questions variable and
        add to the self.scoure variable when a question
        is answered correct."""
        for i in self.questions:
            
            i.CreateRandOptions()

            while 1:
                print i.text
                count = 1
                print "is it..."
                for op in i.options:
                    print str(count) + " " + op
                    count = count + 1

                answer = raw_input("press a num\n")

                check = i.CheckInput(answer)
                if check == 0:
                    print "Your Right!"
                    self.score += 1
                    break
                elif check == 1:
                    print "Your Wrong!"
                    break
                elif check == 2:
                    print "Repet"
            print i.moreinfo
            print i.source
            print "---------------------------"
        self.SessionEnd()
            
    def SessionEnd(self):
        """SessionEnd():
        Input: None
        Output: None
        Side effects: Print a thank you message and
        a message with your score."""
        print "Thank you for playing Quiz!"
        print "You Got " + str(self.score) + " question right!"

if __name__ == "__main__":

    print "Testing... QuizSession Class"
    quiz = QuizSession([Question()])

    quiz.RunSession()
    
        
    
        
