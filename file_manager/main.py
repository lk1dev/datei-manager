from file_manager import list_files, rename_file, delete_file, move_file
from utils import set_start_directory
from config import load_config, save_config

def main():
    # Lade die Konfigurationen
    config = load_config()
    start_directory = config.get("start_directory", "/")  # Default Startverzeichnis
    set_start_directory(start_directory)

    while True:
        print("\n--- Dateimanager ---")
        print("1. Dateien anzeigen")
        print("2. Datei umbenennen")
        print("3. Datei löschen")
        print("4. Datei verschieben")
        print("5. Verzeichnis wechseln")
        print("6. Beenden")
        
        choice = input("Wähle eine Option (1/2/3/4/5/6): ")

        if choice == '1':
            list_files(start_directory)
        elif choice == '2':
            old_name = input("Gib den alten Dateinamen ein: ")
            new_name = input("Gib den neuen Dateinamen ein: ")
            rename_file(old_name, new_name)
        elif choice == '3':
            file_name = input("Gib den Dateinamen ein, den du löschen möchtest: ")
            delete_file(file_name)
        elif choice == '4':
            file_name = input("Gib den Dateinamen ein, den du verschieben möchtest: ")
            target_directory = input("Gib das Zielverzeichnis ein: ")
            move_file(file_name, target_directory)
        elif choice == '5':
            new_directory = input("Gib das neue Startverzeichnis ein: ")
            set_start_directory(new_directory)
            config["start_directory"] = new_directory
            save_config(config)  # Speichern der neuen Konfiguration
        elif choice == '6':
            print("Dateimanager beendet!")
            break
        else:
            print("Ungültige Auswahl!")

if __name__ == "__main__":
    main()
