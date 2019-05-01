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
import sys
sys.path.append('Module.zip')

from Module.QuizXMLSetup import QuizXMLSetup
           
if __name__ == "__main__":
    quiz = QuizXMLSetup()

    ses = quiz.QuizSessionSetup(5)
    ses.RunSession()
