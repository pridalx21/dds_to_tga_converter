from PIL import Image
import os

def convert_dds_to_tga(dds_path, tga_path):
    try:
        # DDS Bild öffnen
        img = Image.open(dds_path)

        # Konvertieren und als TGA speichern
        img.save(tga_path, format='TGA')
        print(f"Konvertierung erfolgreich: {dds_path} -> {tga_path}")

    except Exception as e:
        print(f"Fehler bei der Konvertierung: {e}")

def convert_directory():
    script_directory = os.path.dirname(os.path.realpath(__file__))  # Das aktuelle Verzeichnis des Skripts

    for filename in os.listdir(script_directory):
        if filename.lower().endswith(".dds"):  # Prüfen, ob die Datei eine .dds- oder .DDS-Datei ist
            dds_path = os.path.join(script_directory, filename)
            tga_path = os.path.join(script_directory, filename.rsplit(".", 1)[0] + ".tga")
            convert_dds_to_tga(dds_path, tga_path)

    # Lösche alle .dds und .DDS Dateien nach der Konvertierung
    for filename in os.listdir(script_directory):
        if filename.lower().endswith(".dds"):  # Prüfen, ob die Datei eine .dds- oder .DDS-Datei ist
            file_path = os.path.join(script_directory, filename)
            try:
                os.remove(file_path)
                print(f"Datei gelöscht: {file_path}")
            except Exception as e:
                print(f"Fehler beim Löschen der Datei {file_path}: {e}")

if __name__ == "__main__":
    convert_directory()
