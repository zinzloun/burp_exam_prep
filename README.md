# Burp Exam Roadtrip
Here I collected the lab's solutions following the exam preparation steps required to get the certification (https://portswigger.net/web-security/certification/how-to-prepare#step-1-complete-one-lab-from-every-topic). At the moment is a work in progress activity, I'm interested in the learning path, not in the certification. Morover you need to have the Professionale version to attempt the exam.

Please note that this is not a step-by-step guide to solve the labs, nor a guide about how to use Burp Suite, the aim of this work is to keep notes about the difficult tasks that I have faced solving the labs and sharing the information, of course try to solve the lab by yourself before accessing this material.<br>
In order to be able to follow the solutions I'm assuming that you have some knowledge about:
+ how web apllications work
+ Burp Suite CE
+ common web app vulnerabilities (XSS, SQLi, CSRF, XXE...)
+ how to approach a problem 😃

I really encourage to learn the related topic before to access a solution, otherwise it will be very difficult to understand the steps involved. To solve the labs I used Burp CE only, but remember that there are some Labs that requires Burp Professional, these are mentioned in the list but not solved. If you have any questions, suggestions or just to say hallo you can drop me an email: filobers[at]pm[dot]me.

Finally I suggest to have a look at the following resource: https://portswigger.net/web-security/information-disclosure/exploiting before to start.

Enjoy your learning trip!

## Tools
Befroe starting follows a list of useful tool (apart Burp CE) that you should have in your arsenal to perfotm web app PT

