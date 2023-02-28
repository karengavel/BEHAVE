Feature: Home Screen

  Background:
    Given We are in the Home Page

  @e2e
  Scenario: validate_product_name
    When We tap on first product
    Then We see the Product's price
