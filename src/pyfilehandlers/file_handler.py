"""file_handler.py

Contains class that handles a single file.
"""

from .file_extension import FileExtension
from .file_dat import DatFile
from .file_txt import TxtFile
from .file_json import JSONFile
from .file_yaml import YAMLFile
from lunapyutils import *
import sys, os
from pathlib import Path

from typing import Any



SCRIPT_ROOT = Path.cwd()

class FileHandler:
    """
    A class that handles a single file's input and output.

    Attributes
    ----------
    path : pathlib.Path
        absolute path of the file to be managed
    extension : FileExtension
        handles file IO based on extension type
    """

    def __init__(
        self, 
        file_path : Path
    ) -> None:
        """
        Creates a FileHandler instance.

        Provide an absolute `pathlib.Path` path for the file. 

        Parameters
        ----------
        file_path : pathlib.Path
            the absolute path of the file to be managed, including extension
        """

        self.path = file_path
        try:
            self.extension = self._determine_file_extension_object(self.path)
        except KeyError as e:
            print_internal(text = str(e), display_error_notice = True)
            return
            
        if not self.file_exists():
            if self.create_file():
                print_internal(f'{self.path} created successfully')
            else:
                print_internal(f'error creating file {self.path}')


    @classmethod
    def from_directory_and_filename(
        cls,
        filename : str, 
        directory : str = 'data'
    ) -> None:
        """
        Creates a FileHandler instance.

        The file's path will start with the root of the script, and will
        have an optional directory (defaulted to `data/`), as well as a
        filename.      
        """
        return cls(
            full_path = Path(SCRIPT_ROOT, directory, filename)
        )


    def _determine_file_extension_object(self) -> FileExtension:
        match self.path.suffix:
            case '.txt'  : return TxtFile
            case '.yaml' : return YAMLFile
            case '.json' : return JSONFile
            case '.dat'  : return DatFile
            case _: raise KeyError('No FileHandler for given extension')


    @staticmethod
    def create_dir(dir_path : str) -> bool: 
        """
        Create directory from the root of the script.

        Parameters
        ----------
        dir_path : str
            path of the directory to be created

        Returns
        -------
        bool
            True,  if directory was created successfully or if \
                   directory already exists |
            False, otherwise
        """

        created = False
        try:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            created = True

        except FileExistsError:
            created = True

        except Exception as e:
            handle_error(e, 'FileHandler.create_dir()', 
                        'erroneous error creating data directory')

        finally:
            return created


    def create_file(self) -> bool:
        """
        Creates file at path specified in attribute.

        Returns
        -------
        bool
            True,  if file was created successfully |
            False, otherwise
        """

        file_created_successfully = False
        try:
            with open(self.path, 'a+'):
                file_created_successfully = True

        except FileNotFoundError as e:
            if not FileHandler.create_dir(os.path.dirname(self.path)):
                return False

            return self.create_file()

        except IOError as e:
            handle_error(e, 'FileHandler.create_file()', 
                         'error creating file')

        except Exception as e:
            handle_error(e, 'FileHandler.create_file()', 
                         'erroneous error creating file')

        return file_created_successfully
        

    def file_exists(self) -> bool:
        """
        Determines if file exists.

        Returns
        -------
        bool
            True,  if file exists |
            False, otherwise
        """

        return os.path.isfile(self.path)
    

    def is_empty(self) -> bool:
        """
        Determins if file is empty.

        Returns
        -------
        bool
            True,  if file is empty |
            False, otherwise
        """

        return os.stat(self.path).st_size == 0
    

    def read(self) -> Any | None:
        """
        Opens file and returns its data.

        Returns
        -------
        Any
            the data held in the file | 
            None, if file is empty
        """

        return self.extension.read() if not self.is_empty() else None
    

    def write(self, data: Any) -> bool:
        """
        Writes data to file.

        Parameters
        ----------
        data : Any
            data to write to the file
        
        Returns
        -------
        bool
            True,  if the data was written to the file successfully |
            False, otherwise
        """

        return self.extension.write(data)
    
    
    def print(self) -> None:
        self.extension.print()