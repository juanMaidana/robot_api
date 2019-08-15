# robot_api
API Testing using RobotFramework

## Execute Test files
To execute sample test files found core.
```
python -m robot -d test_results/ core/robots/tests*.robot
```
You should manually create a test_results/ folder or change the results path.

### To Test Pivotal Tracker with Hooks
Create a config.json file with your credentials. A template can be found on: pivotal_tracker/config.dist

Then, simply run the following command.
```
python -m robot -d test_results/ --listener pivotal_tracker/libraries/pivotal_listener.py pivotal_tracker/robots/feature*.robot
```
