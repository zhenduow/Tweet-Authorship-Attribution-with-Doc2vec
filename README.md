# Authorship-Attribution-with-Doc2vec
Using doc2vec on authorship attribution task

This model uses doc2vec as the embedding for a whole twitter post. Then it applies the convolutional neural network to solve the authorship attribution task as a classification problem.

How to use:

0. Install "gensim.models" and "keras" in python.

1. Prepare a corpus as training set for doc2vec (name as ebd_train.txt & copy to current dir). The training set should consist of lines of tweets. One tweet per line, one line per tweet. 

2. Prepare a test set for authorship attribution (name as (author_id).txt & copy to 'data' dir). The test set should consist of files with tweets sorted by author. One file per author, one author per file. In each file, there should be one line per tweet, one tweet per line.

3. Then run the scripts in the following order:

	a. train_model.py.
	This script uses gensim package to train doc2vec model with input corpus (ebd_train.txt) and save the model with the name "model".
	
	b. infer_test.py. (will report a trivial error which does not affect normal use.)
	This script import the doc2vec model trained by "train_model.py" and infer vector representation for the tweets in test set in "data" dir.
	
	c. clean.py.
	This script clean and format the vector representation in a format that can be directly used by sklearn.svm package.
	
	d. gen_clf_train_test.py.
	This script randomly divide all the vector representations and generates training set and test set (training:test == 4:1) for classifier.
	
	e. cnn.py.
	This script uses CNN classifier based on keras package to carry out the classification.

4. Results are shown by classification accuracy.
