# FlaskREST

Technical task:

We will create a REST API using Flask framework. 
We will use Mongodb as our database. 
We will utilize redis as our cache. 

Please create a user object with below attributes; 
Full Name
DOB
Gender

Please make sure this object is stored in mongodb.
Please make sure this object is also stored in redis so when we access it, we access it from redis if the cache is still valid. 
Please create /user endpoint with 3 verbs GET, PUT, and POST. 
Using this endpoint, post data into mongodb and redis, 
When using get, try to read from redis first, if not available fallback to mongodb. 
Edit a single user record using PUT method.

Dependencies: list:
Redis, MongoDB, Flask, MongoEngine.

First set up local params in 'config/local.py'.
Run 'flaskRest.py' to start flask server.
By default flask runs with '127.0.0.1:5000' and response to only GET, PUT and POST methods.