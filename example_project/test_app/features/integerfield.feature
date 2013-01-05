Feature: Integer field
    Functional tests for the editlive Integer field

    Scenario: Initial state
        Given I access the url "/test/integer/"
        Then I see "input#id_integer_test[name='integer_test'][type='text']"
        Then I see a "charField" editlive for "#id_integer_test"
        Then I see "#id_integer_test" is hidden
        Then I see a visible placeholder for "#id_integer_test"

    Scenario: Edit mode
        Given I access the url "/test/integer/"
        When I click on the placeholder for "#id_integer_test"
        Then I see "#id_integer_test" is visible
