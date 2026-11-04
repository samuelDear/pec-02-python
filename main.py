from app.menu import showMenu
from colorama import init, just_fix_windows_console

# Config de colorama
just_fix_windows_console()
init(autoreset=True)

# Inicio
showMenu()