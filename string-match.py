import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

welcome = pd.read_csv('./WELLCOME_APCspend2013_forThinkful.csv',encoding='iso8859_15')

def simularities(needle, haystack):
    return process.extract(needle, haystack)[0]

j_titles_1 = pd.DataFrame(welcome['Journal title'].unique())
j_titles_1.rename(index=int, columns={0:'title'},inplace=True)

titles_pubmed = pd.read_csv('./titles_pubmed.txt', delimiter=';', header=None,
                             names=['abbreviation', 'title'])

for i in j_titles_1.title.head(5):
    result = simularities(i, titles_pubmed.title)
    print(i, result)
