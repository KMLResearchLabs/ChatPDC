def banner():
    print(""" 
 ██████╗██╗  ██╗ █████╗ ████████╗    ██████╗ ██████╗  ██████╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝
██║     ███████║███████║   ██║       ██████╔╝██║  ██║██║     
██║     ██╔══██║██╔══██║   ██║       ██╔═══╝ ██║  ██║██║     
╚██████╗██║  ██║██║  ██║   ██║       ██║     ██████╔╝╚██████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═════╝  ╚═════╝
                                                             
 <Personal Confused Dummy>
 Developed by ByKurebo
 KML Research Labs 2026                                                          
""")
    
def clear():
    import os
    os.system("clear")

def helpi():
    print("""
HELP - Show all commands
CLEAR - Clean the terminal
QUIT - Quit ChatPCD
SELECT - Change ChatPDC Mode""")

def select_mode(mode):
    if mode == 1:
        return "Normal"
    if mode == 2:
        return "Curto e grosso"
    if mode == 3:
        return "Filósofo"
    if mode == 4:
        return "Listador"