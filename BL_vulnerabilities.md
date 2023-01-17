### Insufficient workflow validation

#### LAB
This Lab ha a security flaw in the purchising steps. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

We can start to peform a purchase and to inspect the requests made to server during this process. First of all we can see that we have to be logged in to proceed with the check-out, so let's proceed to log-in. Once logged we can see that wiener has a credit of $100, let's try again to buy an item:
--88--
The purchase flow is composed by 3 requests:
1. add an item to the cart: 
```
POST /cart HTTP/1.1
Host: 0a9e001a04a8bde2c03410b60063009f.web-security-academy.net
Cookie: session=0hRcKcZHLlsKBBHJcr5H4jHaLKJB4H9s
...
Connection: close

productId=2&redir=PRODUCT&quantity=1
```
2. cart check-out (with csrf token)
```
POST /cart/checkout HTTP/1.1
Host: 0a9e001a04a8bde2c03410b60063009f.web-security-academy.net
Cookie: session=0hRcKcZHLlsKBBHJcr5H4jHaLKJB4H9s
...
Connection: close

csrf=jWRswYUqtvd8Fm2hQesbCXTQSfvwhkny
```
3. a confirmation
```
GET /cart/order-confirmation?order-confirmed=true HTTP/1.1
Host: 0a9e001a04a8bde2c03410b60063009f.web-security-academy.net
Cookie: session=0hRcKcZHLlsKBBHJcr5H4jHaLKJB4H9s
...
Connection: close
```
#### References
