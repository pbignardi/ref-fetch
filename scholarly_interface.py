from abstract_result import AbstractResult
from scholarly import scholarly, ProxyGenerator
from typing import Iterable
from console import console


class ScholarlyResult(AbstractResult):
    def __init__(self, result: dict):
        self.result = result
    
    @property
    def title(self):
        try:
            title = self.result["bib"]["title"]
        except KeyError:
            return "" 
        return title

    @property
    def author(self):
        try:
            author_list = self.result["bib"]["author"]
            author = ", ".join(author_list)
        except KeyError:
            return "" 
        return author 

    @property
    def venue(self):
        try:
            venue = self.result["bib"]["venue"]
        except KeyError:
            return "" 
        return venue 

    @property
    def n_cit(self):
        try:
            n_cit = str(self.result["num_citations"])
        except KeyError:
            return "" 
        return n_cit 

    @property
    def year(self):
        try: 
            year = str(self.result["bib"]["pub_year"])
        except KeyError:
            return "" 
        return year

    @property
    def abstract(self):
        try: 
            abstract = self.result["bib"]["abstract"]
        except KeyError:
            return "" 
        return abstract 

    def get_bibtex(self):
        return scholarly.bibtex(self.result)

def scholarly_search(query: str):
    pg = ProxyGenerator()

    console.print("[bold]->[/bold] [info]Connecting to proxy...[/info]")
    scholarly.use_proxy(pg)

    console.print("[bold]->[/bold] [info]Searching on Google Scholar...[/info]")
    query_results = scholarly.search_pubs(query)
    query_results = map(ScholarlyResult, query_results)
    return query_results

def init_results(q: Iterable[ScholarlyResult], n = 10):
    return [next(q) for i in range(n)]
    

    