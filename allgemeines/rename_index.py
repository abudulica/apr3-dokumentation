import os

def rename_index_files(directory):
    # Durchlaufe alle Dateien und Unterordner im angegebenen Verzeichnis
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Überprüfe, ob die Datei "Index" heißt
            if file == "Index":
                # Erstelle den neuen Dateinamen
                new_file_name = "Readme"
                # Vollständiger Pfad zur Datei
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_file_name)
                
                # Benenne die Datei um
                os.rename(old_file_path, new_file_path)
                print(f"Umbenannt: {old_file_path} -> {new_file_path}")

        # Gebe die Ordnernamen in kursiver Schrift aus
        for dir_name in dirs:
            print(f"*{dir_name}*")

# Setze hier den Pfad zu dem Verzeichnis, das du durchsuchen möchtest
directory_path = "dein/verzeichnis/pfad"
rename_index_files(directory_path)
