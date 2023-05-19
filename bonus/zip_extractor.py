import zipfile


def extract_archive(arch_path, dest_folder):
    with zipfile.ZipFile(arch_path, 'r') as arch:
        arch.extractall(dest_folder)

