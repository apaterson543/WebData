import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))


all_tweets_cleaned = []
all_words = ''
for i in range(100):
    user_num = i
    file_name = "q1_data/tweets_by_user/user"+str(user_num)+".txt"

    with open(file_name, 'r') as file:
        user_tweets = file.read()

    user_tweets = user_tweets.split(' ', 1)
    user_tweets[1] = re.sub('@.*', ' ', user_tweets[1])
    user_tweets[1] = re.sub('https://.*', ' ', user_tweets[1])
    user_tweets[1] = re.sub('[.,\/}{"\')(:;!?+#=\-_]+', ' ', user_tweets[1])
    user_tweets[1] = re.sub(r'[^a-zA-Z ]+', ' ', user_tweets[1])
    user_tweets[1] = re.sub(r'\b\w{1,3}\b', ' ', user_tweets[1])
    user_tweets[1] = re.sub(r'\b\w{15,}\b', ' ', user_tweets[1])
    user_tweets[1] = re.sub('\s+', ' ', user_tweets[1])

    tokens = word_tokenize(user_tweets[1])

    filtered = [w for w in tokens if not w in stop_words]
    user_tweets[1] = " ".join(filtered)
    all_tweets_cleaned.append(user_tweets)
    all_words+= user_tweets[1]


all_words = all_words.split()

words = [] # no duplicates/ clean
for word in all_words:
    if word.lower() not in words:
        words.append(word.lower())

user_word_matrix = pd.DataFrame()
# dictionary of word counts for each user and add to dataframe -- allow null entries
user_count = 0
for user in all_tweets_cleaned:
    user_dict = {'screen_name': user[0]}
    user_count += 1
    print(user_count)
    user_words = user[1].split()
    for word in words:
        count = 0
        for token in user_words:
            if word == token:
                count += 1

        user_dict[str(word)] = count

    user_word_matrix = user_word_matrix.append(user_dict, ignore_index=True)
print(user_word_matrix)
user_word_matrix.to_csv('q2_data/unordered_matrix.csv', index=False)