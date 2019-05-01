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
import sys
import random
import subprocess
sys.path.append('Module.zip')

from Question import Question
from QuizSession import QuizSession

from xml.dom.minidom import parse, getDOMImplementation

class QuizXMLSetup:
    """Loads and xml file with the Questions"""
    def __init__(self):
        self._dom = object

        self.questions = []
        self.num = 0

        #self.ReadXMLFile(os.getcwd() + '\\xml\\quiz.xml')
        self.ReadXMLFile('C:\\Documents and Settings\\Administrator\\Desktop\\old\\Quiz\\xml\\quiz.xml')

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
    
    def ReadXMLFile(self, filename):
        """ReadQuestionFile(filename):
        Input: File Name.
        Output: None
        Side effects: Reads the file that holds the
        Questions for the game."""
        try:
            self._dom = parse(filename)
        except:
            print 'File IO Error on file name ' + filename

        questions = self._dom.getElementsByTagName("Question")
        for question in questions:
            self._LoadQuestion(question)
            
    def _LoadQuestion(self, question):
        """_LoadQuestion(question)
        Input: xml element
        Output: None
        Side effects: Loads up the Question xml tag into a
        Question oject and calls _LoadAnswers and _LoadFacts."""
        text = question.getElementsByTagName("Text")[0].firstChild.nodeValue
        
        options = self._LoadOptions(question)

        facts = self._LoadFacts(question)

        quest = Question()
        quest.text = text
        quest.options = options
        quest.moreinfo = facts[0]
        quest.source = facts[1]
        self.questions.append(quest)

    def _LoadOptions(self, question):
        """_LoadOptions(question)
        Input: xml element
        Output: Answers array
        Side effects: Loads up the Option xml tag into a
        array and returns it."""
        rtnvar = []
        options = question.getElementsByTagName("Option")
        for option in options:
            if (option.getElementsByTagName("Answer").length > 0):
                rtnvar.insert(0, option.firstChild.nodeValue)
            else:
                rtnvar.append(option.firstChild.nodeValue)

        return rtnvar

    def _LoadFacts(self, question):
        """_LoadFacts(question)
        Input: xml elemnt
        Output: Facts array
        Side effects: Loads up the Facts and Source xml tag into a
        array and returns it."""
        rtnvar = []

        fact = ""
        source = ""

        try:
            fact = question.getElementsByTagName("Facts")[0].firstChild.nodeValue
        except:
            pass
        try:
            source = question.getElementsByTagName("Source")[0].firstChild.nodeValue
        except:
            pass

        rtnvar.append(fact)
        rtnvar.append(source)
        #rtnvar.insert(1, facts.attributes["text"].value)
        #rtnvar.insert(2, facts.attributes["source"].value)

        return rtnvar

if __name__ == "__main__":
    quiz = QuizXMLSetup()
    i = quiz.QuizSessionSetup(5)
    #print i.questions[0].options


        
            
