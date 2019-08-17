*** Settings ***
Library     ../libraries/pivotal_library.py

*** Keywords ***
A connection is started with Pivotal Tracker API as ${USERNAME}
    log in api  owner

A ${HTTP_TYPE} request is sent to ${ENDPOINT} with data ${DATA}
    send_user_request  ${HTTP_TYPE}   ${ENDPOINT}    ${DATA}

Status code ${CODE} is expected
    ${status_code}=     get status code
    should be equal     ${status_code}     ${CODE}

Is expected that response ${VALUE} is not empty
    ${id}=  get from response   ${VALUE}
    should not be equal  ${EMPTY}   ${id}
