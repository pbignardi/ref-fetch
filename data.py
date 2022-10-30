from abstract_result import AbstractResult
from typing import Iterator

class ResultData:
    """
    Data class for search results.
    
    This class contains all the information required for displaying the results table.

    Fields:
    - search: the text used for the search on scholar
    - results: result of the search on scholarly
    - start: the 
    """
    def __init__(
        self,
        search: str, 
        q: Iterator[AbstractResult]):

        # search text used on Scholar
        self.search = search
        # output of the search from the scholarly interface
        self.__q = q
        # set of indices with selected publications
        self.selected = set()
        # list of instantiated results from the search
        self.results = []
        self.init_results(30)

    
    def init_results(self, n = 10):
        """Initialize results from __q and puts them in results.
        
        __q is an iterator of AbstractResults, so calling next on its elements never get the same element twice."""
        self.results += [next(self.__q) for _ in range(n)]

    def add_results(self, new_res):
        self.selected.update(new_res)
    
    def rm_results(self, to_del):
        self.selected.difference_update(to_del)            


class ResultParameters:
    """
    Class for results parameters

    This class contains the parameters for displaying 
    """
    def __init__(self):
        # index of first element to display
        self._start = 0 
        # number of elements to display
        self._n_it = 10
        # last command given
        self._cmd = ""
        # list of admissible commands
        self._legal_cmds = ["n", "p", "s", "q"]
    
    # Get/set for _start
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, start: int):
        if start >= 0:
            self._start = start
    
    # Get/set for _n_it
    @property
    def n_it(self):
        return self._n_it
    
    @n_it.setter
    def n_it(self, n_it: int):
        if n_it > 0:
            self._n_it = n_it


    # Get/set for _cmd
    @property
    def cmd(self):
        return self._cmd
    
    @cmd.setter
    def cmd(self, cmd):
        if cmd in self._legal_cmds:
            self._cmd = cmd
        else:
            self._cmd = ""
    
    

    


    
