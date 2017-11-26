# Social Media Threat Intel

# Problem statement
Any Bussiness has several IT components that can be compromised directly or indirectly.
Any cyber threats on company's infratructure or its product is considered as direct attack and
any third party tools/service, software and hardware threats or vulnerability is considered as Indirect attack.
Also, Indirect attack can occur by cyber threats associated with vendor, contractors.

Direct attack on infrastructure causes huge impact due to data breach, Trade secret, finacial loss, etc.
Direct attack on products affects the revenue, market, etc.

Usually, Bussiness IT Infrastructure is monitored by the company and any breach in the infrastructure should be
identified by the company itself.

The vulnerabilty or compromise of any proucts either identified by the internal security testing team or
open source security researchers independent of the company. Though, most of the researchers are expected to 
report it to the parent organization many times the bugs are notified through social media like twitter.

Indiect attack on company by exploiting the vulnerabilities of the tools, service, software, products from
third parties can not be directly controlled by the bussiness and should be prepared to identify the vulnerability 
and take nessary action to remediate or protect the infratructure from cyber attack but most of these information will 
not be directly available to the company. Security buletin, social media or news media will best source of the information. 
for example badrabbit ransomeware was first notified via twitter. 

Many companies have struggled a cyber security breach by exploiting the vulnerabilities in the third party tools. 
for example equifax fail to update the apache struts vulnerability and this was exploited in data breach
So, Social media is best source of threat intelligence for indirect threats to the infrastructure.


# Social Media Threat Intel priority model:

Priority 0: Wide spread malware campaign like ransomeware, spyware, virus that creates trend or movement in Social media
priority 1: since third party tools like software, hardware product's security vulnerabilty and threats are beyond the control on the individual company and does not get direct update on thesese vulnerability relaying and these information are published in SM
it takes the first priority
priority 2: Direct attack on Proucts, since there company products are used widely by consumers and some of these independent researchers are like to annouce the vulnerabilty in SM. it takes second priority
priority 3: The direct attack on company itself will take priority 3 as most of the vulnerability is monitored internally

# Social Media Threat Intel Entity relationship model:

Consider Microsoft as an Bussiness organization. Here, Microsoft core IT infrastructur and Data are considered as direct infrastructure and all the activities are monitored by the SOC or NOC.
Their products such as Windows OS, Visual studio, IIS are some of the direct proucts used by many consumers and software security testing team and developers are responsible for identifying and
remediating the software vulnerability but sinnce these products are used by many consumers, Independent security researchers will ocassioaly idntify the vulnerabilty and sometimes report it to 
microdoft security testing team about the bug but some researchers choose to publish it in security bulletin or in social media though it is not standard procedure
the third party tools like network cisico switches, cisco routers, wifi hot spot and encryption techniques and adobe flash player are few common hardware and software not designed by microsoft but any 
vulnerabilities exploited in these system can give un authorized access to Microdoft critcal infrastructiure

So, based on priority model

pririty 1 : Entity to search in SM is " Cisco Switches ", "Cisco routers", "WPA Encryption" and "Adobe Flash player"
and the relation to the entity are "Vulnerability", "exploit", "compromise" etc
So priority 1 Entity and relation to search in social media is {[" Cisco Switches ", "Cisco routers", "WPA Encryption","Adobe Flash player"],["Vulnerability", "exploit", "compromise","Software Bug","Security Bug"]}
similarly priority 2 entity and relation is {["Visual studio","VS", "Windows","Microsoft OS"],["vulnerability","Bug","Security bug","Software Bug"]}
priority 2 due to third party/ vendor {["Yammer","Xamarin","Mindtree"], ["DDOS","hack","attack", "data breach"]}
Priority 3 {[Microsoft, Windows, Azure] ,["DDOS","hack", "Data Breach","attack"]}
       
Based on these priority and test entity and relation model one can elevate the machine learning algorithm to find the threat in social media.

# References
* Automatic Labeling for Entity Extraction in Cyber Security: https://arxiv.org/pdf/1308.4941.pdf
* Auto-labeled-corpus: https://github.com/stucco/auto-labeled-corpus
* entity-extractor in Java: https://github.com/stucco/entity-extractor
* Neuro-NER: https://github.com/Franck-Dernoncourt/NeuroNER
* Towards a Relation Extraction Framework for Cyber-Security Concepts: https://arxiv.org/pdf/1504.04317.pdf
* Cyber & Information Security Research Group, Oak Ridge National Laboratory repository: https://github.com/stucco/docs
* Weakly Supervised Extraction of Computer Security Events from Twitter: https://github.com/aritter/twitter_nlp
* Weakly Supervised Extraction of Computer Security Events from Twitter live system: http://kb1.cse.ohio-state.edu:8123/events/hacked
