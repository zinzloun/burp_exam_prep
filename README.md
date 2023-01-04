# Burp Exam Roadtrip
## Labs
### Web shell upload via extension blacklist bypass
<b>Concepts: Load an .httacces file to allow a file with a custom extension .pws to be executed as PHP file</b>
<br>![img](./img/1.png)<br>
The httaccess file is uploaded<br>![img](./img/2.png) 
<br>Upload your webshell as .pws file<br>![img](./img/3.png)
<br>Now inspect the source code of your account page<br>
![img](./img/4.png)<br>Visit the img src URL and you get the secret

### OAuth account hijacking via redirect_uri
<b>Workflow</b><br/>
Login to the portal using OAuth -> OAuth server authentication (yes) -> Portal (authenticated)  with auth code in the QS
<br>![img](./img/5.png)<br>
In the repeater since we are already authenticated, we can see the cookie session already set
<br>![img](./img/6.png)<br>
We can modify the redirect_uri parameter without get any error. The parameter is used to generate the redirect
<br>![img](./img/7.png)<br>
Now redirect the request to our payload hosted into the exploit server
<br>![img](./img/8.png)<br>
After delivered to the victim the payload, we can inspect the exploit access log to get the leaked auth code:
<br>![img](./img/9.png)<br>
Now we can use the code to access the portal bypassing the authentication process:
https://YOUR-LABID.web-security-academy.net/oauth-callback?code=T2QW7SXUMEHWY_bpSSTnNucJRfhWhQRtbj2GQpqAINC
