# This principle states - A class should have only one reason to change.
# This means that a class should have only one responsibility, as expressed through its methods.

from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

# As shown in the example, It's best to define two classes to handle Files and ZipFiles respectively,
# rather than defining a single class to handle operations on two kinds of files
# In this way, we can make sure that every class has only single responsibility


