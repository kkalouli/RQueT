####################################################################################################################################
#
# This script creates the corpus constructed for the paper : "Is that really a question? Going beyond factoid questions in NLP" by
# Kalouli, et al, 2021. In order to create the corpus, you should first download the CNN files made available by Sood, 2017:
# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ISDPJU
# After you have downloaded all 6 files, unzip them and put them in one folder. In the same folder, you have to also place this
# script and the provided mapped_indices.csv file. After doing so, you can simply run this script by typing
# **python create_cnn_corpus.py**. If the script runs without any issues, you will have a file called 
# "cnn_corpus_annotated_questions.csv" in the same folder. This output file will be tab-separated and have the following structure:
# ID: the unique ID of this question
# ctxB2: the second sentence before the question
# ctxB2_speaker: the speaker of ctxB2
# ctxB1: the first sentence before the question
# ctxB1_speaker: the speaker of ctxB1
# question: the question under investigation
# question_speaker: the speaker of the question
# ctxA1: the first sentence after the question
# ctxA1_speaker: the speaker of ctxA1
# ctxA2: the second sentence after the question
# ctxA2_speaker: the speaker of ctxA2
# gold_label: the gold label for this question, as annotated within this work
#
#
#
# Author: Katerina Kalouli
# Date: 30.04.2021
# License: check the licensing details provided within the origin of the CNN transcripts by Sood, 2017 
#
##########################################################################################################

import os, re
import pandas as pd
pd.set_option('display.max_colwidth', -1)

print ("This may take up to a minute...")
print ("Reading CNN files . . . ")

# open input files downloaded from harvard database
df1 = pd.read_csv("cnn-5.csv", sep = ",")
df2 = pd.read_csv("cnn-6.csv", sep = ",")
# open delivered file with the indices of the questions
df_ids = pd.read_csv("mapped_indices.csv", sep = "\t")
# open output file where the entire corpus will be written
output = open("cnn_corpus_all.csv", "w")
# open output file where only the train split will be written
output_train = open("cnn_corpus_train.csv", "w")
# open output file where only the test split will be written
output_test = open("cnn_corpus_test.csv", "w")

# the unique ids of the questions that belong to the test split
test_ids = ["1113088","1113093","1113104","1113105","1113117","1113120","1113128","1113138","1113147","1113176","1113177","1113180","1113185","1113218","1113229","1113240","1113253","1113266","1113270","1113278","1113283","1113308","1113316","1113322","1113332","1113350","1113375","1113380","1113388","1113404","1113407","1113409","1113415","1113418","1113420","1113435","1113440","1113455","1113473","1113490","1113511","1113522","1113536","1113546","1113572","1113574","1113578","1113667","1113677","1113686","1113697","1113703","1113719","1113725","1113731","1113732","1113734","1113737","1113754","1113773","1113866","1113881","1113922","1113926","1113930","1113959","1113970","1113980","1114015","1114031","1114038","1114056","1114058","1114061","1114104","1114124","1114146","1114167","1114171","1114180","1114193","1114196","1114197","1114205","1114224","1114240","1114245","1114283","1114304","1114316","1114327","1114349","1114358","1114360","1114397","1114415","1114417","1114425","1114436","1114452","1114455","1114457","1114473","1114481","1114484","1114487","1114503","1114521","1114531","1114540","1114548","1114563","1114578","1114602","1114620","1114745","1114762","1114769","1114776","1114794","1114827","1114837","1114842","1114860","1114869","1114929","1114939","1114950","1114957","1114963","1114973","1114976","1114977","1114983","1114992","1115020","1115039","1115048","1115052","1115066","1115067","1115071","1115073","1115087","1115089","1115100","1115158","1115163","1115221","1115242","1115246","1115255","1115280","1115284","1115285","1115288","1115316","1115325","1115341","1115369","1115372","1115374","1115397","1115412","1115414","1115418","1115421","1115425","1115430","1115443","1115447","1115454","1115459","1115469","1115480","1115483","1115492","1115523","1115525","1115546"]

output.write("id\tctx_b2\tctx_b2_spe\tctx_b1\tctx_b1_spe\tque\tque_spe\tctx_a1\tctx_a1_spe\tctx_a2\tctx_a2_spe\tlabel\n")
output_train.write("id\tctx_b2\tctx_b2_spe\tctx_b1\tctx_b1_spe\tque\tque_spe\tctx_a1\tctx_a1_spe\tctx_a2\tctx_a2_spe\tlabel\n")
output_test.write("id\tctx_b2\tctx_b2_spe\tctx_b1\tctx_b1_spe\tque\tque_spe\tctx_a1\tctx_a1_spe\tctx_a2\tctx_a2_spe\tlabel\n")



print ("Creating CNN corpus . . . ")

