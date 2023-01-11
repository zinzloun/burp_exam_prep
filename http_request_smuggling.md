### HTTP request smuggling
#### Basic information
+ HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users.
Most HTTP request smuggling vulnerabilities arise because the HTTP specification provides two different ways to specify where a request ends: the <b>Content-Length header (CL) and the Transfer-Encoding header(TE)</b>. 
The Transfer-Encoding header can be used to specify that the message body uses chunked encoding. This means that the message body contains one or more chunks of data.<br>
Since the HTTP specification provides two different methods for specifying the length of HTTP messages, it is possible for a single message to use both methods at once, such that they conflict with each other. The HTTP specification attempts to prevent this problem by stating that if both the Content-Length and Transfer-Encoding headers are present, then the Content-Length header should be ignored.<br>
If the front-end and back-end servers behave differently in relation to the (possibly obfuscated) <b>Transfer-Encoding header</b>, then they might disagree about the boundaries between successive requests, leading to request smuggling vulnerabilities. The following scenarios are possible:
1. CL-TE: the front-end server uses the Content-Length header and the back-end server uses the Transfer-Encoding header
1. TE-CL: the front-end server uses the Transfer-Encoding header and the back-end server uses the Content-Length header
1. TE-TE: the front-end and back-end servers both support the Transfer-Encoding header, but one of the servers can be induced not to process it by obfuscating the header in some way
#### Lab enviroment
In the lab the front-end server doesn't support chunked encoding. The application is also vulnerable to reflected XSS via the User-Agent header.

To solve the lab, smuggle a request to the back-end server that causes the next user's request to receive a response containing an XSS exploit that executes <b>alert(1)</b> 



#### Reference
+ https://portswigger.net/web-security/request-smuggling

