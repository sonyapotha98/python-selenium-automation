Feature: Tests for Cart functionality

#  Scenario: 'Your cart is empty' message is shown for empty cart
#    Given Open target main page
#    When Click on Cart icon
#    Then Verify 'Your cart is empty' message is shown

    Scenario: Cart is empty
      Given Open target main page
      When  Click cart to view
      Then  Verify cart is empty



    Scenario: Add an item to cart
      Given Open target main page
      When  Search for mug
      And  Add mug to cart
      And  Save the expected product name
      And  From right side navigation menu, click add to cart
      And Open cart page
      Then Verify cart has the product

#  Scenario: User can add a product to cart
#    Given Open target main page
#    When Search for mug
#    And Click on Add to Cart button
#    And Store product name
#    And Confirm Add to Cart button from side navigation
#    And Open cart page
#    Then Verify cart has 1 item(s)
#    And Verify cart has correct product




