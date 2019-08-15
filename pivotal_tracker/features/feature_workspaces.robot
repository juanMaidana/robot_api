*** Settings ***
Resource          resources.robot

*** Test Cases ***

Verify that I can update data of a workspace
    ${DATA}=    create dictionary   name    vipre_workspace_2
    Given I start a connection with the Pivotal Tracker API as owner
    When I send a POST request to workspaces with data ${DATA}
    Then I expect the status code is 200


