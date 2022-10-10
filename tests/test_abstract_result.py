from scholarly_interface import ScholarlyResult, scholarly_search

if  __name__=="__main__":
    dicts = scholarly_search("Isogeometric BDDC Preconditioners with Deluxe Scaling")
    single_result = next(dicts)
    print(single_result.title)
    print(single_result.author)
    print(single_result.venue)
    print(single_result.n_cit)
    print(single_result.year)  
    print(single_result.abstract)
    print(single_result.get_bibtex())