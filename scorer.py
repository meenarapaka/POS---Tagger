
#Team: Meena Rapaka, K.Siva Naga Lakshmi, Ying ke
#Assignment 3: POS Tagger, file: scorer.py

#The output of the tagger file("pos-test-with-tags.txt") is compared with golden 
#standard key "pos-test-key.txt" file to calculate the accuracy and provide 
#confusion matrix 

#The program should run on command prompt/ terminal, then specify the path of the python file.

#python scorer.py pos-test-with-tags.txt pos-test-key.txt pos-taggingreport.txt(command to be given in terminal)

#once the above command is executed, a text file pos-taggingreport.txt is created where scorer.py is stored.
#This file will contain accuracy and confusion matrix computed for the above compared tags.

#Algorithm:
#1 :Input is passed as sys arguments which are tagger program output file and test key 
#2: Read the output file to clean the unwanted characters from the file 
#3: Read the POS tagged Key file and place them in a list after tokenizing and removing unwanted characters. 
#4: corresponding words from the model output are matched to the test key and the counter is incremented every time it matches
#5: Find the accuracy of the model by dividing the count of matched words with the length of the model output file.
#6: confusion matrix is created by comparing the tagged key-POS list file tokens  with the model output tagged POS tokens 
#END




import scipy
import sys
import nltk
import pandas as pd
from sklearn.metrics import confusion_matrix

if __name__ == "__main__":
     #trainfile = "pos-train.txt"
    #testfile = "pos-test.txt"
    #outputfile = "pos-test-with-tags.txt"
    outputfile = sys.argv[1]
    testingkey = sys.argv[2]#passing the inpu
    taggerreport= sys.argv[3]
     #outputfile = "pos-test-with-tags.txt"
    #testingkey = "pos-test-key.txt" 
# a value is assigned with special characters and these are not considered as POS tags.
    a=('[',']','#','$',"''",'(',')',',','.',':','``')#special characters

#the test key file is read and replaced
    f1=open(testingkey)
    x2=f1.read()
    x3=x2.replace('\n', '')
    temp = x3.replace("[","")
    finalkey=temp.replace("]","") 
    final_tokens = [nltk.tag.str2tuple(t) for t in finalkey.split()if t.strip()
        not in a ]#str2tuple is used to tokenize training file output is given as tuple, and special characters are removed using strip function#

# the output key file is read and replaced   
    f=open(outputfile)
    x1 = f.read()
    model = x1.replace('\n', '')
    model_tokens = [nltk.tag.str2tuple(y) for y in model.split() if y.strip() 
        not in a ]#str2tuple is used to tokenize training file output is given as tuple, and special characters are removed using strip function#
    
    #for value in model_tokens:
    tag_list= [i[1] for i in final_tokens]#tested tokens are passed into tag_list and output of tagger tokens are passed into model_list #
    model_list = [i[1] for i in model_tokens]
    count=0
    for word in tag_list:
        pos=tag_list.index(word)
        if ( word== model_list[pos]):
            count= count+1
    accuracy = (count/ len(final_tokens)*100) #Comparing with the key, accuracy is calculated
    key = set(tag_list)
    list(key)
    modelkey = set(model_list)
    list(modelkey)
    #confusion matrix is created
    d1 = pd.Series( (i for i in tag_list) )
    d2 = pd.Series( (i for i in model_list) )
    dfconfusion = pd.crosstab(d1, d2) 
    print("open file pos-taggingreport.txt which is created in the same directory as scorer to check for accuracy and confusion matrix")
    
    with open(taggerreport,'w') as f:
        f.writelines("Accuracy : ")
        f.writelines(str(accuracy))
        f.writelines('\n')
        f.writelines("Confusion Matrix: ")
        f.writelines('\n')
        f.writelines(str(dfconfusion))
    

