### Web cache poisoning with multiple headers
#### Lab
The lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser.
<b>Hints: The requests  supports both the X-Forwarded-Host and X-Forwarded-Scheme headers. </b>

Inspecting the requests we can see that a JS script is used in the Home page:
--97--
We could code an malicious version of this script to be delivered to the visitors to solve the lab, to do that of course we have to find an injections point, let's use Param Miner exstension to find unkeyed inputs header in order to verify if the web site is vulnerable to cache poisoning. Before that don't forget to add a cachebuster value: change the exstension configuration as follows:
--96--
 
#### References
+ https://portswigger.net/web-security/web-cache-poisoning
