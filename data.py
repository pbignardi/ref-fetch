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
            "down": "j",
            "up": "k",
            "pg_down": "n", 
            "pg_up": "p", 
            "select": "s", 
            "quit": "q",
            "clear": "c"}):
        self.n_it = n_it
        self.cmds = keys
        self.current_color = "green"
        self.select_color = "cyan"
        self.command_color = "orange3"
        
    
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
        self.__nit = config.n_it 
        self.__start = 0
        self.__cmd = ""
        self.__config = config
        self.__current = 0
        # iterator __q is finished
        self.__empty_iter = False
    
    @property
    def config(self):
        return self.__config

    @property
    def current(self):
        return self.__current

    @property
    def start(self):
        return self.__start
    
    @start.setter
    def start(self, start: int):
        # ignore if start is negative
        if start < 0:
            return
        # when iterator is empty, ignore whenever start >= #results - n_it
        if self.__empty_iter:
            if start > len(self.__results) - self.n_it:
                return
        
        self.__start = start
    
    @property
    def n_it(self):
        return self.__nit

    @property
    def cmd(self):
        return self.__cmd
    
    @cmd.setter
    def cmd(self, new_cmd):
        if new_cmd in self.config.cmds.values():
            self.__cmd = new_cmd
            if new_cmd == self.config.cmds["down"]:
                self.down()
            if new_cmd == self.config.cmds["up"]:
                self.up()
            if new_cmd == self.config.cmds["pg_down"]:
                self.pg_down()
            if new_cmd == self.config.cmds["pg_up"]:
                self.pg_up()
            if new_cmd == self.config.cmds["select"]:
                self.select()
            if new_cmd == self.config.cmds["clear"]:
                self.clear()
            if new_cmd == self.config.cmds["quit"]:
                exit()

        else:
            self.__cmd = ""

    def pg_down(self):
        """Set visible elements to the next page"""
        self.start += self.n_it
        self.__current = self.start + 1
    
    def pg_up(self):
        """Set visible elements to the previous page"""
        self.start -= self.n_it
        self.__current = self.start + 1

    def select(self):
        """Add the currently highlighted element if 
        it is not in the selected dict, else it is removed"""
        if self.current in self.select:
            self.rm_results([self.current])
        else:
            self.add_results([self.current])

    def clear(self):
        """Clear all the selected items"""
        self.selected.clear()        

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

    def down(self):
        if self.__empty_iter:
            if self.__current + 1 > self.__last:
                return

        self.__current += 1

        visible_end = self.start + self.n_it - 1
        # if newly selected is ad the bottom of the table, increase start by 1
        if self.current >= visible_end:
            self.start += 1
        
        

    def up(self):    
        if self.__current - 1 < 0:
            return
        
        self.__current -= 1

        visible_start = self.start
        if self.current <= visible_start:
            self.start -= 1


    @property
    def results(self):
        if self.__last < self.start + self.n_it - 1:
            to_init = self.start + self.n_it - 1 - self.__last
            self.__init_results(to_init)
        return self.__results

    @property
    def visible(self):
        return self.results[self.start:self.start + self.n_it]


    def add_results(self, new_res):
        self.selected.update(new_res)
    
    def rm_results(self, to_del):
        self.selected.difference_update(to_del)            



    


    
