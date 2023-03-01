Feature: Home Screen

  Background:
    Given We are in the Home Page
    When We tap on first product


  @e2e
  Scenario: validate_product_price
    Then We see the Product's price
    And We see the Product's name



  @e2e
  Scenario: validate_add_to_cart
    When We tap on Add To Cart
    Then We see a number one on the Cart
