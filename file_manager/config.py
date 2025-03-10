import json 

def load_config():
    """Lädt die Konfiguration aus einer JSON-Datei."""
    try: 
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Konfigurationsdatei nicht gefunden.")
        return {}

def save_config(config):
    """Speichert die Konfiguration in einer JSON-Datei."""
    with open('config.json', 'w') as file:
        json.dump(config, file)
