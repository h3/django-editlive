Feature: Time field
    Functional tests for the editlive Time field

    Scenario: Initial state
        Given I access the url "/test/time/"
        Then I see "input#id_time_test[name='time_test'][type='text']"
        Then I see a "charField" editlive for "#id_time_test"
        Then I see "#id_time_test" is hidden
        Then I see a visible placeholder for "#id_time_test"

    Scenario: Edit mode
        Given I access the url "/test/time/"
        When I click on the placeholder for "#id_time_test"
        Then I see "#id_time_test" is visible
