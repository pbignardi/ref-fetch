from abstract_result import AbstractResult
from scholarly import scholarly

class ScholarlyResult(AbstractResult):
    def __init__(self, result: dict):
        self.result = result
    
    @property
    def title(self):
        return self.result["bib"]["title"]

    @property
    def author(self):
        return self.result["bib"]["author"]

    @property
    def venue(self):
        return self.result["bib"]["venue"]

    @property
    def n_cit(self):
        return self.result["num_citations"]

    @property
    def year(self):
        return self.result["bib"]["year"]

    @property
    def abstract(self):
        return self.result["bib"]["abstract"]


    def get_bibtex(self):
        return scholarly.bibtex(self.result)

def scholarly_search(query: str):
    query_results = scholarly.search_pubs(query)
    query_results = map(ScholarlyResult, query_results)
    return query_results
    

    