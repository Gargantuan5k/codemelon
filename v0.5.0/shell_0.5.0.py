print('''
x----------------------------------------------------------------------------------------------------------------------x
CodeMelon
Shell v0.4.0 (indev)
x----------------------------------------------------------------------------------------------------------------------x
''')
import codemelon

while True:
    text = input('>>> ')

    if text.lower() == 'exit()':
        break

    elif text.strip() == '':
        continue

    else:
        result, error = codemelon.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(result)
        else:
            pass
