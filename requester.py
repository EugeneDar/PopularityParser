import time
import requests
import pandas as pd
import numpy as np

ex_data = pd.read_excel('methods2.xlsx')

all_names_methods = np.array(ex_data['METHOD_NAMES'].values)

language_names = np.array(('Java', 'Ruby', 'Python', 'C++', 'JavaScript', 'Go', 'C#', 'Swift', 'PHP', 'Rust'))

all_lang_methods = np.ndarray((0, all_names_methods.size))

for lang in language_names:
    x = np.array(ex_data[lang].values.tolist())
    x = x.reshape((1, x.size))
    all_lang_methods = np.concatenate((all_lang_methods, x), axis=0)

dictionary = {}

results = {}

for i in range(language_names.size):
    for j in range(all_lang_methods.shape[1]):
        value = str(all_lang_methods[i][j])
        if value != "nan":
            dictionary[value] = all_names_methods[j]
            results[value] = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

token = ""

token2 = ""

headers = {
    'Authorization': ('Token ' + token)
}

for lang in language_names:
    print('\n%s started\n' % lang)
    methods = list(filter(lambda w: str(w) != "nan", ex_data[lang].values))

    for method in methods:
        good = False

        while not good:
            url = "https://api.github.com/search/code?q=%s+in:file+language:%s" % (method, lang)
            response = requests.request("GET", url, headers=headers).json()
            try:
                x = response['total_count']
                print(method, x, dictionary[method])
                results[dictionary[method]] = int(str(x))
                good = True
            except:
                time.sleep(10)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print(results)
