# Hospital_Booking_Slot_Rest_API


Bed Booking REST API using Django and MongoDB. Here, you can see the booking table with name,pateint critical condition,pincode ,particular hospital and time slot
You can book , Reschdule and cancel the booking by using http methods via get, post, patch,delete.

The best way to reduce API response time is caching.  As because of caching we don't have to query over the database everytime user request the same output. And also avoid using PUT if the request can be done by PATCH.
as PUT completely replace the data with new given data.



# Quick Start


* Install all the required libraries using the pip command : 

    `pip install -r requirements.txt`
    
* Start Up your mongodb Local Server :

    `mongod`
 
* If you are using mongoAtlas make Sure to Change the Host and port from setting.py

* Run the API by using :

  `python manage.py runserver`
 
 
* you can use [POSTMAN](https://www.postman.com/api-platform/api-testing/) for further API testing at :

  `localhost:8080`


