*** Settings ***
Library  ../libraries/my_library.py
Library  OperatingSystem

*** Test Cases ***
Create service yml file as an example
    ${PROJECT_PATH}=    get project path
    ${ENV_VARIABLES}=   get environment variables
    ${CURRENT_OS}=      get operating system    ${ENV_VARIABLES}
    ${RAW_CONTENTS}=    get file  ${PROJECT_PATH}/core/docker_compose.dist
    ${FIXED_CONTENTS}=  prepare contents    ${CURRENT_OS}    ${RAW_CONTENTS}
    create file  ${PROJECT_PATH}/core/docker-compose.yml   ${FIXED_CONTENTS}
    run  cd core/ && docker-compose up -d && cd ..
    ${STDOUT}=   run  docker ps --filter "ancestor=mysql:5.7" --format '{{.Names}}'
    should not be equal  ${EMPTY}   ${STDOUT}
    ${STDOUT}=   run  docker ps --filter "ancestor=wordpress" --format '{{.Names}}'
    should not be equal  ${EMPTY}   ${STDOUT}
    run  cd core/ && docker-compose down && cd ..
    remove file  ${PROJECT_PATH}/core/docker-compose.yml
