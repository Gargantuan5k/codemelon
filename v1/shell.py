print('''
x----------------------------------------------------------------------------------------------------------------------x
CodeMelon
Shell v1.0.0
x----------------------------------------------------------------------------------------------------------------------x
''')
import codemelon

while True:
    text = input('>>> ')

    if text.lower() == 'exit()':
        break

    else:
        result, error = codemelon.run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)
