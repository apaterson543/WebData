import requests
import json

urls_file = open('../output/unique_urls.txt', 'r')

links = urls_file.readlines()
flag = False
c = 0
for link in links:
    try:
        response = requests.get("http://memgator.cs.odu.edu/timemap/json/" + link)
        if response.status_code == 200 and response.json():
            timemap = response.json()
            path = '../output/timemaps/timemap' + str(c) + '.json'
            print("path: " + path)
            with open(path, "a") as outfile:
                print('writing to json')
                json.dump(timemap, outfile)
            c += 1
            outfile.close()
    except:
        print('No archive')
urls_file.close()
