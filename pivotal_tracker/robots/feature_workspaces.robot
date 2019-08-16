*** Settings ***
Resource          resources.robot

*** Test Cases ***
Verify that I can create a workspace
    ${DATA}=    create dictionary   name    vipre_workspace_2
    Given I start a connection with the Pivotal Tracker API as owner
    When I send a POST request to workspaces with data ${DATA}
    Then I expect the status code is 200


Veirfy taht I can create multiple workspaces
    ${workspace_data_1}=  create dictionary  name=vipre_workspace_4
    ${workspace_data_2}=  create dictionary  name=vipre_workspace_5
    ${workspace_data_3}=  create dictionary  name=vipre_workspace_6
    @{workspaces_data}    create list     ${workspace_data_1}   ${workspace_data_2}     ${workspace_data_3}
    Given I start a connection with the Pivotal Tracker API as owner
    :FOR    ${element}    IN    @{workspaces_data}
    \   When I send a POST request to workspaces with data ${element}
    \   Then I expect the status code is 200
