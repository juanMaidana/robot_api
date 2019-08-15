*** Settings ***
Library  ../libraries/my_library.py
Library  OperatingSystem

*** Keywords ***
# Environmental Variables management
The environment variable ${TAG} is set to ${EXPECTED_VALUE}
    ${CURRENT_VALUE}=     get environment variable   ${TAG}
    should be equal     ${CURRENT_VALUE}    ${EXPECTED_VALUE}

I set the environment variable ${TAG} to ${VALUE}
    set environment variable   ${TAG}     ${VALUE}

I remove the variable ${TAG} from environment
    remove environment variable  ${TAG}