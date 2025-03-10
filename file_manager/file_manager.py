import os
import shutil 

def list_files(directory):
    """Listet alle Dateien und Ordner im angegebenen Verzeichnis auf."""
    try: 
        files = os.listdir(directory)
        if not files: 
            print("Das Verzeichnis ist leer.")
        else:
            print(f"Dateien und Ordner in '{directory}'")
            for file in files: 
                print(file)
    except FileNotFoundError:
        print(f"Das Verzeichnis '{directory}' wurde nicht gefunden.")

def rename_file(old_name, new_name):
    """Benennt eine Datei um."""
    try: 
        os.rename(old_name, new_name)
        print(f"Datei umbenannt von '{old_name}' zu '{new_name}'.")
    except FileNotFoundError:
        print(f"Die Datei '{old_name}' wurde nicht gefunden.")

def delete_file(file_name):
    """Löscht eine Datei."""
    try:
        os.remove(file_name)
        print(f"Datei '{file_name}' wurde gelöscht.")
    except FileNotFoundError:
        print(f"Die Datei '{file_name}' wurde nicht gefunden.")

def move_file(file_name, target_directory):
    """Verschiebt eine Datei in ein anderes Verzeichnis."""
    try:
        shutil.move(file_name, target_directory)
        print(f"Datei '{file_name}' wurde nach '{target_directory}' verschoben.")
    except FileNotFoundError:
        print(f"Die Datei '{file_name}' oder das Zielverzeichnis wurde nicht gefunden.")
