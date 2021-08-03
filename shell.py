import pathlib

version = '1.1.0'

print(f'''
x----------------------------------------------------------------------------------------------------------------------x
🍉 CodeMelon 🍉
🐚 Shell Release {version} 🐚
x----------------------------------------------------------------------------------------------------------------------x

Type '_license_', '_about_', '_syntax_' or '_test_' For more info.
Type 'exit()' to exit Shell.

''')
import codemelon

while True:
    try:
        text = input('🍉> ')

        if text.lower().strip() == 'exit()':
            break
        elif text.lower().strip() == '_syntax_':
            try:
                print(open(f"{pathlib.Path(__file__).parent.resolve()}\\assets\\_syntax_.txt", "r").read())
            except:
                print("ERROR: Could not locate CodeMelon file _syntax_.txt")
        elif text.lower().strip() == '_license_':
            try:
                print(open(f"{pathlib.Path(__file__).parent.resolve()}\\assets\\_license_.txt", "r").read())
            except:
                print("ERROR: Could not locate CodeMelon file _license_.txt")

        elif text.strip().lower() == '_test_':
            print(str(open(f"{pathlib.Path(__file__).parent.resolve()}\\assets\\test.mln", "r").read()))
            print("\n\nOUTPUT:\n")
            runpath = f"{pathlib.Path(__file__).parent.resolve()}/assets/test.mln".replace("\\", "/")
            res, err = codemelon.run("test.mln", f"run(\"{runpath}\")")
            
            if err:
                print(err.as_string())
            elif res:
                if len(res.elements) == 1:
                    print(repr(res.elements[0]))
                else:
                    print(res)
            else:
                pass

        elif text.strip().lower() == '_about_':
            print(open(f"{pathlib.Path(__file__).parent.resolve()}\\assets\\_about_.txt", "r").read())

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
    except EOFError:
        print("Goodbye")
        break
