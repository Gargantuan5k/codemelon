print('''
x----------------------------------------------------------------------------------------------------------------------x
CodeMelon
Shell v1.1.0_indev
x----------------------------------------------------------------------------------------------------------------------x
''')
import codemelon

while True:
    text = input('>>> ')

    if text.lower() == 'exit()':
        break

    elif text == '' or text == '\n':
        pass

    else:
        result, error = codemelon.run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)