# go through each row of the mapped_indices file in order to map it to real text
for index, row in df_ids.iterrows():
	# retrieve the specific file in which this question is found
	file = row['file'] 
	# retrieve the specific line of the file in which this question is found (source of the question)
	source = row['source']
	# retrieve the id of the question
	id = row['ID']
	# retrieve the correct dataframe
	if file == "cnn-5.csv":
		df = df1
	elif file == "cnn-6.csv":
		df = df2 
	# retrieve the row of the dataframe corresponding to the retrieved source
	utt_row = df.loc[df['url'] == source]	
	# retrieve only the "text" element of the row
	text = str(utt_row['text']).replace(":","").replace("'","").replace('"', '-') 
	# get all information by detecting the exact slices of the text contained in the mapped_indices file
	# 9 has to be added to the standard index to get the correct portion of the element	
	# remove space from the beginning of some utterances 
	counter = 9
	### question
	que = text[int(row['que_index'].split(":")[0])+counter:int(row['que_index'].split(":")[1])+counter]
	if que.startswith(" "):
		que = que.replace(" ", "", 1)
	que_spe = text[int(row['que_speaker_index'].split(":")[0])+counter:int(row['que_speaker_index'].split(":")[1])+counter]
	### question speaker
	if que_spe.startswith(" "):
		que_spe = que_spe.replace(" ", "", 1)
	### context-before 2
	ctx_b2 = text[int(row['context_2_index'].split(":")[0])+counter:int(row['context_2_index'].split(":")[1])+counter]
	if ctx_b2.startswith(" "):
		ctx_b2 = ctx_b2.replace(" ", "", 1)
	### context-before 2 speaker
	ctx_b2_spe = text[int(row['context_2_speaker_index'].split(":")[0])+counter:int(row['context_2_speaker_index'].split(":")[1])+counter]
	if ctx_b2_spe.startswith(" "):
		ctx_b2_spe = ctx_b2_spe.replace(" ", "", 1)
	### context-before 1
	ctx_b1 = text[int(row['context_1_index'].split(":")[0])+counter:int(row['context_1_index'].split(":")[1])+counter]
	if ctx_b1.startswith(" "):
		ctx_b1 = ctx_b1.replace(" ", "", 1)
	### context-before 1 speaker
	ctx_b1_spe = text[int(row['context_1_speaker_index'].split(":")[0])+counter:int(row['context_1_speaker_index'].split(":")[1])+counter]
	if ctx_b1_spe.startswith(" "):
		ctx_b1_spe = ctx_b1_spe.replace(" ", "", 1)
	### context-after 1
	ctx_a1 = text[int(row['context1_index'].split(":")[0])+counter:int(row['context1_index'].split(":")[1])+counter]
	if ctx_a1.startswith(" "):
		ctx_a1 = ctx_a1.replace(" ", "", 1)
	### context-after 1 speaker
	ctx_a1_spe = text[int(row['context1_speaker_index'].split(":")[0])+counter:int(row['context1_speaker_index'].split(":")[1])+counter]
	if ctx_a1_spe.startswith(" "):
		ctx_a1_spe = ctx_a1_spe.replace(" ", "", 1)
	### context-after 2
	ctx_a2 = text[int(row['context2_index'].split(":")[0])+counter:int(row['context2_index'].split(":")[1])+counter]
	if ctx_a2.startswith(" "):
		ctx_a2 = ctx_a2.replace(" ", "", 1)
	### context-after 2 speaker
	ctx_a2_spe = text[int(row['context2_speaker_index'].split(":")[0])+counter:int(row['context2_speaker_index'].split(":")[1])+counter]
	if ctx_a2_spe.startswith(" "):
		ctx_a2_spe = ctx_a2_spe.replace(" ", "", 1)
	### label
	label = row['label']
	# write everything into the corresponding files
	output.write(str(id) + "\t" +ctx_b2 + "\t" + ctx_b2_spe + "\t" + ctx_b1 + "\t" + ctx_b1_spe + "\t" + que + "\t" + que_spe + "\t" + ctx_a1 + "\t" + ctx_a1_spe + "\t" + ctx_a2 + "\t" + ctx_a2_spe + "\t" + label +"\n")
	if str(id) in test_ids:
		output_test.write(str(id) + "\t" +ctx_b2 + "\t" + ctx_b2_spe + "\t" + ctx_b1 + "\t" + ctx_b1_spe + "\t" + que + "\t" + que_spe + "\t" + ctx_a1 + "\t" + ctx_a1_spe + "\t" + ctx_a2 + "\t" + ctx_a2_spe + "\t" + label +"\n")
	else:
		output_train.write(str(id) + "\t" +ctx_b2 + "\t" + ctx_b2_spe + "\t" + ctx_b1 + "\t" + ctx_b1_spe + "\t" + que + "\t" + que_spe + "\t" + ctx_a1 + "\t" + ctx_a1_spe + "\t" + ctx_a2 + "\t" + ctx_a2_spe + "\t" + label +"\n")


print ("Processing finished!")	 
output.close()
output_train.close()
output_test.close()
