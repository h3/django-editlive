Feature: PositiveSmallInteger field
    Functional tests for the editlive PositiveSmallInteger field

    Scenario: Initial state
        Given I open the positivesmallinteger test page
        Then I see "input#id_positivesmallinteger_test[name='positivesmallinteger_test'][type='text']"
        Then I see a "charField" editlive for "#id_positivesmallinteger_test"
        Then I see "#id_positivesmallinteger_test" is hidden
        Then I see a visible placeholder for "#id_positivesmallinteger_test"

    Scenario: Edit mode
        Given I open the positivesmallinteger test page
        When I click on the placeholder for "#id_positivesmallinteger_test"
        Then I see "#id_positivesmallinteger_test" is visible

    Scenario: PositiveInteger edit and save
        Given I open the positivesmallinteger test page
        When I click on the placeholder for "#id_positivesmallinteger_test"
        Then I see "#id_positivesmallinteger_test" is visible
        When I input "1" in "#id_positivesmallinteger_test"
        Then the value of "#id_positivesmallinteger_test" is "1"
        Then I see "#id_positivesmallinteger_test" is hidden
        Then I see a visible placeholder for "#id_positivesmallinteger_test"
        Then I see the placeholder text change to "1"

    Scenario: PositiveInteger invalid (negative)
        Given I open the positivesmallinteger test page
        When I click on the placeholder for "#id_positivesmallinteger_test"
        When I input "-1" in "#id_positivesmallinteger_test"
        Then I see the following error: Ensure this value is greater than or equal to 0.

    Scenario: PositiveInteger invalid
        Given I open the positivesmallinteger test page
        When I click on the placeholder for "#id_positivesmallinteger_test"
        When I input "a" in "#id_positivesmallinteger_test"
        Then I see the following error: Enter a whole number.
