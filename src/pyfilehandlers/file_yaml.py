"""file_yaml.py

Contains a class that handles YAML file IO.
"""

from .file_extension import FileExtension
from lunapyutils import handle_error
from ruamel.yaml import YAML
from pathlib import Path

from typing import Any



class YAMLFile(FileExtension):
    """
    Class that handles YAML file IO.

    Attributes
    ----------
    path : pathlib.Path
        absolute path of the file to be managed
    """

    def __init__(self, path: Path) -> None:
        """
        Creates YAMLFile instance.

        Attributes
        ----------
        path : pathlib.Path
            absolute path of the file to be managed
        """

        super().__init__(path = path, extension_suffix = '.yaml')


    def read(self) -> dict | None:
        """
        Opens YAML file and returns its data.

        Returns
        -------
        dict
            the data contained in the file | 
            None is there was an error
        """

        data = None
        try:
            with open(self.path, 'r') as f:
                yaml = YAML(typ='safe')
                data = yaml.load(f)

        except IOError as e:
            handle_error(e, 'YAMLFile.open()',
                         'error opening file')

        except Exception as e:
            handle_error(e, 'YAMLFile.open()', 
                         'erroneous error opening file')

        finally:
            return data
        

    def write(self, data: dict[str, Any]) -> bool:
        """
        Writes data to YAML file.

        Parameters
        ----------
        data : dict[str, Any]
            the data to write to the file

        Returns
        -------
        bool
            True,  if the data was written to the file |
            False, otherwise
        """

        saved = False
        try: 
            with open(self.path, 'w') as f:
                yaml = YAML()
                yaml.dump(data, f)
                saved = True
        
        except Exception as e:
            handle_error(e, 'YAMLFile.write()', 'error writing to file')

        finally:
            return saved
        

    def print(self) -> None:
        """
        Opens the yaml file and prints the data.
        """

        data = self.read()
        print(data)