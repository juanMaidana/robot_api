*** Settings ***
Resource          ../resources.robot

*** Test Cases ***
Verify that I can create a workspace
    [Tags]      Gherkins  acceptance
    ${DATA}=    create dictionary   name    vipre_workspace_2
    [Setup]     A connection is started with Pivotal Tracker API as owner
    When A POST request is sent to workspaces with data ${DATA}
    Then Status code 200 is expected


Veirfy that I can create multiple workspaces
    [Tags]      Gherkins    functional
    ${workspace_data_1}=  create dictionary  name=vipre_workspace_4
    ${workspace_data_2}=  create dictionary  name=vipre_workspace_5
    ${workspace_data_3}=  create dictionary  name=vipre_workspace_6
    @{workspaces_data}    create list     ${workspace_data_1}   ${workspace_data_2}     ${workspace_data_3}
    Given A connection is started with Pivotal Tracker API as owner
    :FOR    ${element}    IN    @{workspaces_data}
    \   When A POST request is sent to workspaces with data ${element}
    \   Then Status code 200 is expected
