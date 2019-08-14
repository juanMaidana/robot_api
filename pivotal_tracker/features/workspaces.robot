*** Settings ***
Resource          resource.robot

*** Keywords ***

Verify that I can update data of a workspace
    Given I connect to pivotal tracker
    When I send a "POST" request with name "workspace_1"
    And I send a "PUT" request with name "workspace_update"
    Then I expect successful code "200"


*** Keywords ***








${data} =  create dictionary
    ...     name    viper_test
    do request   POST    projects   owner   ${data}
    ${status_code}=     get status code
    should be equal     ${status_code}     200
    ${id}=  get from response   id
    should not be equal  ${EMPTY}   ${id}