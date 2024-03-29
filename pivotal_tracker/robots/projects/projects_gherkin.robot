*** Settings ***
Resource    ../resources.robot
Suite Setup  A connection is started with Pivotal Tracker API as owner

*** Test Cases ***
# Gherkin Test Cases
Verify that I can get the user's project list - Gherkin version
    [Tags]  Gherkin  acceptance
    When A GET request is sent to projects with data ${EMPTY}
    Then Status code 200 is expected

Verify that I can create a new project - Gherkin version
    [Tags]  Gherkin  acceptance
    ${project_data}=  create dictionary  name=$R(0)_project_$R(1)
    When A POST request is sent to projects with data ${project_data}
    Then Status code 200 is expected
    And Is expected that response id is not empty

Veirfy that I can create multiple projects
    [Tags]  Gherkin  functional
    ${project_data_1}=  create dictionary  name=$R(0)_project1_$R(1)
    ${project_data_2}=  create dictionary  name=$R(0)_project2_$R(1)
    ${project_data_3}=  create dictionary  name=$R(0)_project3_$R(1)
    @{projects_data}  create list  ${project_data_1}  ${project_data_2}  ${project_data_3}
    :FOR  ${element}  IN  @{projects_data}
    \   When A POST request is sent to projects with data ${element}
    \   Then Status code 200 is expected
    \   Is expected that response id is not empty