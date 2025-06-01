"""file_json.py

Contains a class that handles JSON file IO.
"""

from .file_extension import FileExtension
from lunapyutils import *
import json

from typing import Any



class JSONFile(FileExtension):
    """
    Class that handles JSON file IO.

    Attributes
    ----------
    fn : str
        filename of the file
    
    Methods
    -------
    read():
        opens the file and returns its data
    write(data):
        writes data to file
    print():
        opens the file and prints the data
    """

    def __init__(self, fn: str) -> None:
        """
        Creates JSONFile instance.

        Attributes
        ----------
        fn : str
            filename of the desired file
        """

        super().__init__(fn = fn, extension_suffix = '.json')


    def read(self) -> Any | None:
        """
        Opens JSON file and returns its data.

        Returns
        -------
        Any
            the data contained in the file | 
            None is there was an error
        """

        data = None
        try:
            with open(self.fn, 'r') as f:
                data = json.load(f)

        except IOError as e:
            handle_error(e, 'JSONFile.open()',
                         'error opening file')

        except Exception as e:
            handle_error(e, 'JSONFile.open()', 
                         'erroneous error opening file')

        finally:
            return data
        

    def write(self, data : Any) -> bool:
        """
        Writes data to JSON file.

        Parameters
        ----------
        data : Any
            the data to write to the file

        Returns
        -------
        bool
            True,  if the data was written to the file |
            False, otherwise
        """

        saved = False
        try: 
            with open(self.fn, 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                saved = True
        
        except Exception as e:
            handle_error(e, 'JSONFile.write()', 'error writing to file')

        finally:
            return saved
        

    def print(self) -> None:
        """
        Opens the json file and prints the data.
        """
        
        data = self.read()
        print(json.dumps(data, indent=2))