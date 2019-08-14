*** Settings ***
Library     libraries/PivotalLibrary.py

*** Keywords ***

I connect to pivotal tracker

I send a "${feature}" request with name "${name}"
${data} =  create dictionary
    ...     name    ${name}
    do request   POST    projects   owner   ${data}
    ${status_code}=     get status code
    should be equal     ${status_code}     200
    ${id}=  get from response   id
    should not be equal  ${EMPTY}   ${id}

I expect successful code "${code}"

    should be equal  true   true

I exist
    should be equal  true   true

I am happy
    should be equal  true   true
