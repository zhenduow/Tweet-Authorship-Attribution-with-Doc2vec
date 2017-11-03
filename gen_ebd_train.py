# -*- coding:utf-8 -*-  
# file: FileMerage.py  
#  
'''
Generate the trainning set for doc2vec model.
This training set is kept separated from the authorship attribution set.

From the whole dataset, sample author_num many authors,
	and then divide the set into group_size many even partitions.
Then later one can use one or one combination of several partitions as 
	authorship attribution set, others to train the doc2vec model.
Each partition of the dataset is saved in one folder.
Each partition set has (author_num/group_size) many authors and their tweets.
'''
import os  
import random
from shutil import copyfile

author_num = 7000
group_size = 50
group_num = author_num/test_size

mergefiledir = os.getcwd()+'\\'+'data'
author_names = os.listdir(mergefiledir)  

if not os.path.isdir(os.path.join(os.getcwd(), 'Sets')):
	os.mkdir(os.path.join(os.getcwd(), 'Sets'))

author_list=[]
for author_name in author_names:
	author_list.append(author_name)

random_author_list = random.sample(author_list, author_num)

for i in range(group_num):
	group = random_author_list[(i)*group_size:(i+1)*group_size]
	if not os.path.isdir(os.getcwd()+'\\'+'Sets'+'\\'+'Set_'+str(i+1)):
		os.mkdir(os.getcwd()+'\\'+'Sets'+'\\'+'Set_'+str(i+1))
	for author_name in group:
		filename = mergefiledir + '\\'+ author_name
		copyfile(filename, os.getcwd()+'\\'+'Sets'+'\\'+'Set_'+str(i+1)+'\\'+author_name)
		
output=open('ebd_train.txt','w')
for i in range(group_num):
	if i > 0:
		path = os.getcwd()+'\\'+'Sets'+'\\'+'Set_'+str(i+1)
		filenames = os.listdir(path) 
		for filename in filenames:
			for line in open(os.getcwd()+'\\'+'Sets'+'\\'+'Set_'+str(i+1)+'\\'+filename  ):
				output.writelines(line)
output.close()
