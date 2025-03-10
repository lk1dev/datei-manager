# Statt jedes Modul einzeln zu importieren:
# from file_manager.file_manager import list_files
# from file_manager.utils import set_start_directory

# Kannst du das gesamte Paket mit dieser `__init__.py` so importieren:
from file_manager import list_files, rename_file, delete_file, move_file, set_start_directory
