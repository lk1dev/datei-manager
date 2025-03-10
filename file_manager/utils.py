import os

def set_start_directory(path):
    """Setzt das Startverzeichnis für den Dateimanager."""
    if os.path.exists(path): 
        os.chdir(path)
        print(f"Startverzeichnis auf '{path}' gesetzt.")
    else:
        print(f"Das Verzeichnis '{path}' existiert nicht.")
