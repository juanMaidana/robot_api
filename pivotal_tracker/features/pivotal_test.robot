*** Settings ***
Library     libraries/PivotalLibrary.py

*** Test Cases ***
Example that calls a Python keyword
    ${result}=  join two strings    hello   world
    Should be equal     ${result}   hello world
