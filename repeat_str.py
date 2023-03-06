# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e

# def repeat_str(repeat,string):
#     return string * repeat
 
repeat_str = lambda repeat,string:string*repeat



if repeat_str(6,'I') == 'IIIIII':
    print('ok')
else:
    print('errado')