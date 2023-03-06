# https://www.codewars.com/kata/63b84f54693cb10065687ae5

def create_box(x,y):
    def get_number(listIndex,numberIndex):
        pass


    return [
        [
            get_number(listIndex,numberIndex)
            for numberIndex,_ in enumerate(range(x))
        ]
        for listIndex,_ in enumerate(range(y)) 
    ]
    pass









result = create_box(10,9)
for array in result:
    print(array)
if result == [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
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