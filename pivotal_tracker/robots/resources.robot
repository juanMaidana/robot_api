*** Settings ***
Library     ../libraries/pivotal_library.py

*** Keywords ***
I start a connection with the Pivotal Tracker API as ${USERNAME}
    log in api  owner

I send a ${HTTP_TYPE} request to ${ENDPOINT} with data ${DATA}
    do user request  ${HTTP_TYPE}   ${ENDPOINT}    ${DATA}

I expect the status code is ${CODE}
    ${status_code}=     get status code
    should be equal     ${status_code}     200

I expect the reponse ${VALUE} is not empty
    ${id}=  get from response   ${VALUE}
    should not be equal  ${EMPTY}   ${id}