- [Turbo intruder](https://github.com/PortSwigger/turbo-intruder)
- [Ffuf](https://github.com/ffuf/ffuf)
- [Web cache vulnerability scanner](https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner/releases)
- [Nikto](https://github.com/sullo/nikto)
- [Wappalyzer browser plugin](https://www.wappalyzer.com/)
- [Netcraft exstension](https://www.netcraft.com/apps/)
- [Nmap](https://nmap.org/) of course...
- [Whatweb](https://github.com/urbanadventurer/WhatWeb)

### Cors
+ [Vulnerability with trusted insecure protocols](./CORS.md#cors-vulnerability-with-trusted-insecure-protocols)
+ [CORS vulnerability with trusted null origin](./CORS.md#cors-vulnerability-with-trusted-null-origin)

### CSRF, XSS
+ [CSRF when token validation depends on request method](./CSRF-XXS.md#csrf-where-token-validation-depends-on-request-method)
+ [CSRF where token validation depends on token being present](CSRF-XXS.md#csrf-where-token-validation-depends-on-request-method)
+ [Exploiting cross-site scripting to capture passwords](./CSRF-XXS.md#exploiting-cross-site-scripting-to-capture-passwords)
+ [DOM XSS using web messages and a JavaScript URL](./CSRF-XXS.md#dom-xss-using-web-messages-and-a-javascript-url)
+ [Exploiting cross-site scripting to steal cookies](./CSRF-XXS.md#exploiting-cross-site-scripting-to-steal-cookies)
+ [DOM XSS in document.write sink using source location.search inside a select element](CSRF-XXS.md#dom-xss-in-documentwrite-sink-using-source-locationsearch-inside-a-select-element)
### SSRF
+ [SSRF with filter bypass via open redirection vulnerability](./SSRF.md#ssrf-with-filter-bypass-via-open-redirection-vulnerability)
+ [SSRF via flawed request parsing](./SSRF.md#ssrf-via-flawed-request-parsing)
+ [SSRF with blacklist-based input filter](./SSRF.md#ssrf-with-blacklist-based-input-filter)
+ [SSRF via OpenID dynamic client registration](./SSRF.md#ssrf-via-openid-dynamic-client-registration)

### SQLi
+ [SQL injection attack, querying the database type and version on MySQL and Microsoft](./SqlI.md#sql-injection-attack-querying-the-database-type-and-version-on-mysql-and-microsoft)
+ [SQL injection attack, listing the database contents on non-Oracle databases](./SqlI.md#sql-injection-attack-listing-the-database-contents-on-non-oracle-databases)
+ Blind SQL injection with out-of-band data exfiltration (requires Burp professional)
+ [SQL injection with filter bypass via XML encoding](./SqlI.md#sql-injection-with-filter-bypass-via-xml-encoding)
+ [Listing the database contents on Oracle](./SqlI.md#sql-injection-attack-listing-the-database-contents-on-oracle)
+ [Blind SQL injection with conditional responses](SqlI.md#blind-sql-injection-with-conditional-responses)

### XXE
+ [Blind XXE with out-of-band interaction via XML parameter entities](./XXE.md#blind-xxe-with-out-of-band-interaction-via-xml-parameter-entities)
+ [Exploiting blind XXE to exfiltrate data using a malicious external DTD](./XXE.md#exploiting-blind-xxe-to-exfiltrate-data-using-a-malicious-external-dtd)
### Authentication && Authorization
+ [OAuth account hijacking via redirect_uri](./authorization_authentication.md#oauth-account-hijacking-via-redirect_uri)
+ [Multi-step process with no access control on one step](./authorization_authentication.md#multi-step-process-with-no-access-control-on-one-step)
+ [Broken brute-force protection with IP block](./authorization_authentication.md#broken-brute-force-protection-with-ip-block)
+ [JWT authentication bypass via weak signing-key](./authorization_authentication.md#jwt-authentication-bypass-via-weak-signing-key)
+ [Forced OAuth profile linking](./authorization_authentication.md#forced-oauth-profile-linking)
+ [Brute-forcing a stay-logged-in cookie](authorization_authentication.md#brute-forcing-a-stay-logged-in-cookie)
+ [2FA broken logic](./authorization_authentication.md#2fa-broken-logic)
+ [JWT authentication bypass via kid header path traversal](./authorization_authentication.md#jwt-authentication-bypass-via-kid-header-path-traversal)
+ [Predicatble session tokens generation](./authorization_authentication.md#predicatble-session-tokens-generation)
+ [CBC bit flipping attack](./authorization_authentication.md#cbc-bit-flipping-attack)

### Click-jacking
+ [Multistep clickjacking](https://github.com/zinzloun/burp_exam_prep/blob/main/clickjacking.md#lab-multistep-clickjacking)
### File upload
+ [Web shell upload via extension blacklist bypass](./file_upload.md#web-shell-upload-via-extension-blacklist-bypass)
### HTTP request smuggling
+ [HTTP request smuggling](./http_request_smuggling.md#http-request-smuggling)
+ [Exploiting HTTP request smuggling to capture other users' requests](./http_request_smuggling.md#exploiting-http-request-smuggling-to-capture-other-users-requests)
### Server-side template injection
+ [Server side template injection](./ss_template_inject.md)
### Insecure deserialization
+ [Using application functionality to exploit insecure deserialization](./insecure_deserialization.md#using-application-functionality-to-exploit-insecure-deserialization)
### Path traversal
+ [File path traversal, traversal sequences stripped non-recursively](./path_traversal.md#file-path-traversal-traversal-sequences-stripped-non-recursively)
### Business logic vulnerabilities
+ [Insufficient workflow validation](./BL_vulnerabilities.md#insufficient-workflow-validation)
### Web socket
+ [Manipulating the WebSocket handshake to exploit vulnerabilities](./WS.md)
### Web cache poisoning
+ [Web Cache poisoning using multiple headers](./web_cache_pois.md#web-cache-poisoning-with-multiple-headers)
+ [Parameter cloaking](./web_cache_pois.md#parameter-cloaking)
### Information disclosure
+ [Version control history](./info_disclosure.md#information-disclosure-in-version-control-history)
### OS command injection
+ [Blind OS command injection with output redirection](./OS_cmd_injection.md#blind-os-command-injection-with-output-redirection)
### JS Protorype pollution
+ [Client-side prototype pollution in third-party libraries](./JS_proto_pollution.md#client-side-prototype-pollution-in-third-party-libraries)
