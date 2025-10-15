import os
import subprocess
import sys

wt_path = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "WindowsApps", "wt.exe")
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
exe_path = os.path.join(desktop, "code inspecteur", "dist", "main.exe")

if not os.path.isfile(exe_path):
    print(f"❌ Impossible de trouver main.exe à : {exe_path}")
    input("Appuyez sur Entrée pour quitter...")
    sys.exit(1)

subprocess.run([
    wt_path,
    "powershell",
    "-NoExit",
    "-Command",
    f"& '{exe_path}'"
])
