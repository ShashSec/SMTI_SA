# Nov 25 2017
* Problem statement moved to wikki pages
* Renamed the project from THSM_SA to SMTI_SA
* Next steps: finding cyber security knowledge source, extracting entities

# Nov 26 2017
* Automatic Labeling for Entity Extraction in Cyber Security is presented in 2014 ASE Bigdata conference stanford university
* There are two problem statement in the paper, First, Auto labeling the sentence containing security related words and second part train the ML algorithm from the auto labeled NVD corpus to extract the security related from any given sentence
* Auto labeling is done by considering the each sentence and converting word list/vector s1={w1, w2, w3,...} and tags T={t1, t2, t3..} the probability of tag t1 applied to w1 is calculated using history based Maximum entropy method with greedy tagging algorithm.
* The auto labled corpus is used to train a classifier that can apply domain-appropriate labels to a wider class of documents including news articles, security blogs, and tweets.This is done by Mathew Honnibal’s persuasive results and documentation of greedy tagging using the aver- aged perceptron for part-of-speech tagging

# Nov 27 2017
* Discussion of Entity extraction research paper with Kumar, following are the few dicussion points
* Most Paper and perticularly this paper has used word matching, regular expression and Relevant Terms Gazetteer (to group relavent words) to create the training data
* This method will not be able to identify similar terms like Hack and attack as synonym in cyber security domain
* This research aim is to develop  AI assistant that will help security analyst to proactively incorporate Social media threat intel 
* Action items 
    * 1. Use the entity extraction corpus to train wordtoVEc and then use LSM classifier
    * 2. Collect large corpus from CVE, NVD, Security bulletin and perform step 1
    * 3. Twitter stram api to filter based on Entity and relationship model

# Dec 13 2017
* Social media hunting should not be limited to twitter and the information extraction should not be limited Vulnerability and patch management. Having said that, the system should have multiple problem set addressing the various issues and multiple platforms addressing various data source (data set)
* These problem set and platform should be an individual blocks should work independly as well as together. Any problem new problem set can be introduced or removed with mininmal effort and knowledge by security analyst.
* The main objective of the project is to develop a platform to serve on demand threat intel request by leveraging AI
   * Analyst should be able to identify new problem or choose among the problem set.
      * If creates new problem set, He trains the model with minimal data
      * develop a playbook (model to extract the relavent information)
   * Analyst will choose the platforms to search (data source)
   * Develop common aggregasion methodology
   * Result

# Dec 14 2017
* Some of the system provide this feature are silobreaker, zerofox, wapack labs

# Dec 17 2017
* LSTM tagging, POS tagging, Sequence of word and identifies the noun word.
* bidirectional LSTM, tag the sentence
                 
# Dec 30 2017
* Completed extracting NVD data set and uplaoded to github
* since data is only 25 mb, alternate data is in search

# Jan 3 2017
* Security text book is a good source of data- identified because credible and security related text
* Found 867 MB (45 e-books) in PDF format. Need to find pdf to text convertor.
* Slate and Pdfminer can be used

# Jan 7 2017
* Studied SVN from Math of intelligence and MIT. should continue

# Jan 19 2017
* started working on Slate and Pdf miner to extract data from PDF but unable to install package on windows

# Jan 28 2017
* using textextract and pdfPy2 was able to convert PDF to text
* converting individual pdf as initial and last few pages needs to be removed

# Feb 3 2017 
* Converted all 45 e-books and 867 MB reduced to 26 MB of text file
* Only 50MB so far combining e-books and NVD corpus
* Few oter books downloaded from internet and conveted
* new plan use research paper as it will only contain text most of the cases and need not to cut any pages
* started collecting research paper
* started twitter stream program to collect tweets

# Feb 4 2017
* 11 MB tweets were collected and anlayzed and modified the code to stream line the tweets
* new streaming program is written to filter based on user
* Top security users, Company and Blogs twiiter account was found and used in program
* Program to filter tweets based on user is not feteching any result - Might be some issue!!
* uploaded the data and program in Github under TwitterStream_Python
* Next, Need to collect more research paper
* run pdftoText program to extract text
* Normalizing twitter streaming code
