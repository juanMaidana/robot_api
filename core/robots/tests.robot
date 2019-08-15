*** Settings ***
Library     ../libraries/MyLibrary.py

*** Test Cases ***
Example that calls a Python keyword
    ${result}=  join two strings    hello   world
    Should be equal     ${result}   hello world

Exmample that creates a dictionary
    ${data}=    create dictionary
    ...     name    hello
    ...     second  world
    should be equal  ${data.name}   hello
    should be equal  ${data.second}   world
