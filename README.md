# Robot Framework API (robot_api)
API Testing using RobotFramework. 

Currently working with Ubuntu and CentOS.

## Requirements
* python2.7 (specific libraries can be found on requirements.txt).
* docker.
* docker-compose.

### Sample Test Cases
These are sample test cases that can work as a guide for more complex development. 
All these samples can be found on the "core" folder and can be run with the command.
```
python -m robot -d test_results/ examples/robots/tests*.robot
```
*You may manually create a test_results/ folder or change the results path.*

### Pivotal Tracker Test Cases
Create a config.json file with your credentials. 
A template can be found on: pivotal_tracker/config.dist. 
More details [here](#generating-pivotal-config-file).

Then, simply run the following command.
```
python setup.py
```
 All the attributes (listener, loglevel, etc.) that are sent to execute the application are included in setup.json.  

*You might need an account with free-trial account by default. 
All test objects created are deleted at the end of execution*

### Generating Pivotal Config File
Copy the template on pivotal_tracker/config.dist and create a config.json file on the same directory.
Then, fill the missing values as it follows:
* **base_url**: the url to do the http request on its base form, example for APIv5 "https://www.pivotaltracker.com/services/v5".
* **headers**: headers for the request, for APIv5 token=X-TrackerToken and contents="Content-Type".
* **users**: the token the is going to be used to log in the Pivotal Tracker API service. 
It can usually be found on your Pivotal Tracker account information.

*Once you create this configuration file correctly, you should be able to run all tests files.*

