Feature: Float field
    Functional tests for the editlive Float field

    Scenario: Initial state
        Given I access the url "/test/float/"
        Then I see "input#id_float_test[name='float_test'][type='text']"
        Then I see a "charField" editlive for "#id_float_test"
        Then I see "#id_float_test" is hidden
        Then I see a visible placeholder for "#id_float_test"

    Scenario: Edit mode
        Given I access the url "/test/float/"
        When I click on the placeholder for "#id_float_test"
        Then I see "#id_float_test" is visible
