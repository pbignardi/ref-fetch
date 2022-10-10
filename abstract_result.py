from abc import ABC, abstractmethod
from typing import Iterable

class AbstractResult(ABC):
    """
    Abstract class for the results of the fetching from Scholar
    """
    # Property
    @property
    @abstractmethod
    def title(self):
        """Title of the publication"""
        pass
    @property
    @abstractmethod
    def author(self):
        """Author of the publication"""
        pass
    @property
    @abstractmethod
    def venue(self):
        """Venue where the publication appeared"""
        pass
    @property
    @abstractmethod
    def n_cit(self):
        """Number of citation of the publication"""
        pass
    @property
    @abstractmethod
    def year(self):
        """Year of publication"""
        pass
    @property
    @abstractmethod
    def abstract(self):
        """Abstract of the publication"""
        pass

    # Methods
    @abstractmethod
    def get_bibtex(self):
        """Recover the bibtex file of the publication"""
        pass

    

