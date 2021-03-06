from  PageRow import PageRow
from  AzureLineResult import AzureLineResult
from functools import reduce

class PageVal:
    def __init__(self):
        self.pageRows = []

    #
#    def _init_(self,pagerows):
#      self.pageRows = pagerows

    def addpageRow(self,pagerow):
        #print('In addpageRow')
        updatedList = self.pageRows.append(pagerow)
        #self.pageRows = updatedList

    def createOrAddToPageRow(self,azureLineResult,translatedtText):
        #print('In createOrAddToPageRow.Line text is%s'%azureLineResult["text"])
        if (len(self.pageRows) == 0):
            nppagerow = PageRow()
            nppagerow.addToLine(azureLineResult,translatedtText)
            self.addpageRow(nppagerow)
        else:
            '''
            tempMaxy=azureLineResult["boundingBox"][5]
            if(azureLineResult["boundingBox"][7] >  tempMaxy):
                tempMaxy = azureLineResult["boundingBox"][7]
            '''
            minf = lambda a,b: a if (a < b) else b
            minval = reduce(minf, [azureLineResult["boundingBox"][1],azureLineResult["boundingBox"][3],azureLineResult["boundingBox"][5],azureLineResult["boundingBox"][7]])

            existingrow = 1
            selectedPageRow = None
            for pagerow in self.pageRows:
                #if(pagerow.maxY >= tempMaxy):
                ##If even the minimum is less than any rows maximum, then consider them to be in same row
                if(pagerow.maxY >= minval):

                    #selectedPageRow = pagerow
                    pagerow.addToLine(azureLineResult,translatedtText)
                    #print("AFTER ADDING CONTENTS ARE")
                    existingrow = 0
                    #for result in  pagerow.azureLineResults:
                    #    print(result.textVal)

                    break
            #print ('existingrow %s' %existingrow)
            if (existingrow == 1):
                newpagerow=PageRow()
                newpagerow.addToLine(azureLineResult,translatedtText)
                self.addpageRow(newpagerow)
#            else:
#                selectedPageRow.addToLine(azureLineResult)
#                resultsinrow=selectedPageRow.azureLineResults
#                print("AFTER ADDING CONTENTS ARE")
#                for result in  resultsinrow:
#                    print(result["text"])

    def printValues(self):
        i =1
        for row in self.pageRows:
            print("LINE NUMBER %s"%i)
            resultsinrow=row.azureLineResults
            for result in  resultsinrow:
                print("BoundingBox%s"%result.boundingBoxValues)
                print("text%s"%result.textVal)
                print("translatedtext%s"%result.translatedValue)
            i = i+1
