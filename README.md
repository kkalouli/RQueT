# RQueT---Resource-of-Question-Types
The RQueT corpus was used to introduce the task of Question Type Identification (QTI). The corpus contains 1768 questions annotated for their question type, i.e., whether they are information-seeking or non-information-seeking. The questions originate from CNN transcripts. For every question the corpus also provides the two sentences before the question and the two sentences after, as well as the speaker of each of these sentences. The corpus is split into a training/test set with 1588 items in the training set and 180 in the test set. For more information on the corpus, please see our paper:

*Kalouli, A.-L., R. Kehlbeck, R. Sevastjanova, O. Deussen, D. Keim and M. Butt. 2021. Is that really a question? Going beyond factoid questions in NLP. In Proceedings of the 14th International Conference on Computational Semantics 2021 (IWCS 2021) (link coming soon).*

If you use this corpus or software in any way, please include the above citation.


## Annotation Guidelines
The annotation guidelines given to the annotators were the following:

You are given questions originating from real-life interviews and debates. For each question you are also given its context: the two sentences before it and the two sentences after it, as well as the speakers of each sentence. Based on this context and the question itself, decide whether the question is an information-seeking question (ISQ) or a non-information-seeking question (NISQ). Information-seeking questions are posed to retrieve information and elicit an answer, e.g. What are the changes that the new law will bring? Non-information-seeking questions are not posed to elicit a real answer, but rather to achieve other communication goals, e.g., a discourse-structuring question like "What has this pandemic taught us? It has taught us that..." . Annotate as naturally as possible with the first impression that you get out of the question.

## Corpus
Due to copyright reasons, the corpus cannot be provided directly. Instead, we provide a script with which the exact corpus can be retrieved from its source.
In order to create the corpus, you should first download the CNN files made available by Sood, 2017: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ISDPJU
After you have downloaded all 6 files, unzip them and put them in one folder. In the same folder, you have to also place the script *create_cnn_corpus.py* (found within the *scripts* folder) and the provided *mapped_indices.csv* file. After doing so, you can simply run the script by typing *python create_cnn_corpus.py*. If the script runs without any issues, you will have a file containing the entire corpus, a file containing the train split and a file containing the test split. The output files will be tab-separated and have the following structure:
- ID: the unique ID of this question
- ctxB2: the second sentence before the question
- ctxB2_speaker: the speaker of ctxB2
- ctxB1: the first sentence before the question
- ctxB1_speaker: the speaker of ctxB1
- question: the question under investigation
- question_speaker: the speaker of the question
- ctxA1: the first sentence after the question
- ctxA1_speaker: the speaker of ctxA1
- ctxA2: the second sentence after the question
- ctxA2_speaker: the speaker of ctxA2
- gold_label: the gold label for this question, as annotated within this work


## Models
We make available the most significant models trained within this work. Specifically, we make available the following:
- the NB model trained on the speaker-after feature (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the BERT model fine-tuned on the question and the context-after (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the BERT model fine-tuned on the question and the context-before (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the BERT model fine-tuned only on the question (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the FF model trained on a) the fine-tuned BERT model of question and context-after and b) the speaker-after (found within the folder *models*)
- the SVM model trained on the fine-tuned BERT model of question and context-before (found within the folder *models*)
- the best lexicalized model trained on the bigrams and trigrams of the surface forms and the POS tags of the question, of the first context-before and of the first context-after (found within the folder *models*, note that this model was trained with the LightSide platform so that you need to install the platform if you want to load and investigate the model further. Download LightSide from: http://ankara.lti.cs.cmu.edu/side/)

## Scripts
In the folder *scripts* you can find the main notebooks used for the fine-tuning of the BERT models and the training of the further classifiers. The notebook *Question_Type_Identification_Fine-tuning_BERT* can be used to reproduce our fine-tuning of the BERT models. You will also need the train and test splits of RQueT (see Section *Corpus* above). Our fine-tuned models can be downloaded from the above links. The embeddings we extracted from each of these models (the CLS embedding of the 11th layer) can be found in the folder *fine-tuned_bert_embeddings*. These embeddings files are also necessary to run the other notebook we make available *Question_Type_Identification_Training_Classifiers*. This notebook also uses the files found in the folder *simple_features_annotations*. The folder *scripts* also contains the script used for the creation of the corpus from its source files.  


## Contact
For any questions or comments, please write to aikaterini-lida.kalouli AT uni-konstanz DOT de
 
