# Authorship-Attribution-with-Doc2vec
Using doc2vec on authorship attribution task

This model uses doc2vec as the embedding for a whole twitter post. Then it applies the convolutional neural network to solve the authorship attribution task as a classification problem.

How to use:

1. Prepare a corpus as training set for doc2vec (name as ebd_train.txt & copy to current dir). The training set should consist of lines of tweets. One tweet per line, one line per tweet. 
2. Prepare a test set for authorship attribution (name as (author_id).txt & copy to 'data' dir). The test set should consist of files with tweets sorted by author. One file per author, one author per file. In each file, there should be one line per tweet, one tweet per line.
3. Then run the scripts in the following order:
a. train_model.py
b. infer_test.py (will report a trivial error which does not affect normal use.)
c. clean.py
d. gen_clf_train_test.py
e. cnn.py

4. Results are shown by classification accuracy.
