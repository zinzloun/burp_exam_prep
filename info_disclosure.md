### Information disclosure in version control history
<i>Please note that during the explanation my Lab ID will change, so there will be some discrepancy between the screen-shots.</i><br>
To follow the solution you will need to have installed:
+ wget
+ git CLI

#### Lab
The lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the administrator user then log in and delete Carlos's account.

First of all let's to brute-force the application directories structure. To do that we can use Intruder. Set up the position in the request as follows (choose Sniper as attack)
--100--
Then in the payload(1) set the type as Simple list (2) and the list of the sub directories to test (3, <i>please note that here I have used a limited wordlist to speed up the process</i>). Be sure to uncheck the URL encoding characters option (4) before to execute the attack.
--101--
After a while we can see that the <b>.git</b> has been found. 
--102--
Just to recall this folder contains all information that is necessary for the project and all information relating commits. It also contains a log that stores the commit history. This log can help you to roll back to the desired version of the code. Very interesting, we can proceed to downlad the whole folder using wget:


#### References
