import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def similarities(needle, haystack):
    return process.extract(needle, haystack)[0]

welcome_titles_df = pd.read_csv('./welcome-titles-to-match.csv', names=['title'])
#welcome_titles_df.rename(index=str, columns={'Journal title':'title'}, inplace=True)

pubmed_titles = pd.read_csv('./pubmed-titles.txt', delimiter=';', header=None, names=['abbreviation', 'title'])

for i in welcome_titles_df.title:
    data = similarities(i, pubmed_titles.title)
    abbr = pubmed_titles.loc[pubmed_titles['title'] == similarities(i, pubmed_titles.title)[0], 'abbreviation']
    abbr = list(abbr)
    print(i, ',', data, ',', abbr)
