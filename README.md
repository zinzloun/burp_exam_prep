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

### SSRF via flawed request parsing
In this lab we can take advantage of host header injection, just to recall what is the purpose of this header: https://www.rfc-editor.org/rfc/rfc7230#section-5.4
<br>First let’s try to modify the host value, we can notice that the request is blocked
<br>![img](./img/10.png)<br>
Now we inspect the GET request providing the full path to our LAB URL, deleting the Host header, we notice that we get a valid response:
<br>![img](./img/11.png)<br>
Since we know that the admin panel is locally accessible in the subnet 192.168.0.0/24, we can try to insert a test value in the Host parameter:
<br>![img](./img/12.png)<br>
Here we get a timeout, but we also can notice that the Host value is used to resolve the URI provided into the GET parameter, now we can configure the Intruder to try to brute force the IP value, looking for a 200 or 302 (redirect) response.<br>
Set the payload parameter (1)
<br>![img](./img/13.png)<br>
Then configure the payload as follows:
<br>![img](./img/14.png)<br>
Run the Intruder (in the community it is time throttled):
<br>![img](./img/15.png)<br>
Coming back to the repeater to modify the request according to the redirect:
<br>![img](./img/16.png)<br>
Here we can see that posting a request to the <b>/admin/delete</b> passing the csrf token and the username parameters permit to delete a user. Modify the request according to the information we discovered and we solve the lab (see the picture in the next page). Here there is another very insecure flow, since the csrf token is transmitted even if we are not authenticated as an admin user, of course this scenario must be mitigated through an authentication mechanism. Additional information about csrf token generation can be found at https://portswigger.net/web-security/csrf/tokens 
<br>![img](./img/17.png)<br>




