*** Settings ***
Resource    ../resources.robot
Suite Setup  A connection is started with Pivotal Tracker API as owner

*** Test Cases ***
# Gherkin Test Cases
Verify that I can get the user's project list - Gherkin version
    [Tags]  Gherkins    acceptance
    When A GET request is sent to projects with data ${EMPTY}
    Then Status code 200 is expected

Verify that I can create a new project - Gherkin version
    [Tags]  Gherkins    acceptance
    ${project_data} =  create dictionary    name=vipre_project_test_2
    When A POST request is sent to projects with data ${project_data}
    Then Status code 200 is expected
    And Is expected that response id is not empty

Veirfy that I can create multiple projects
    [Tags]  Gherkins    functional
    ${project_data_1}=  create dictionary  name=vipre_project_4
    ${project_data_2}=  create dictionary  name=vipre_project_5
    ${project_data_3}=  create dictionary  name=vipre_project_6
    @{projects_data}    create list     ${project_data_1}   ${project_data_2}   ${project_data_3}
    :FOR    ${element}    IN    @{projects_data}
    \   When A POST request is sent to projects with data ${element}
    \   Then Status code 200 is expected
    \   Is expected that response id is not empty