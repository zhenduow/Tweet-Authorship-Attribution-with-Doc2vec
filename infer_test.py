#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import codecs
import os


#inference hyper-parameters
start_alpha=0.01
infer_epoch=100

#load model
model="model_7.bin"
m = g.Doc2Vec.load(model)


#vectorize test set	
mergefiledir = os.getcwd()+'\\'+'classification_set'
if os.path.isdir(mergefiledir):
	if not os.path.isdir(os.path.join(mergefiledir, 'vectorized_data')):
		os.mkdir(os.path.join(mergefiledir, 'vectorized_data'))
filenames = os.listdir(mergefiledir)  

#parameters
for filename in filenames:  
	test_docs = mergefiledir+'\\'+filename  
	output_path = mergefiledir+'\\'+'vectorized_data'+'\\'+filename
	test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines() ]
	#infer test vectors
	output = open(output_path, "w")
	for d in test_docs:
		output.write( filename +"$$" )
		output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )
	output.flush()
	output.close()
