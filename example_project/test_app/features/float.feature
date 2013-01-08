Feature: Float field
    Functional tests for the editlive Float field

    Scenario: Float initial state
        Given I open the float test page
        Then I see "input#id_float_test[name='float_test'][type='text']"
        Then I see a "charField" editlive for "#id_float_test"
        Then I see "#id_float_test" is hidden
        Then I see a visible placeholder for "#id_float_test"

    Scenario: Float edit mode
        Given I open the float test page
        When I click on the placeholder for "#id_float_test"
        Then I see "#id_float_test" is visible

    Scenario: Float edit and save
        Given I open the float test page
        When I click on the placeholder for "#id_float_test"
        Then I see "#id_float_test" is visible
        When I input "1.23" in "#id_float_test"
        Then the value of "#id_float_test" is "1.23"
        Then I see "#id_float_test" is hidden
        Then I see a visible placeholder for "#id_float_test"
        Then I see the placeholder text change to "1.23"

    Scenario: Float validation
        Given I open the float test page
        When I click on the placeholder for "#id_float_test"
        When I input "blah blah" in "#id_float_test"
        Then I see the following error: Enter a number.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_float_test"
        Then I see "#id_float_test" is visible
