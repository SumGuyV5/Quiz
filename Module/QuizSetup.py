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
import os
import random

from Question import Question
from QuizSession import QuizSession

class QuizSetup:
    """Sets up the Quiz  """
    def __init__(self):
        self.questions = []
        self.num = 0
        
        self.ReadQuestionFile(os.getcwd() + '..\\Text\\questions.txt')
        self.ReadAnswerFile(os.getcwd() + '..\\Text\\answers.txt')
        self.ReadMoreInfoSource(os.getcwd() + '..\\Text\\facts.txt')

        self.num = len(self.questions)

        

    def QuizSessionSetup(self, howmany):
        """QuizSessionSetup(howmany):
        Input: The number of questions.
        Output: The QuizSession object
        Side effects: Random numbers to pick the questions
        that are avable and returns a QuizSession objcet that
        is ready to run."""
        random.seed()

        """if there less questions avalable
        we change howmany varable to self.num"""
        if self.num < howmany:
            howmany = self.num

        numlist = []
       
        count = 1
        while 1:
            if self.num > 0:
                rand = random.randrange(0, self.num)
            else:
                rand = 0
                
            if numlist.count(rand) == 0:
                numlist.append(rand)
                count = count + 1

            if count > howmany:
                break #exit the while loop

        
        temp = []
        for num in numlist:            
            temp.append(self.questions[num])
            
        session = QuizSession(temp)
                
        return session 
    
    def ReadQuestionFile(self, filename):
        """ReadQuestionFile(filename):
        Input: File Name.
        Output: None
        Side effects: Reads the file that holds the
        Questions for the game."""
        try:
            file = open(filename, 'r')
            for lines in file:
                line = lines.strip('\n')
                quest = Question()
                quest.text = str(line)
                self.questions.insert(1, quest)
            file.close()
        except IOError:
            print 'File IO Error on file name ' + filename

    def ReadAnswerFile(self, filename):
        """ReadAnswerFile(filename):
        Input: File Name.
        Output: None
        Side effects: Reads the file that holds the
        Answer for the game."""
        try:
            file = open(filename, 'r')
            count = 0
            
            for lines in file:
                line = lines.strip('\n')
                
                opts = line.split(':')
                self.questions[count].options = opts
        
                count = count + 1
                
            self.num = count
                           
            file.close()
        except IOError:
            print 'File IO Error on file name ' + filename

    def ReadMoreInfoSource(self, filename):
        """ReadMoreInfoSource(filename):
        Input: File Name.
        Output: None
        Side effects: Reads the file that holds the
        More Info for the game."""
        try:
            file = open(filename, 'r')
            count = 0
            
            for lines in file:
                line = lines.strip('\n')
                
                infos = line.split(':')

                for info in infos:
                    if info == infos[0]:
                        self.questions[count].moreinfo = info
                    else:
                        self.questions[count].source += info
        
                count = count + 1
                
            file.close()
        except IOError:
            print 'File IO Error on file name ' + filename
