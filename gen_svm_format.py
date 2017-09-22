# -*- coding:utf-8 -*-  
# file: FileMerage.py  
#  
  
import os  
import random
import re

mergefiledir = os.getcwd()+'\\'+'vectorized_data'
filenames = os.listdir(mergefiledir)  

if os.path.isdir(mergefiledir):
	if not os.path.isdir(os.path.join(os.getcwd(), 'svm_format_data')):
		os.mkdir(os.path.join(os.getcwd(), 'svm_format_data'))

for filename in filenames:
	output_path = os.getcwd()+'\\'+'svm_format_data'+'\\'+filename
	output = open( output_path,'w')  
	filepath = mergefiledir+'\\'+filename  
	for line in open(filepath):  	
		m = re.match('(.+).txt\$\$(.+)', line)
		author = m.group(1)
		output.write(author)
		vectors = m.group(2)
		vector_list = re.split(' ',vectors)
		for i,v in enumerate(vector_list):
			output.write(' '+str(i+1)+':'+v)
		output.write('\n')				
		
	output.close()  



