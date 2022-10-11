from abstract_result import AbstractResult
from scholarly import scholarly

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
            author = self.result["bib"]["author"]
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
            n_cit = self.result["num_citations"]
        except KeyError:
            return "" 
        return n_cit 

    @property
    def year(self):
        try: 
            year = self.result["bib"]["year"]
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
    query_results = scholarly.search_pubs(query)
    query_results = map(ScholarlyResult, query_results)
    return query_results
    

    