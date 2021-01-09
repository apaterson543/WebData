# Homework 9 - Email Classification
**Andrew Paterson CS 432** 



### Q1. Create two datasets, Testing and Training.

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

### Q2. Naive Bayes classifier
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

### Q3. Confusion Matrix

Overall, the classification was pretty good. One email however, one from my bank telling me my statement was ready showed up in Advertisement.
Test results are usually only as good as your training data so I think possibly with a larger training set with more examples similar to the false positive 
the confusion could be reduced or eliminated.

|               | Advertisement | Other |
|:--------------|:-------------:|:-----:|
| Advertisement |      5        |   1   |
| Other         |      0        |   4   |

## Extra Credit

### Q4. 
*(Extra credit, 1 point)* 

Report the precision and accuracy scores of your classification results (see Week-13 Document Filtering, slide 43).

### Q5. 
*(Extra credit, 2 points)* 

Tune your classifier by updating weights to obtain better classification results. You may want to change the default weights (`weight`, `ap`) given to `weightedprob()` or the threshold used for the Bayesian classifier or change how the words are extracted from the document (for this you will need to re-train the model).  Report the changes you made, re-run your Testing dataset, and show that the performance improved (either by using the confusion matrix or by computing precision and accuracy).

### Q6. 
*(Extra credit, 4 points)* 

Implement the classifier with the Multinomial model instead of the multiple Bernoulli model and re-run Q2 and Q3.  Did the classification improve?  *Make sure to remove the unique word filter from the extractor.*

*For credit on this part, you must describe what you have done and discuss the differences between the Multinomial model and the multiple Bernoulli model.*

## Submission

Make sure that you have committed and pushed your local repo to GitHub.  Your repo should contain any code you developed to answer the questions.  Include "Ready to grade @weiglemc @brutushammerfist" in your final commit message. 

Submit the URL of your *report* in Blackboard:

* Click on HW9 under Assignments in Blackboard
* Under "Assignment Submission", click the "Write Submission" button.
* Copy/paste the URL of your report into the edit box
  * should be something like https<nolink>://github.com/cs432-websci-fall20/hw9-classify-*username*/blob/master/HW9-report.{pdf,md}
* Make sure to "Submit" your assignment.
