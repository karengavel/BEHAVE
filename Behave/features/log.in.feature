Feature: Log In

  Background:
    Given we are in the Home Page

  @e2e
  Scenario: login_correct_credentials
    Given we tap in the side menu
    When we tap on Log In


    Then we are in the Home Page

