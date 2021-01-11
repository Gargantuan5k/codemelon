print('''
x----------------------------------------------------------------------------------------------------------------------x
CodeMelon
Shell v0.3.0 (indev)
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
        elif result:
            print(result)
        else:
            pass
