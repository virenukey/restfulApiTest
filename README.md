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
=> pip install nose
=> pip install requests
=> pip install requests_oauthlib

Note: framework has been developed run and verified on 64 bit Windows platform. To run on Linux, please port following things accordingly
=> setupTest.py
=> testSuites.py

Components
===========
=> Class Api : This is base class wrapper for all Rest API methods (GET, POST, PUT, DELETE)
=> Class ApiAuth: This clild to Api for API authentications
=> testData.json : This is file to define your test data for each test case in json format
=> setupTest.py : This define path to your test data file
=> Class TestData: This is to create object in each test case to bring all test data into test case
=> scripts: Consists of individual test cases
=> testSuits: To run test suites

Run a test
==========
Individual test case can be run using command:
=> nosetests –v testcase2.py
Similarly test suites can be run smilarly from testSuits folder





