# Python URL Shortener using flask
## Preview
![Website Preview](https://z.zz.fo/G07SZ.png)
## How it works
Creating a URL shortener you will be able to access long links easier
Example: https://mywebiste.com/80jSj1 will redirect to https://example.com/
## Features
-   Create Short URL via API
-   Delete Short URL via API
-   Get Short URL informations via API
-   Access any links based on route (eg: www.mywebsite.com/XXXXXX)
-   Save Timestamp of creation
-   Filter incorrect formats for URLs
-   Json data storage (**urls.json**)

## API Documentation

>Syntax
```
code -> Short URL code => https://mywebsite.com/code

url -> URL to redirect => https://example.com/
```

  ># Info Short Url
```
POST /info HTTP/1.1
Content-Type: application/x-www-form-urlencoded

code=XXXXXXXXXX
```
##### Example Response (200 OK)
```json
{"timestamp": 1657098673, "url": "https://example.com/"}
```
># Create Short Url
```
POST /create HTTP/1.1
Content-Type: application/x-www-form-urlencoded

url=https://example.com
```
##### Example Response (200 OK)
```json
{"success": true, "already_created": false, "short_url": "XXXXXXXXXX", "url": "https://example.com/"}
```

># Delete Short Url
```
POST /delete HTTP/1.1
Content-Type: application/x-www-form-urlencoded

code=XXXXXXXXXX
```
##### Example Response (200 OK)
```json
{"success": true, "message": "Code deleted!"}
```
># Requirements
>flask
>validators


  

