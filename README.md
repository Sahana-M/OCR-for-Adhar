 <h3>Actyv ocr : Version 1.0

---
Usage : This API is designed to extract general fields from Adhar card
**URL** :- https://custom-ocr.herokuapp.com/get_adhar

It accepts 2 types of documents,
 - Adhar front image
 - Adhar back image
---
<h3>Exractions

> **Adhar front**

The general fields extracted from uploaded Adhar front image includes,
|Fields extracted|  
|--|
|Name| 
|DOB|
|Gender| 
|Father/Husband name| 
|Age| 
|Adhar number| 
|Document identified| 

>**Adhar back**

The general fields extracted from uploaded Adhar back image includes,
|Fields extracted|  
|--|
|Address| 
|Pincode|
|Document identified| 

---
<h3>Usage :

<H4>Request format

    Request - POST
    Request URL - https://custom-ocr.herokuapp.com/get_adhar
    In Body -> raw format -> <b>JSON request
    Example :-
	    {
	    "file" : "image_url"
	    }

<h4>Response format - Adhar front

    Response type - JSON response
    Example :-
    {
    "age": age,
    "dob": "dd/mm/yyyy",
    "father": "father name",
    "fileIdentified": "document_front.jpg",
    "gender": "MALE/FEMALE",
    "husband": "husband name",
    "idNumber": "adhar number",
    "name": "name"
    }
   
<h4>Response format - Adhar front
   

    Response type - JSON response
    Example :-
    {
    "address": "xxxxxx",
    "fileIdentified" : "document_back.jpg",
    "pincode" : "xxxxxx"
    }
    


