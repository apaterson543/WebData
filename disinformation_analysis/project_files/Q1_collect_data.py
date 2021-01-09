import requests
from requests.exceptions import Timeout
import pandas as pd

uris_frame = pd.read_csv("expanded-URLs.csv")
final_uris = []
status_codes = []
redirect = []
count = 0

for index,row in uris_frame.iterrows():
    init_uri = row['Article URL']
    print(init_uri)

    try:
        response = requests.get(init_uri, timeout=20)
        final_uri = response.url
        final_uris.append(response.url)
        status_codes.append(response.status_code)

        if str(final_uri) == str(init_uri):
            redirect.append(False)
        else:
            redirect.append(True)
        print(final_uri)
        print(response)

    except:
        final_uris.append("Not reached")
        status_codes.append("Connection Failed")
        redirect.append(False)

uris_frame['Final URL'] = final_uris
uris_frame['Status Code'] = status_codes
uris_frame['Redirect'] = redirect
uris_frame.to_csv('D2_extended.csv')