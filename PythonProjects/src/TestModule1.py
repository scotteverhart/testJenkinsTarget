"""
@created:   Feb 20, 2017
@author: scotteverhart
"""

import stringFormatter
import random


class printStuff():

    outputFileName = 'myTestFile.txt'
    randNum = random.randint(1,10)
    num = range(0,randNum)
    listValues = ["one  ","two  ","three","four ","five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven "]
    
    print
    print "randNum: ",randNum
    print "Values in num: ",num
    print "Values in listValues: ",listValues
    print
    
    def printRange(self):
        for i in self.num:
            print i,self.printText(i-1)
        print "class processing complete"
            
    def printText(self,listNum):
        
        outputtext =  "\t" + stringFormatter.addTwoHyphensBeforeAndAfter(self.listValues[listNum]) + "\t" + \
            stringFormatter.addTwoAsterisksBeforeAndAfter(self.listValues[listNum]) + "\t" + \
            stringFormatter.addTwoCaretsBeforeAndAfter(self.listValues[listNum])
            
        self.of =file(outputFileName, 'w')
        self.of.write(outputtext)
        
if __name__ == '__main__':
    printStuff().printRange()