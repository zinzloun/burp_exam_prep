### Server side template injection (SSTI)
#### Intro
Server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.<br>
Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data. 
#### Lab
<i>Please note that my Lab ID will change during the explanation</i><br>
To solve the lab, identify the template engine and find a documented exploit online that you can use to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

So let's try to find an injection point, viewing the details of the first item we can see that the message query string parameter is reflected into the page:
-- 72 --
We can eventually try to test for XSS, but as we can see it is not vulnerable (at least not to a simple attack), anyway knowing that this is not the aim of the lab, we can move forward to test for a simple SSTI payload:
```
{{7*7}}
```
Then we get an error response that indicates that the application could be vulnerable, here we get two interesting information: A module called <b>handlebars</b> is used and the coding language seems to be <b>Node.js</b>. Since I have a very little knowledge about Node.js and nothing about Handlebars I have no idea how to proceed further 🤨. Googling for 'ssti handlebars node.js' returned some interesting results, among all I found this one: http://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html<br>
Telling the truth I had problem to clearly understand what <b>Mahmoud Gamal</b> actually did 😬, so I had to study quite a bit the handlebars library and Node.js
#### Reference
+ https://portswigger.net/web-security/server-side-template-injection
+ https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
+ http://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html
