import requests
import re
import string
from bs4 import BeautifulSoup
import lxml.html.clean

urls_file = open('io_text_resources/unique_urls.txt', 'r')

links = urls_file.readlines()
file_read_count = 0
counter = 0
for link in links:
    try:
        url = "https://www.presstv.com/Detail/2020/10/07/635854/India-Dhananjay-Tingal-Syed-Arshad-Mehdi-Aakash-"
        res = requests.get(link)
        html_page = res.content
        out = lxml.html.clean.clean_html(html_page)
        output = str(out)
        st = re.sub(r'<.+?>', '', output)

        st = re.sub(r'\\r', '', st)
        st = re.sub(r'\\n', '', st)
        st = re.sub(r'\\t', '', st)
        st = re.sub(' +', ' ', st)

        slimmedpath = "./io_text_resources/Cleaner/slimmed_text" + str(counter) + ".txt"
        with open(slimmedpath, 'a') as cleanfile:
            cleanfile.write(link + '\n')
            cleanfile.writelines(str(st))
        rawpath = "./io_text_resources/Raw/raw_text" + str(counter) + ".txt"
        with open(rawpath, 'a') as rawfile:
            rawfile.write(link + '\n')
            rawfile.write(str(html_page))
        print("file number " + str(file_read_count) + " read")
        counter += 1
        file_read_count += 1

    except:
        print("Nothing read from file " + str(file_read_count))

password_regex = re.compile(r'^(?:(?:(?=(.*[0-9])(.*\S))(?=(.*[a-z])(.*\S))(?=(.*[A-Z])(.*\S)))|(?:(?=(.*[a-z])(.*\S))(?=(.*[A-Z])(.*\S))(?=(.*[*.!@$%^&(){}[]:;<>,.?/~\+-=|\])(.*\S)))|(?:(?=(.*[0-9])(.*\S))(?=(.*[A-Z])(.*\S))(?=(.*[*.!@$%^&(){}[]:;<>,.?/~\+-=|\])(.*\S)))|(?:(?=(.*[0-9])(.*\S))(?=(.*[a-z])(.*\\S))(?=(.*[*.!@$%^&(){}[]:;<>,.?/~\+-=|\])(.*\S)))).{8,32}$')
