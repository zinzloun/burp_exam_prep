### Server side template injection
#### Intro
Server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.

Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data. 

#### Reference
+ https://portswigger.net/web-security/server-side-template-injection
+ http://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html
