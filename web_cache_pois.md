### Web cache poisoning with multiple headers
#### Lab
The lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser.
<b>Hints: The requests  supports both the X-Forwarded-Host and X-Forwarded-Scheme headers. </b>

Inspecting the requests we can see that a JS script is used in the Home page:
--96--
We could code an malicious version of this script to be delivered to the visitors to solve the lab, to do that of course first we have to find out if the application is vulnerable to cache poisoning. To automate the headers analysis I used the wonderful tool <b>Web-Cache-Vulnerability-Scanner</b> (more info in the [reference](#references) section). Executing the program as follows:
```
 .\wcvs.exe -u https://0acc009f04df6e15c5a378880089005a.web-security-academy.net -ppath .\BurpCer.pem -ot headers -hw '.\wordlists\lab'

[ERR] Published by Hackmanit under http://www.apache.org/licenses/LICENSE-2.0
[ERR] Author: Maximilian Hildebrand
[ERR] Repository: https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner

[ERR] WCVS v1.1.0 started at 2023-01-19_09-41-36
[ERR]
Testing website(1/1): https://0acc009f04df6e15c5a378880089005a.web-security-academy.net
....
| Header Poisoning
 --------------------------------------------------------------
[ERR] Testing 2 headers
[ERR] Unexpected Status Code 302 for 1st request of header X-Forwarded-Scheme
[ERR] Unexpected Status Code 302 for 2nd request of header X-Forwarded-Scheme
[ERR]
[ERR] Header X-Forwarded-Scheme was successfully poisoned! cb: 933918142027 poison: 624564716619
[ERR] URL: https://0acc009f04df6e15c5a378880089005a.web-security-academy.net?cb=933918142027
[ERR] Reason: Status Code 302 differed from 200
...
[ERR] Successfully finished the scan
[ERR] Duration: 2.8823452s
```
I used the following parameters
+ -ppath = path to Burp certification file in PEM format (if you have installed the certificate in FF, visualizing it then you have the option to export it as PEM file) 
+ -ot = test only headers
+ -hw = custom word list that contains only X-Forwarded-Host and X-Forwarded-Scheme

Using the -ppath option implies to use the Burp proxie. As we can see from the output we were able to identify that the <b>X-Forwarded-Scheme</b> can be poisoned, but nothing is reported for the X-Forwarded-Host header. Anyway I tried to send a request with both the parameters set
```
X-Forwarded-host: www.google.it
x-forwarded-scheme: https
```
In this case nothing happens and I got a 200 response. Indeed changing the protocol to http we get a redirect to the X-Forwarded-host value:
--97--
Knowing that we can try to poison the server cache for the script <b>/resources/js/tracking.js</b> to poin to the exploit server, configured as follows
--98--
Now modify in Repeater modify the request for the script as follows:
--99--
Here the x-forwarded-host points to the exploit server that hosts the malicious script (1), setting the x-forwarded-scheme to http (2) will trigger the redirection to the malicious script URI (3). Keep submitting the request until you get <b>x-cache: hit</b> in the response (4), that means that the resources has been cached.

Now reloading the home page you should get the alert pop-up, and the lab should be solved

#### References
+ https://portswigger.net/web-security/web-cache-poisoning
+ https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner
