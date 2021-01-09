from NaiveBayes import naivebayes, classifier, getwords
import re

def preprocess_words_from_file(filepath):
    file = open(filepath)
    words = file.read()
    # words = getwords(doc)
    #words = re.sub(r'[^a-zA-Z ]+', ' ', words)
    #words = re.sub('\s+',' ',words)
    list_of_words = words.split(' ')
    final_list = []
    for word in list_of_words:
        final_list.append(word.lower())
    words = ' '.join(final_list)
    return words


train1_ad = preprocess_words_from_file('TrainingData/Advertisement/ad0.txt')
train2_ad = preprocess_words_from_file('TrainingData/Advertisement/ad1.txt')
train3_ad = preprocess_words_from_file('TrainingData/Advertisement/ad2.txt')
train4_ad = preprocess_words_from_file('TrainingData/Advertisement/ad3.txt')
train5_ad = preprocess_words_from_file('TrainingData/Advertisement/ad4.txt')
train6_ad = preprocess_words_from_file('TrainingData/Advertisement/ad5.txt')
train7_ad = preprocess_words_from_file('TrainingData/Advertisement/ad6.txt')
train8_ad = preprocess_words_from_file('TrainingData/Advertisement/ad7.txt')
train9_ad = preprocess_words_from_file('TrainingData/Advertisement/ad8.txt')
train10_ad = preprocess_words_from_file('TrainingData/Advertisement/ad9.txt')
train11_ad = preprocess_words_from_file('TrainingData/Advertisement/ad10.txt')
train12_ad = preprocess_words_from_file('TrainingData/Advertisement/ad11.txt')
train13_ad = preprocess_words_from_file('TrainingData/Advertisement/ad12.txt')
train14_ad = preprocess_words_from_file('TrainingData/Advertisement/ad13.txt')
train15_ad = preprocess_words_from_file('TrainingData/Advertisement/ad14.txt')
train16_ad = preprocess_words_from_file('TrainingData/Advertisement/ad15.txt')
train17_ad = preprocess_words_from_file('TrainingData/Advertisement/ad16.txt')
train18_ad = preprocess_words_from_file('TrainingData/Advertisement/ad17.txt')
train19_ad = preprocess_words_from_file('TrainingData/Advertisement/ad18.txt')
train20_ad = preprocess_words_from_file('TrainingData/Advertisement/ad19.txt')

train1_o = preprocess_words_from_file('TrainingData/Other/o0.txt')
train2_o = preprocess_words_from_file('TrainingData/Other/o1.txt')
train3_o = preprocess_words_from_file('TrainingData/Other/o2.txt')
train4_o = preprocess_words_from_file('TrainingData/Other/o3.txt')
train5_o = preprocess_words_from_file('TrainingData/Other/o4.txt')
train6_o = preprocess_words_from_file('TrainingData/Other/o5.txt')
train7_o = preprocess_words_from_file('TrainingData/Other/o6.txt')
train8_o = preprocess_words_from_file('TrainingData/Other/o7.txt')
train9_o = preprocess_words_from_file('TrainingData/Other/o8.txt')
train10_o = preprocess_words_from_file('TrainingData/Other/o9.txt')
train11_o = preprocess_words_from_file('TrainingData/Other/o10.txt')
train12_o = preprocess_words_from_file('TrainingData/Other/o11.txt')
train13_o = preprocess_words_from_file('TrainingData/Other/o12.txt')
train14_o = preprocess_words_from_file('TrainingData/Other/o13.txt')
train15_o = preprocess_words_from_file('TrainingData/Other/o14.txt')
train16_o = preprocess_words_from_file('TrainingData/Other/o15.txt')
train17_o = preprocess_words_from_file('TrainingData/Other/o16.txt')
train18_o = preprocess_words_from_file('TrainingData/Other/o17.txt')
train19_o = preprocess_words_from_file('TrainingData/Other/o18.txt')
train20_o = preprocess_words_from_file('TrainingData/Other/o19.txt')

cl = naivebayes(getwords)
cl.setdb('Ad_vs_other.db')

cl.train(train1_ad,'Advertisement')
cl.train(train2_ad,'Advertisement')
cl.train(train3_ad,'Advertisement')
cl.train(train4_ad,'Advertisement')
cl.train(train5_ad,'Advertisement')
cl.train(train6_ad,'Advertisement')
cl.train(train7_ad,'Advertisement')
cl.train(train8_ad,'Advertisement')
cl.train(train9_ad,'Advertisement')
cl.train(train10_ad, 'Advertisement')
cl.train(train11_ad, 'Advertisement')
cl.train(train12_ad, 'Advertisement')
cl.train(train13_ad, 'Advertisement')
cl.train(train14_ad, 'Advertisement')
cl.train(train15_ad, 'Advertisement')
cl.train(train16_ad, 'Advertisement')
cl.train(train17_ad, 'Advertisement')
cl.train(train18_ad, 'Advertisement')
cl.train(train19_ad, 'Advertisement')
cl.train(train20_ad, 'Advertisement')

cl.train(train1_o, 'Other')
cl.train(train2_o, 'Other')
cl.train(train3_o, 'Other')
cl.train(train4_o, 'Other')
cl.train(train5_o, 'Other')
cl.train(train6_o, 'Other')
cl.train(train7_o, 'Other')
cl.train(train8_o, 'Other')
cl.train(train9_o, 'Other')
cl.train(train10_o, 'Other')
cl.train(train11_o, 'Other')
cl.train(train12_o, 'Other')
cl.train(train13_o, 'Other')
cl.train(train14_o, 'Other')
cl.train(train15_o, 'Other')
cl.train(train16_o, 'Other')
cl.train(train17_o, 'Other')
cl.train(train18_o, 'Other')
cl.train(train19_o, 'Other')
cl.train(train20_o, 'Other')

cl.setthreshold('Advertisement', 3.0)














