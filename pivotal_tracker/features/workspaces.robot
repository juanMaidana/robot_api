*** Settings ***
Library     libraries/PivotalLibrary.py

*** Keywords ***

I can use Gherkins
    should be equal  true   true

I exist
    should be equal  true   true

I am happy
    should be equal  true   true
