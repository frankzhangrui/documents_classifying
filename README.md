documents_classifying
=====================
This is my first python project to classify documents.
The first step is to convert documents into words and create tf-idf features for each documents.
After feature extraction, any kind of classifier is your choice.
Later I will upload myknn.py as my first python project on classfiers.
Command line usage
python tfidf.py yourdocuments1.txt yourdocuments2.txt ... >output.txt
or
you can just name your document in a unified way like good01.txt good02.txt then
command line would be 
python tfidf.py good*.txt>output.csv
