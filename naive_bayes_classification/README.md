# Email Classification

### Create two datasets, Testing and Training.

I recieve an obscene amount of emails that are advertisements. Many of them are things I might be interested in, however they usually go straight to my trash anyway.
Because I have a plethora of training and test data for this classification chose to pick items that were advertisements. Advertisements are still spam
but maybe a slightly more specific subset. 

The **Training** dataset I created consisted of
* 20 text documents for email messages that I received that were trying to sell something.
* 20 text documents for email messages that were from teachers, peers or my bank classified as other.

The **Testing** dataset consisted of 5 of each of these categories.

I performed some pre-processing to change letters to lowercase for this classification in accordance with the statement given in the example
that the `naivebayes` and `classification` classes would not recognize all caps.

These datasets are available in [TrainingData](TrainingData) and [TestData](TestData).

### Naive Bayes classifier
For this section, I used the `classification` and `naivebayes` classes from https://github.com/cs432-websci-fall20/assignments/blob/master/432_PCI_Ch06.ipynb to train and test the Naive Bayes classifier. 
While adding my training data, I classified the advertisement emails as *Advertisement* and the other emails as *Other*. 

```
cl = naivebayes(getwords)
cl.setdb('Ad_vs_other.db')
cl.train(train1_ad,'Advertisement')
cl.setthreshold('Advertisement', 3.0)
```
*Full code can be viewed [here](Q2_run_naive_bayes.py).*

Because this training uses SQLite database, I created another module to test the test data as to not interfere or repeat training: [Test.py](Test.py)

```
test_data_results = []

for i in range(10):
    filename = "TestData/t%s.txt" % i
    test_data_results.append((filename,cl.classify(preprocess_words_from_file(filename), default='unknown')))

for tup in test_data_results:
    print(tup)
```
From this script, the test results for each file in [TestData](TestData) were stored in a tuple and printed to the console.
```
('TestData/t0.txt', 'Advertisement')
('TestData/t1.txt', 'Other')
('TestData/t2.txt', 'Other')
('TestData/t3.txt', 'Other')
('TestData/t4.txt', 'Other')
('TestData/t5.txt', 'Advertisement')
('TestData/t6.txt', 'Advertisement')
('TestData/t7.txt', 'Advertisement')
('TestData/t8.txt', 'Advertisement')
('TestData/t9.txt', 'Advertisement')

```

### Confusion Matrix

Overall, the classification was pretty good. One email however, one from my bank telling me my statement was ready showed up in Advertisement.
Test results are usually only as good as your training data so I think possibly with a larger training set with more examples similar to the false positive 
the confusion could be reduced or eliminated.

|               | Advertisement | Other |
|:--------------|:-------------:|:-----:|
| Advertisement |      5        |   1   |
| Other         |      0        |   4   |
