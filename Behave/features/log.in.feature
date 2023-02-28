Feature: Log In

  Background:
    Given We are in the Home Page

  @e2e
  Scenario: login_correct_credentials
    Given We tap in the side menu
    When We tap on Log In
    And We enter the correct user
    And We enter the correct password
    And Tap on the Log In button
    Then We are in the Home Page

