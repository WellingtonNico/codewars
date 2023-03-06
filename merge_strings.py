# https://www.codewars.com/kata/61c78b57ee4be50035d28d42/python

def merge_strings(first, second):
    matches = [
        first[index:len(first)]
        for index in range(len(first))
    ]
    for match in matches:
        if second.startswith(match):
            second = second[len(match):]
            break
    return first + second



if merge_strings('abcde','cdefgh') == 'abcdefgh':
    print('ok')
else:
    print('errado')

if merge_strings('abaab','aabab') == 'abaabab':
    print('ok')
else:
    print('errado')
    print('errado')

if merge_strings('abc','def') == 'abcdef':
    print('ok')
else:
    print('errado')

if merge_strings('abc','abc') == 'abc':
    print('ok')
else:
    print('errado')