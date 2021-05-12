# RQueT---Resource-of-Question-Types
The RQueT corpus was used to introduce the task of Question Type Identification (QTI). The corpus contains 1768 questions annotated for their question type, i.e., whether they are information-seeking or non-information-seeking. The questions originate from CNN transcripts. For every question the corpus also provides the two sentences before the question and the two sentences after, as well as the speaker of each of these sentences. The corpus is split into a training/test set with 1588 items in the training set and 180 in the test set. For more information on the corpus, please see our paper:

*Kalouli, A.-L., R. Kehlbeck, R. Sevastjanova, O. Deussen, D. Keim and M. Butt. 2021. Is that really a question? Going beyond factoid questions in NLP. In Proceedings of the 14th International Conference on Computational Semantics 2021 (IWCS 2021) (link coming soon).*

If you use this corpus or software in any way, please include the above citation.


## Annotation Guidelines

## Corpus

## Models
We make available the most significant models trained within this work. Specifically, we make available the following:
- the NB model trained on the speaker-after feature (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the BERT model fine-tuned on the question and the context-after (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the BERT model fine-tuned on the question and the context-before (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the BERT model fine-tuned only on the question (https://drive.google.com/drive/folders/1nLfdbTCf81tA689vuadsBs89gYs8Ry3j?usp=sharing)
- the FF model trained on a) the fine-tuned BERT model of question and context-after and b) the speaker-after (found within the folder *models*)
- the SVM model trained on the fine-tuned BERT model of question and context-before (found within the folder *models*)
- the best lexicalized model trained on the bigrams and trigrams of the surface forms and the POS tags of the question, of the first context-before and of the first context-after (found within the folder *models*)

## Scripts
In the folder *scripts* you can find the main notebooks used for the fine-tuning of the BERT models and the training of the further classifiers. The notebook *QTI - Fine-tuning BERT* can be used to reproduce our fine-tuning of the BERT models. The models themselves can be downloaded from the above links. The embeddings we extracted from each of these models (the CLS embedding of the 11th layer) can be found in the folder *fine-tuned_bert_embeddings*. These files with the embeddings are also necessary to run the other notebook we make available *QTI - Training Further Classifiers*. This notebook also uses the files found in the folder *simple_features_annotations*. 


## Contact
For any questions or comments, please write to aikaterini-lida.kalouli AT uni-konstanz DOT de
 
