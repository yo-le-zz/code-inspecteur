import ast
import inspect
import os
import sys
import tkinter as tk
from tkinter import filedialog
import ctypes

"""
Analyseur de script Python
Auteur : yolezz
os : Windows
compiler : Python 3.10+ with pyinstaller
Date : 2024-08-15
Version : 1.0
by : frenche coder
Description : Ce programme analyse un script Python donné et affiche des informations sur les fonctions, classes et docstrings qu'il contient.
Il utilise les modules ast, inspect et tkinter pour la sélection de fichiers.
This project is the original work, can copyright but mention me if you use it.
install : pip install tkinter
"""

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

resource_dir = r"C:\Users\Ilan\Desktop\code inspecteur\r"

root = tk.Tk()
root.iconbitmap(os.path.join(resource_dir, "files.ico"))
root.withdraw()

def analyser_script(path):
    print("\n=== 🔍 Analyse du fichier :", os.path.basename(path), "===")
    print("Chemin :", os.path.abspath(path))

    with open(path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"❌ Erreur de syntaxe : {e}")
        return

    doc = ast.get_docstring(tree)
    print("Docstring du module :", doc or "Aucune")

    fonctions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    if fonctions:
        print("\n📘 Fonctions détectées :")
        for func in fonctions:
            args = [arg.arg for arg in func.args.args]
            print(f"\n--- Fonction : {func.name}({', '.join(args)}) ---")
            fdoc = ast.get_docstring(func)
            print("Docstring :", fdoc or "Aucune")
            start, end = func.lineno, func.end_lineno
            code = source.splitlines()[start - 1:end]
            print("\nCode source :")
            print("\n".join(code))
    else:
        print("\nAucune fonction détectée.")

    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    if classes:
        print("\n🏛️ Classes détectées :")
        for cls in classes:
            print(f"\n--- Classe : {cls.name} ---")
            cdoc = ast.get_docstring(cls)
            print("Docstring :", cdoc or "Aucune")
            methods = [n for n in cls.body if isinstance(n, ast.FunctionDef)]
            if methods:
                print("Méthodes :")
                for m in methods:
                    args = [a.arg for a in m.args.args]
                    print(f"  - {m.name}({', '.join(args)})")
            else:
                print("Aucune méthode.")
    else:
        print("\nAucune classe détectée.")

    print("\n✅ Analyse terminée.")

def main():
    print("=== 🐍 Analyseur de script Python ===")
    print("Choisissez un fichier !")
    path = filedialog.askopenfilename(
        title="Sélectionner un fichier",
        filetypes=(("Fichiers Python", "*.py"), ("Tous les fichiers", "*.*"))
    )
    if not path:
        print("❌ Aucun fichier sélectionné.")
        return
    if not os.path.isfile(path):
        print("❌ Fichier introuvable :", path)
        return
    try:
        analyser_script(path)
    except Exception as e:
        print("⚠️ Erreur pendant l'analyse :", e)

if __name__ == "__main__":
    main()
    print("\n=== Fin du programme ===")
    input("Appuyez sur Entrée pour quitter...")
