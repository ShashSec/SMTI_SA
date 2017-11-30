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
    
                 
