Feature: PositiveInteger field
    Functional tests for the editlive PositiveInteger field

    Scenario: Initial state
        Given I access the url "/test/positiveinteger/"
        Then I see "input#id_positiveinteger_test[name='positiveinteger_test'][type='text']"
        Then I see a "charField" editlive for "#id_positiveinteger_test"
        Then I see "#id_positiveinteger_test" is hidden
        Then I see a visible placeholder for "#id_positiveinteger_test"

    Scenario: Edit mode
        Given I access the url "/test/positiveinteger/"
        When I click on the placeholder for "#id_positiveinteger_test"
        Then I see "#id_positiveinteger_test" is visible
