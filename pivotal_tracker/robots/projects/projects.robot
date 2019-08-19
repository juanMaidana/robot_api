*** Settings ***
Resource    ../resources.robot

*** Test Cases ***
Verify that I can get the user's projects list
    do request  GET     projects    owner   ${none}
    ${status_code}=     get status code
    should be equal     ${status_code}     200

Verify that I can create a new project
    ${data} =  create dictionary
    ...     name    $R(0)_project_$R(1)
    do request   POST    projects   owner   ${data}
    ${status_code}=     get status code
    should be equal     ${status_code}     200
    ${id}=  get from response   id
    should not be equal  ${EMPTY}   ${id}

# Gherkin Test Cases
Verify that I can get the user's project list - Gherkin version
    Given I start a connection with the Pivotal Tracker API as owner
    When I send a GET request to projects with data ${EMPTY}
    Then I expect the status code is 200

Verify that I can create a new project - Gherkin version
    ${project_data} =  create dictionary
    ...     name    $R(0)_project_$R(1)
    Given I start a connection with the Pivotal Tracker API as owner
    When I send a POST request to projects with data ${project_data}
    Then I expect the status code is 200
    And I expect the reponse id is not empty

Veirfy that I can create multiple projects
    ${project_data_1}=  create dictionary  name=$R(0)_project1_$R(1)
    ${project_data_2}=  create dictionary  name=$R(0)_project2_$R(1)
    ${project_data_3}=  create dictionary  name=$R(0)_project3_$R(1)
    @{projects_data}    create list     ${project_data_1}   ${project_data_2}   ${project_data_3}
    :FOR    ${element}    IN    @{projects_data}
    \   Given I start a connection with the Pivotal Tracker API as owner
    \   When I send a POST request to projects with data ${element}
    \   Then I expect the status code is 200
    \   And I expect the reponse id is not empty