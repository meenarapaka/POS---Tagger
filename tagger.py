#Team: Meena Rapaka, K.Siva Naga Lakshmi, Ying ke
#Assignment-3: POS Tagging, tagger.py
#1.Introduction
#This program will recognize parts of speech in a given text input file. pos-train.txt(words are predefined set of tags)
# is passed as input and pos-test.txt file has words which need to be tagged. To generate output file which
#contains tags beside the words in the test file.
#The output file generated words will be tagged if they present in training data and which are not there in train data
#they will be assigned according to the rules given below. Example like if word is unknown it is considered as NN and words
#ends with ed is VBD.

# parts of speech are divided into 8 categories, namely
#noun-> NN, singular or mass-->NNS is noun plural
#NNP-proper noun singular, NNPS is proper noun plural
#PDT-predeterminer,POS-possesive ending
#PRP- personal pronoun, PRP$- possessive pronoun
#RB-adverb
#RBR- adverb comparitive 
#VBD-verbe past tense
#JJ- adjective big
# tags are added next to the words in the ouput file based on its context in the training file.
#output file format will be
#   [played/VBD]


#2. Example input/output:

#The program should run on command prompt/ terminal, then specify the path of the python file

#python tagger.py pos-train.txt pos-test.txt pos-test-with-tags.txt(command to used in terminal)
#(please make sure that the folder which contains the python file should also contain the train, test and key files)

#After running the above command, the output file
#pos-text-with-tags.txt is located in  the same folder as tagger.py

#Now check for file pos-text-with-tags.txt and open it.You can find
#tags besides the words which are present in test data based on the train data.

#3. Algorithm:

#Start
    
#1 : Input is passed as sys arguments which are the train , test and output file name 

#2: Read the training file to clean the unwanted characters

#3: After removing the unwanted characters, the training file is tokenized and stored in a list

#4: Conditional distribution of the word and POS tag combination for the training dataset are identified

#5: After 4, we will read the test file and remove the unwanted characters from the file

#6: Tokenize the test file

#7: Match words in test file with training file, will give the POS tag.

#8: If the token in the train has been associated with more than one POS tag then  pick the POS tag with the highest occurrence

#9: the rules defined in the code, example VBD, JJ etc., will be tagged for words ending with 'ed', 'able' respectively as mentioned in the below rules. 

#10: If there is match then write that matched POS tag and the word into the output file.If no match found we use NN.

#11: Write the Output file into directory. 

#End




import sys
import nltk
if __name__ == "__main__":

    #trainfile = "pos-train.txt"
    #testfile = "pos-test.txt"
    #outputfile = "pos-test-with-tags.txt"

    trainfile=sys.argv[1]
    testfile=sys.argv[2]    #passing the input
    outputfile=sys.argv[3]

    tagged_token = None
    input_training = None
#the train file is read and replaced
    f=open(trainfile) 
    x1=f.read()
    x2=x1.replace('\n', '') 
#using replace we are removing "["
    temp = x2.replace("[","")
    final_input = temp.replace("]","")

    if final_input is not None:
        traintoken = [nltk.tag.str2tuple(x) for x in final_input.split()] # str2tuple is used to tokenize training file
#output is given as tuple
        tagged_token = nltk.ConditionalFreqDist(traintoken) #frequency distribution is calculated

    test = None
    input1= None
#test file is read and replaced
    f=open(testfile)
    y1=f.read()
    y2=y1.replace('\n', '')
#using replace we are removing "["
    temp = y2.replace("[","")
    finaltest = temp.replace("]","")

#the below loop is used to tag the test dataset with the defined rules and training data, if a word is matched, it is tagged with training data#
    if finaltest is not None and tagged_token is not None:
        finaltest = " "+finaltest+" " #add temporary spaces before starting and ending words
        test = [i for i in finaltest.split()]
        for x in test:
            if x.endswith('able'): #x==word, if it ends with 'able', it is tagged as JJ-> adjective
                pos_tag='JJ'
            elif x.endswith('ed'): #if the words ends with 'ed', it is tagged as VBD-> simple past
                pos_tag='VBD'
            elif x.endswith('ly'):#if the words ends with 'ly', it is tagged as RB-> adverb
                pos_tag='RB'
            elif x=='his' or x=='His' or x=='her' or  x=='Her' or x=='its' or x=='Its': 
                pos_tag='PRP$'#if the word is his/her etc., it is tagged as PRP$-> possessive pronoun
            else:
                pos_tag = 'NN'  # if word in  not existed in training, it is tagged as NN
            matched_pos = tagged_token[x].most_common()
            if matched_pos:
                pos_tag = matched_pos[0][0]
            z = x+"/"+pos_tag# now the test data words, the tags are added
            finaltest = finaltest.replace(" "+x+" "," "+z+" ") 
            finaltest = finaltest.replace("\n"+x+" ","\n"+z+" ") #replace function used here is to replace the word with tagged added to the word. Ex: its -> its/PRP$/ #
            finaltest = finaltest.replace(""+x+"\n",""+z+"\n")
            
    finaltest = finaltest[1:-1]  # removes previously added temporary spaces 
    with open(outputfile,'w') as f:#write output to the text file parsed initially.
          f.write(finaltest)
print("open file pos-test-with-tags.txt which has been created in the same directory where tagger is stored")

            
            
    
