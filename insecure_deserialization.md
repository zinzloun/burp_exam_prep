### Using application functionality to exploit insecure deserialization

#### Intro
Insecure deserialization is when user-controllable data is deserialized by a website. This potentially enables an attacker to manipulate serialized objects in order to pass harmful data into the application code. 

#### Lab
This lab uses a serialization-based session mechanism. To solve the lab, edit the serialized object in the session cookie and use it to delete the morale.txt file from Carlos's home directory.<br>
Let's proceed to deserialize the session cookies once we are logged in:
-- 77 --
We can notice that the user data is passed serialized through the cookie session in PHP format. Furthermore if try to send some fake data we get an error:
-- 78 --
Now switch to the backup user, gregg, delete the account and resend the same request: we are redirected to the home page if the account does not exist anymore. Then I logged in as wiener user, I uploaded an avatar image and I deleted the account again, but this time if we submit again the request we will get an error:
-- 79 --
Luckily the server error is very verbose, and we can understand that:
1. The user avatar image was stored to the file /tmp/mavis.jpg
2. When the user delete event occurs, the associated avatar image is also deleted
3. The source code is stored in /home/carlos/User.php

Knowing that we can try to modify the session cookie setting  the value for the avatar link to point to the file that has to be deleted:
```
O:4:"User":3:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"j1qrlmlnwheiop14d31ialg4y5up18sc";s:11:"avatar_link";s:23:"/home/carlos/morale.txt";}
```
So enable the capture on the Proxy and intercept the delete request, then encode to Base64 the above paylod and set it as session cookie, then forward the request to the server:
-- 80 --
You should solve the Lab




#### References
+ https://en.wikipedia.org/wiki/PHP_serialization_format
+ https://portswigger.net/web-security/deserialization
