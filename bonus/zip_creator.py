import zipfile
import pathlib


def make_archive(filepaths, destination_folder):
    dest_path = pathlib.Path(destination_folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for f in filepaths:
            f = pathlib.Path(f)
            archive.write(f, arcname=f.name)


if __name__ == "__main__":
    make_archive(filepaths=["parsers9.py", "questions.json"], destination_folder="dest")
