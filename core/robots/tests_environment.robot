*** Settings ***
Resource    core_resources.robot

*** Test Cases ***
Verify that I can change my username environment variable
    Given The environment variable USERNAME is set to gabriel
    When I set the environment variable VIPRE_TEST_VARIABLE to luis
    Then The environment variable VIPRE_TEST_VARIABLE is set to luis
    And I remove the variable VIPRE_TEST_VARIABLE from environment

Create service yml file as an example
    ${PROJECT_PATH}=    get project path
    ${CONTENTS}=    get file  ${PROJECT_PATH}/core/docker_compose.dist
    create file  ${PROJECT_PATH}/core/docker_compose.yml   ${CONTENTS}
    remove file  ${PROJECT_PATH}/core/docker_compose.yml
