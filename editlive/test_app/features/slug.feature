Feature: Decimal field
    Functional tests for the editlive Decimal field

    Scenario: Initial state
        Given I access the url "/editlive/test/decimal/"
        Then I see "input#id_decimal_test[name='decimal_test'][type='text']"
        Then I see a "charField" editlive for "#id_decimal_test"
        Then I see "#id_decimal_test" is hidden
        Then I see a visible placeholder for "#id_decimal_test"

    Scenario: Edit mode
        Given I access the url "/editlive/test/decimal/"
        When I click on the placeholder for "#id_decimal_test"
        Then I see "#id_decimal_test" is visible
