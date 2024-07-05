Feature: Target main page search tests

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for product
    Then Verify search worked

#  # Make sure scenario names are unique:
#  Scenario: User can search for a product2 on target
#    Given Open target main page
#    # .....

  Scenario: Cart is empty
    Given Open target main page
    When Click cart to view
    Then Verify cart is empty

  Scenario: Logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
