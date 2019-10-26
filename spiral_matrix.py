theMatrix = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13,14, 15, 16]
            ]

endRowIndex = 4
endColumnIndex = 4



def printSpiralMatrix(endRowIndex, endColumnIndex, theMatrix):
     startRowIndex = 0
     startColumnIndex = 0
     while (startRowIndex < endRowIndex and startColumnIndex < endColumnIndex):
           for i  in range(startColumnIndex, endColumnIndex):
                print(theMatrix[startRowIndex][i], end= " ")  # first_row
           startRowIndex += 1  #increment-decrement depending on the way you want to traverse the array

           for i in range(startRowIndex, endRowIndex):
                print(theMatrix[i][endColumnIndex-1], end=" ") # last_column
           endColumnIndex -= 1 #increment-decrement depending on the way you want to traverse the array
         
           if (startRowIndex < endRowIndex):
              for i in range(endColumnIndex-1, startColumnIndex-1, -1):#range(3,-1,-1), reverse from index 3 to index 0 
                   print(theMatrix[endRowIndex-1][i], end=" ") #last_row remaining_elements
              endRowIndex -= 1 #increment-decrement depending on the way you want to traverse the array

           
           if (startColumnIndex < endColumnIndex):
              for i in range(endRowIndex-1, startRowIndex-1, -1):
                   print(theMatrix[i][startColumnIndex], end=" ")
              startColumnIndex += 1 #increment-decrement depending on the way you want to traverse the array
      
           

printSpiralMatrix(endRowIndex, endColumnIndex, theMatrix)