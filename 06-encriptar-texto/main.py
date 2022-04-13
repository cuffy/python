from sys import argv
import hashlib

ARGV_ACTIONS = ["sha1", "check"]

if len(argv) > 1 and argv[1] in ARGV_ACTIONS:
    action = argv[1]
    if action == ARGV_ACTIONS[0]:
        try:
            print(hashlib.sha1(argv[2].encode()).hexdigest())
        except IndexError:
            pass
    elif action == ARGV_ACTIONS[1] and len(argv) > 3:
        sha1_text = hashlib.sha1(argv[2].encode()).hexdigest()
        compare_text = argv[3]
        if sha1_text == compare_text:
            print("Los textos coinciden!")
        else:
            print("Los textos no coinciden.")
    else:
        print("Los parametros no coinciden con: check text sha1_text")
else:
    print("Primer argumento no valido, los posibles:", ARGV_ACTIONS)
