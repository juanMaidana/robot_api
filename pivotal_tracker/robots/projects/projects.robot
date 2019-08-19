*** Settings ***
Resource    ../resources.robot

*** Test Cases ***
Verify that I can get the user's projects list
    do request  GET     projects    owner   ${none}
    ${status_code}=     get status code
    should be equal     ${status_code}     200

Verify that I can create a new project
    ${data} =  create dictionary
    ...     name    vipre_project_test_1
    do request   POST    projects   owner   ${data}
    ${status_code}=     get status code
    should be equal     ${status_code}     200
    ${id}=  get from response   id
    should not be equal  ${EMPTY}   ${id}