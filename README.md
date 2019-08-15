# Robot Framework API (robot_api)
API Testing using RobotFramework. 

Currently working with Ubuntu and CentOS.

## Requirements
* python2.7 (specific libraries can be found on requirements.txt).
* docker.
* docker-compose.

### Core Test Cases
These are sample test cases that can work as a guide for more complex development. 
All these samples can be found on the "core" folder and can be run with the command.
```
python -m robot -d test_results/ core/robots/tests*.robot
```
*You may manually create a test_results/ folder or change the results path.*

### Pivotal Tracker Test Cases
Create a config.json file with your credentials. A template can be found on: pivotal_tracker/config.dist

Then, simply run the following command.
```
python -m robot -d test_results/ --listener pivotal_tracker/libraries/pivotal_listener.py pivotal_tracker/robots/feature*.robot
```
*You might need an account with free-trial account by default. 
All test objects created are deleted at the end of execution*
