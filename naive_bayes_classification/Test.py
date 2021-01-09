from NaiveBayes import naivebayes, classifier, getwords
from Q2_run_naive_bayes import preprocess_words_from_file
cl = naivebayes(getwords)
cl.setdb('Ad_vs_other.db')


test_data_results = []

for i in range(10):
    filename = "TestData/t%s.txt" % i
    test_data_results.append((filename,cl.classify(preprocess_words_from_file(filename), default='unknown')))

for tup in test_data_results:
    print(tup)