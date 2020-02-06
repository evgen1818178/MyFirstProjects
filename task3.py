InputString = ''
slovar = {}

while InputString != 'exit':
    InputString = input('type string: ')
    if InputString in slovar:
        slovar[InputString] = slovar.get(InputString) + 1
    else:
        slovar[InputString] = 1

del slovar['exit']
print('collecting stats')
print('stats:',slovar)