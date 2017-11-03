# Authorship-Attribution-with-Doc2vec
Using doc2vec on authorship attribution task

This model uses doc2vec as the embedding for a whole twitter post. Then it applies the convolutional neural network to solve the authorship attribution task as a classification problem.

How to use:

0. Install "gensim.models" and "keras" in python.

1. Prepare a corpus as training set for doc2vec (name as ebd_train.txt & copy to current dir). The training set should consist of lines of tweets. One tweet per line, one line per tweet. I used a cleaned version of dataset in a previous work about AA on tweets (R. Schwartz, O. Tsur, A. Rappoport, and M. Koppel. 2013. Authorship attribution of micromessages). It can be downloaded in the following link:
https://drive.google.com/open?id=0B8vZdk3kTRJmOTZVV2JET0VuQ2c
A zip file named "sample_data.rar" is also included in the project. One can download and check it out.
2. Prepare a test set for authorship attribution (name as (author_id).txt & copy to 'data' dir). The test set should consist of files with tweets sorted by author. One file per author, one author per file. In each file, there should be one line per tweet, one tweet per line.

3. Then run the scripts in the following order:

	a. train_model.py.
	This script uses gensim package to train doc2vec model with input corpus (ebd_train.txt) and save the model with the name "model". If you have a pretrained model in binary file, you can skip this step and rename your pretrained model as "model" and copy to the main dir.
	
	b. infer_test.py. (will report a trivial error which does not affect normal use.)
	This script imports the doc2vec model trained by "train_model.py" and infer vector representation for the tweets in test set in "data" dir. The test set is both the test set for doc2vec and the whole set for authorship attribution.
	
	c. clean.py.
	This script cleans and formats the vector representation in a format that can be directly used by libsvm package. 
	
	d. gen_clf_train_test.py.
	This script randomly samples a set with custom size (authornumber * tweetnumber) and divides the sample set into training set and test set (training:test == 4:1) for the classifier.
	
	e. cnn.py.
	This script uses CNN classifier based on keras package to carry out the classification.

4. Results are shown by classification accuracy.
