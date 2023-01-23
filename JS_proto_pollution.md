### Client-side prototype pollution in third-party libraries
#### Lab
 This lab is vulnerable to DOM XSS via client-side prototype pollution. This is due to a gadget in a third-party library, [BBQ](https://github.com/BlackFan/client-side-prototype-pollution/blob/master/pp/jquery-bbq.md), which is difficult to discover due to the minified source code. Although it's technically possible to solve this lab manually, it is recommend using DOM Invader as this will save you a considerable amount of time and effort.

To solve the lab:

1. Use DOM Invader to identify a prototype pollution and a gadget for DOM XSS

1. Use the provided exploit server to deliver a payload to the victim that calls alert(document.cookie) in their browser

First of all we have to enable Prototype pollution in the Attacker section in DOM Invader
--113--
Now reloading the home page and inspecting the DOM Invader TAB we can see that the tool has found a vulnerability into the <b>location.hash property</b>
--114--
We can inspect the source of the storage.js to see the injection point
--115--



#### References
+ https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance
+ https://portswigger.net/web-security/prototype-pollution
