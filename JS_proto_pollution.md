### Client-side prototype pollution in third-party libraries
In order to perform a client side prototype pollution we need to meet the following conditions:
- a way to poison the prototype, referred to as a prototype pollution source.
- a way to use a poisoned prototype for an actual exploit, referred to as a prototype pollution gadget.

<i>More information in the [refernces section](JS_proto_pollution.md#references)</i>
#### Lab
 This lab is vulnerable to DOM XSS via client-side prototype pollution. This is due to a gadget in a third-party library, Google analytics (ga.js) which is difficult to discover due to the minified source code. Although it's technically possible to solve this lab manually, it is recommend using DOM Invader as this will save you a considerable amount of time and effort.

To solve the lab:

1. Use DOM Invader to identify a prototype pollution and a gadget for DOM XSS

1. Use the provided exploit server to deliver a payload to the victim that calls alert(document.cookie) in their browser

First of all we have to enable Prototype pollution in the Attacker section in DOM Invader
--113--
Now reloading the home page and inspecting the DOM Invader TAB we can see that the tool has found a pollution vector into the <b>location.hash property</b>
--114--
We can inspect the source of the storage.js to see the injection point
--115--
Now if we test (1) the attack vector we can see that it succeed
--116--
and the property is set to the object prototype with the relativa value. Now we need to find a suitable <b>gadget</b>, again we can take advantage od DOM Incader to perform this operation. CLick on Scan for gadgets (1) as shown below:
--117--
A gadget is found: <b>hitCallback</b>. As previously mentioned this a feature sused in Google analytics (GA)  that allows to execute a function after a hit is successfully sent to GA.



#### References
+ https://portswigger.net/web-security/prototype-pollution/javascript-prototypes-and-inheritance
+ https://portswigger.net/web-security/prototype-pollution
+ https://portswigger.net/research/widespread-prototype-pollution-gadgets
