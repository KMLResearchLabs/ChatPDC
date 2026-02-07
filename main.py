from PDCBot import *
from terminalpkg import *
from prompts import chatpdc_prompts

clear()
banner()

actual_mode = "Normal"

while True:
    print("\n(Type HELP to see commands)")
    cmd = input(">>> ").strip().upper()

    if cmd == "CLEAR":
        clear()
        banner()

    elif cmd == "HELP":
        helpi()

    elif cmd == "SELECT":
        while True:
            print("\n[1] Normal [2] Curto e grosso [3] Filósofo [4] Listador")
            md = input("Select a mode: ").strip()

            if md.isdigit() and int(md) in (1, 2, 3, 4):
                amode = int(md)
                actual_mode = select_mode(amode)
                break
            else:
                print("[ERROR] Invalid mode.")

    elif cmd == "QUIT":
        break

    else:
        PDC_Bot(cmd, chatpdc_prompts[actual_mode])
