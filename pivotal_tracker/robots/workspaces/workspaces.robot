*** Settings ***
Resource          ../resources.robot

*** Test Cases ***
Verify that I can create a workspace
    [Tags]  Gherkin  acceptance
    ${DATA}=  create dictionary   name    $R(0)_$R(1)
    [Setup]  A connection is started with Pivotal Tracker API as owner
    When A POST request is sent to workspaces with data ${DATA}
    Then Status code 200 is expected

Veirfy that I can create multiple workspaces
    [Tags]  Gherkins  functional
    ${workspace_data_1}=  create dictionary  name=$R(0)1$R(1)
    ${workspace_data_2}=  create dictionary  name=$R(0)2$R(1)
    ${workspace_data_3}=  create dictionary  name=$R(0)3$R(1)
    @{workspaces_data}  create list  ${workspace_data_1}  ${workspace_data_2}  ${workspace_data_3}
    Given A connection is started with Pivotal Tracker API as owner
    :FOR  ${element}  IN  @{workspaces_data}
    \   When A POST request is sent to workspaces with data ${element}
    \   Then Status code 200 is expected
