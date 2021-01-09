import re
import pandas as pd
import os

allwords = []

path, dirs, files = next(os.walk('io_text_resources/Cleaner/'))
for i in range(len(files)-1):
    filename = 'io_text_resources/Cleaner/slimmed_text%s.txt' % i
    with open(filename, 'r') as file:
        file_content = file.read()
    print('filecontent: ' + file_content )
    file_content = re.sub('[\b\n\t]',' ', file_content)

    file_content = file_content.split(' ')

    for word in file_content:
        for w in allwords:
            if word != w:
                allwords.append(word)

print(allwords)