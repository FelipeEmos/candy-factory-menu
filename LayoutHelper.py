from typing import List


class LayoutHelper():
    # Arbitrary value
    defaultWidth = 66

    
    def alignLeft_untilWidth(string:str, width:int, marginLeft:int=0):
        available_space = width - marginLeft
        remaining_space = available_space - len(string)
        
        if(remaining_space >= 3):
            resultLine = string + (remaining_space * " ")
        else:
            resultLine = string[:available_space-3] + "..."+string[-1:]
        return resultLine
        
    def getLine_TwoColums(leftStr:str,
                          rightStr:str,
                          marginLeft=0,
                          marginRight=0,
                          sepWidth:int = 20,
                          width=defaultWidth
                          ) -> str:

        resultLine = LayoutHelper.alignLeft_untilWidth(
            leftStr,
            width=sepWidth,
            marginLeft=marginLeft)
        
        resultLine += LayoutHelper.alignLeft_untilWidth( rightStr,
            width=width -  sepWidth - marginRight)
        
        return resultLine
    
    def fillLine(string:str, marginLeft=0, marginRight=0, width:str=defaultWidth):
        available_space = width - marginLeft - marginRight
        remaining_space = available_space - len(string)
        
        if(remaining_space >= 0):
            resultLine = string + (remaining_space * " ")
        else:
            resultLine = string[:available_space-3] + "..."
        return resultLine
    