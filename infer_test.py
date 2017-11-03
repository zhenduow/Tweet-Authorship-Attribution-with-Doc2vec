# -*- coding:utf-8 -*-
import gensim.models as g
import codecs
import os

'''
Load the saved doc2vec model and infer docvecs for the authorship attribution set.
'''

#inference hyper-parameters
start_alpha=0.01
infer_epoch=100

#load model
model="model.bin"
m = g.Doc2Vec.load(model)

#make folders for the inference vecs	
mergefiledir = os.getcwd()+'\\'+'ebd_data'
if os.path.isdir(mergefiledir):
	if not os.path.isdir(os.path.join(mergefiledir, 'embedding')):
		os.mkdir(os.path.join(mergefiledir, 'embedding'))
filenames = os.listdir(mergefiledir)  

#infer test vectors
for filename in filenames:  
	test_docs = mergefiledir+'\\'+filename  
	output_path = mergefiledir+'\\'+'embedding'+'\\'+filename
	test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]
	output = open(output_path, "w")
	for d in test_docs:
		output.write( filename +"$$" )
		output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )
	output.flush()
	output.close()
