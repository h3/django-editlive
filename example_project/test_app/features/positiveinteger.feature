Feature: PositiveInteger field
    Functional tests for the editlive PositiveInteger field

    Scenario: PositiveInteger initial state
        Given I'm TestMan
        Given I open the positiveinteger test page
        Then I see "input#id_positiveinteger_test[name='positiveinteger_test'][type='text']"
        Then I see a "charField" editlive for "#id_positiveinteger_test"
        Then I see "#id_positiveinteger_test" is hidden
        Then I see a visible placeholder for "#id_positiveinteger_test"

    Scenario: PositiveInteger edit mode
        Given I'm TestMan
        Given I open the positiveinteger test page
        When I click on the placeholder for "#id_positiveinteger_test"
        Then I see "#id_positiveinteger_test" is visible

    Scenario: PositiveInteger edit and save
        Given I'm TestMan
        Given I open the positiveinteger test page
        When I click on the placeholder for "#id_positiveinteger_test"
        Then I see "#id_positiveinteger_test" is visible
        When I input "1" in "#id_positiveinteger_test"
        Then the value of "#id_positiveinteger_test" is "1"
        Then I see "#id_positiveinteger_test" is hidden
        Then I see a visible placeholder for "#id_positiveinteger_test"
        Then I see the placeholder text change to "1"

    Scenario: PositiveInteger invalid (negative)
        Given I'm TestMan
        Given I open the positiveinteger test page
        When I click on the placeholder for "#id_positiveinteger_test"
        When I input "-1" in "#id_positiveinteger_test"
        Then I see the following error: Ensure this value is greater than or equal to 0.

    Scenario: PositiveInteger validation
        Given I'm TestMan
        Given I open the positiveinteger test page
        When I click on the placeholder for "#id_positiveinteger_test"
        When I input "a" in "#id_positiveinteger_test"
        Then I see the following error: Enter a whole number.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_positiveinteger_test"
        Then I see "#id_positiveinteger_test" is visible

    Scenario: Anonymous mode
        Given I open the char test page
        Then I don't see ".editlive"
