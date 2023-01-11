# Burp Exam Roadtrip
Here I collected the lab's solutions following the exam preparation steps required to get the certification (https://portswigger.net/web-security/certification/how-to-prepare#step-1-complete-one-lab-from-every-topic). At the moment is a work in progress activity, I'm interested in the learning path, not in the certification.<br>
Please note that this is not a step-by-step guide to solve the labs, nor a guide about how to use Burp Suite, the aim of this work is to keep notes about the difficult tasks that I have faced solving the labs and sharing the information, of course try to solve the lab by yourself before accessing this material.<br>
In order to be able to follow the solutions I'm assuming that ou have some knowledge about:
+ how web apllications work
+ Burp Suite CE
+ common web app vulnerabilities (XSS, SQLi, CSRF, XXE...)
+ how to approach a problem 😃

I really encourage to learn the related topic before to access a solution, otherwise it will be very difficult to understand the steps involved. To solve the labs I have used Burp CE only<br>
If you have any questions, suggestions or just to say hallo you can drop me an email: filobers[at]pm[dot]me.

Enjoy your learning trip!

## Summary
### Cors
+ [Vulnerability with trusted insecure protocols](./CORS.md#cors-vulnerability-with-trusted-insecure-protocols)
### CSRF, XSS
+ [CSRF when token validation depends on request method](./CSRF-XXS.md#csrf-where-token-validation-depends-on-request-method)
+ [Exploiting cross-site scripting to capture passwords](./CSRF-XXS.md#exploiting-cross-site-scripting-to-capture-passwords)
### SSRF
+ [SSRF with filter bypass via open redirection vulnerability](./SSRF.md#ssrf-with-filter-bypass-via-open-redirection-vulnerability)
+ [SSRF via flawed request parsing](./SSRF.md#ssrf-via-flawed-request-parsing)
+ [SSRF with blacklist-based input filter](./SSRF.md#ssrf-with-blacklist-based-input-filter)
### SQLi
+ [SQL injection attack, querying the database type and version on MySQL and Microsoft](./SqlI.md#sql-injection-attack-querying-the-database-type-and-version-on-mysql-and-microsoft)
+ [SQL injection attack, listing the database contents on non-Oracle databases](./SqlI.md#sql-injection-attack-listing-the-database-contents-on-non-oracle-databases)
### XXE
+ [Blind XXE with out-of-band interaction via XML parameter entities](./XXE.md#blind-xxe-with-out-of-band-interaction-via-xml-parameter-entities)
+ [Exploiting blind XXE to exfiltrate data using a malicious external DTD](./XXE.md#exploiting-blind-xxe-to-exfiltrate-data-using-a-malicious-external-dtd)
### Authentication && Authorization
+ [OAuth account hijacking via redirect_uri](./authorization_authentication.md#oauth-account-hijacking-via-redirect_uri)
### Click-jacking
+ [Multistep clickjacking](https://github.com/zinzloun/burp_exam_prep/blob/main/clickjacking.md#lab-multistep-clickjacking)
### File upload
+ [Web shell upload via extension blacklist bypass](./file_upload.md#web-shell-upload-via-extension-blacklist-bypass)
### HTTP request smuggling
+ [HTTP request smuggling](./http_request_smuggling.md#http-request-smuggling)