# robot_api
API Testing using RobotFramework

## Execute Test files
To execute sample test files found core.
```
python -m robot -d test_results/ core/robots/*.robot
```
You should manually create a test_results/ folder or change the results path.

### To Test Pivotal Tracker with Hooks
Create a config.json file with your credentials. An example can be found on: pivotal_tracker/config.dist

Then, simply run:
```
python -m robot -d test_results/ --listener pivotal_tracker/features/MyListener.py pivotal_tracker/features/feature*.robot
```