### Using application functionality to exploit insecure deserialization

#### Intro
Insecure deserialization is when user-controllable data is deserialized by a website. This potentially enables an attacker to manipulate serialized objects in order to pass harmful data into the application code. 

#### Lab
This lab uses a serialization-based session mechanism. To solve the lab, edit the serialized object in the session cookie and use it to delete the morale.txt file from Carlos's home directory.<br>
Let's proceed to deserialize the session cookies once we are logged in:
-- 77 --
We can notice that the user data is passed serialized through the cookie session in PHP format. Furthermore if try to send some fake data we get an error:
-- 78 --
Now switch to the backup user, gregg, delete account and resend the same request. We will get a server error with some useful information:


#### References
+ https://en.wikipedia.org/wiki/PHP_serialization_format
+ https://portswigger.net/web-security/deserialization
