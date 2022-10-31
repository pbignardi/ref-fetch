from dataclasses import dataclass
from abstract_result import AbstractResult
from typing import Iterator, List
from sys import exit

@dataclass
class Configuration:
    def __init__(
        self,
        n_it: int = 10, 
        keys: dict = {
            "next": "n", 
            "previous": "p", 
            "select": "s", 
            "quit": "q"}):
        self.n_it = n_it
        self.cmds = keys
    
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
        q: Iterator[AbstractResult],
        config: Configuration):

        ## RESULT DATA
        # search text used on Scholar
        self.search = search
        # set of indices with selected publications
        self.selected = set()

        # output of the search from the scholarly interface -> iterator
        self.__q: Iterator = q
        # list of instantiated results from the search
        # index of last initialized element
        self.__last = -1
        # list of initialized elements
        self.__results = []
        # result parameter reference
        
        ## PARAMETER DATA
        self._n_it = config.n_it 
        self._start = 0
        self._cmd = ""
        self.__config = config
        self.__selectmode = False
        # iterator __q is finished
        self.__empty_iter = False
    
    @property
    def config(self):
        return self.__config

    @property
    def select_mode(self):
        return self.__selectmode

    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, start: int):
        # ignore if start is negative
        if start < 0:
            return
        # when iterator is empty, ignore whenever start >= #results - n_it
        if self.__empty_iter:
            if start > len(self.__results) - self.n_it:
                return
        
        self._start = start
    
    @property
    def n_it(self):
        return self._n_it

    @property
    def cmd(self):
        return self._cmd
    
    @cmd.setter
    def cmd(self, new_cmd):
        if new_cmd in self.config.cmds.values():
            self._cmd = new_cmd
            if new_cmd == self.config.cmds["next"]:
                self.start += 1
            if new_cmd == self.config.cmds["previous"]:
                self.start -= 1
            if new_cmd == self.config.cmds["select"]:
                self.__selectmode = True
            if new_cmd == self.config.cmds["quit"]:
                exit()

        else:
            self._cmd = ""

    def __init_results(self, n = 10):
        """
        Initialize results from __q and put them in results.
        
        __q is an iterator of AbstractResults, so calling next on its elements never get the same element twice.
        """

        try:
            self.__results += [next(self.__q) for _ in range(n)]
        except StopIteration:
            self.__empty_iter = True
        finally:
            self.__last = len(self.__results) - 1



    @property
    def results(self):
        if self.__last < self.start + self.n_it - 1:
            to_init = self.start + self.n_it - 1 - self.__last
            self.__init_results(to_init)
        return self.__results

    @property
    def visible(self):
        return self.results[self.start:self.start + self.n_it - 1]


    def add_results(self, new_res):
        self.selected.update(new_res)
    
    def rm_results(self, to_del):
        self.selected.difference_update(to_del)            



    


    
