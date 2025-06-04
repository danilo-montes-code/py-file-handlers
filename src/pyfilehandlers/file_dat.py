"""file_dat.py

Contains a class that handles dat file IO.
Class is written as an abstract class.
"""

from .file_extension import FileExtension
from lunapyutils import *
from pathlib import Path
from abc import ABC, abstractmethod

from typing import Any



class DatFile(FileExtension, ABC):
    """
    Class that handles dat file IO.

    Attributes
    ----------
    path : pathlib.Path
        absolute path of the file to be managed
    """

    def __init__(self, path: Path) -> None:
        """
        Creates DatFile instance.

        Attributes
        ----------
        path : pathlib.Path
            absolute path of the file to be managed
        """

        super().__init__(path = path, extension_suffix = '.dat')

    @abstractmethod
    def read(self) -> Any | None:
        """
        Opens dat file and returns its data.

        Returns
        -------
        Any
            the data contained in the file | 
            None is there was an error
        """
        pass


    @abstractmethod
    def write(self, data: Any) -> bool:
        """
        Writes data to dat file. Overwrites all data held in file.

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
        pass


    @abstractmethod
    def print(self) -> None:
        """
        Opens the dat file and prints the data.
        """
        pass