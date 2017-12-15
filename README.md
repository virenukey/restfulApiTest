RESTFul API Test
================

Framework for testing (RESTful) HTTP/HTTPS APIs
=================================================
This framework allows you to develop test cases for verifying any kind of HTTP/HTTPS API with various Input Parameters.
Test cases can be developed using Python and incorporated Nose Unit test framework to run/report and execute test suites

Advantage of this framework
============================
Testing RESTful APIs generally involves two prediticable steps -

- Invoke the API end point
- Validate the response - headers, payload etc

Most testing tools available for testing RESTful APIs use some sort of
a GUI based approach which doesn't lend itself towards re-use, better
code organization, abstraction and some of the other benefits that
are generally available with programmatic frameworks. 
Programmatically building test cases provides the highest level
of flexibility and sophistication. 
This framework supports HTTP/HTTPS RestAPI calls. All available Authentication supports (including OAUTH)

Note: As of now this framework only supports APIs whose responsetype is JSON.


# Practical uses of "RESTFul API Test"
- Perform "integration" testing of internal and external API endpoints
- Examine and test complex response payloads
- You can simply use this framework to dump and analyze API responses - headers, payload etc.


Prerequisites
================
Using Python pip install following packages:
1. pip install nose
2. pip install requests
3. pip install requests_oauthlib

Note: framework has been developed run and verified on 64 bit Windows platform. To run on Linux, please port following things accordingly
1. setupTest.py
2. testSuites.py

Components
===========
1. Class Api : This is base class wrapper for all Rest API methods (GET, POST, PUT, DELETE)
2. Class ApiAuth: This clild to Api for API authentications
3. testData.json : This is file to define your test data for each test case in json format
4. setupTest.py : This define path to your test data file
5. Class TestData: This is to create object in each test case to bring all test data into test case
6. scripts: Consists of individual test cases
7. testSuits: To run test suites

Run a test
==========
Individual test case can be run using command:
1. nosetests –v testcase2.py
Similarly test suites can be run smilarly from testSuits folder

Limitations
=============
1. Parses only json type response
2. Need to incorporate REST PUT and DELETE methods

"# restfulApiTest" 
