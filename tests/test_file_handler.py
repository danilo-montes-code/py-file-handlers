from src.pyfilehandlers.file_handler import FileHandler
from src.pyfilehandlers.file_txt import TxtFile

from pathlib import Path

class TestFileHandler:

    def test__determine_file_extension_object(self):
        fh = FileHandler(Path('test.txt'))
        assert fh._determine_file_extension_object() == TxtFile