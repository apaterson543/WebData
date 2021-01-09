import math
import csv

page_text = ''
count = 0
chart_path = "io_text_resources/Charts/TF_IDF_web.csv"
chart = open(chart_path, 'w+')
chart.close()
all_values = []
chart_headers = ['TF-IDF', 'TF', 'IDF', 'URI']
all_values.append(chart_headers)
# chart = open(chart_path, "a")

for count in range(10):
    filepath = "./io_text_resources/TopTen/top_ten" + str(count) + '.txt'

    with open(filepath, 'r') as file:
        all_lines = file.readlines()

    uri = all_lines[0].strip()
    page_text = all_lines[3]
    term_count = int(all_lines[4])
    total_words = len(str(page_text).split())

    TF = term_count / total_words

    docs_with_term = 357
# count_path = 'io_text_resources/TopTen/number_of_files_containing_term.txt'
# with open(count_path) as inpt:
#     count_in_corpus = inpt.readline()
#     twitter links
    # docs_in_corpus = 979
    #Bing
    docs_in_corpus = 10000000000
    IDF = math.log((docs_in_corpus / docs_with_term), 2)
    TF_IDF = TF * IDF
    page_values = [TF_IDF,TF,IDF,uri]
    all_values.append(page_values)

print(all_values)
with open(chart_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(all_values)