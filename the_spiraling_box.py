# https://www.codewars.com/kata/63b84f54693cb10065687ae5
import math

def create_box(x,y):
    rows = []
    for rowIndex in range(1,y+1):
        newRow = list(range(x))
        for columnIndex in range(1,rowIndex+1):
            middleRow = newRow[columnIndex -1:len(newRow)-columnIndex+1]
            for index,_ in enumerate(middleRow) :
                middleRow[index] = columnIndex 
            newRow[columnIndex -1:len(newRow)-columnIndex+1] = middleRow
        rows.append(newRow)
    finalRows = reversed(rows[0:int(abs(y/2))])
    rows[math.ceil(abs(y/2)):] = finalRows
    return rows


result = create_box(10,12)
for array in result:
    print(array)
if result == [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]:
    print('ok')
else:
    print('errado')

result = create_box(5,8)
for array in result:
    print(array)
if result == [
    [1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1],
    [1, 2, 3, 2, 1],
    [1, 2, 3, 2, 1],
    [1, 2, 3, 2, 1], 
    [1, 2, 3, 2, 1],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]
]:
    print('ok')
else:
    print('errado')

result = create_box(19,19)
for array in result:
    print(array)
if result == [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]:
    print('ok')
else:
    print('errado')