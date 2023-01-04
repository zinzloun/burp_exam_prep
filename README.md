# Burp Exam Roadtrip
## Labs
### Web shell upload via extension blacklist bypass
Concepts: Load an .httacces file to allow a file with a custom extension .pws to be executed as PHP file
<br>![img](./img/1.png)<br>
The httaccess file is uploaded<br>![img](./img/2.png) 
<br>Upload your webshell as .pws file<br>![img](./img/2.png)
<br>Now inspect the source code of your account page<br>
![img](./img/3.png)<br>Visit the img src URL and you get the secret
