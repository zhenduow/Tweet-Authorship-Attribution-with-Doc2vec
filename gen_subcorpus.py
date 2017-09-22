# -*- coding:utf-8 -*-  
# file: FileMerage.py  
#  
  
import os  
import random
import re

author_num=1000
text_num=200

mergefiledir = os.getcwd()+'\\'+'svm_format_data'
foldernames = os.listdir(mergefiledir)  

author_list=[]
for foldername in foldernames:
	author_list.append(foldername)

random_author_list = random.sample(author_list, author_num)


output = open( 'random_subset_of_corpus.txt','w')  
for author_name in random_author_list:
	filepath = mergefiledir+'\\'+author_name  
	count=0
	for line in open(filepath):  
		count+=1	
		if count<=text_num:
			m = re.match('(\S+) (.+)', line)
			author = m.group(1)
			output.write(str(random_author_list.index(author_name)))
			output.write(' ')
			output.write(m.group(2)) 
			output.write('\n')				

output.close()  



