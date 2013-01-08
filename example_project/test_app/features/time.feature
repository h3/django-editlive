Feature: Time field
    Functional tests for the editlive Time field

    Scenario: Time initial state
        Given I open the time test page
        Then I see "input#id_time_test[name='time_test'][type='text']"
        Then I see a "charField" editlive for "#id_time_test"
        Then I see "#id_time_test" is hidden
        Then I see a visible placeholder for "#id_time_test"

    Scenario: Time edit mode
        Given I open the time test page
        When I click on the placeholder for "#id_time_test"
        Then I see "#id_time_test" is visible

    Scenario: Time Edit and save
        Given I open the time test page
        When I click on the placeholder for "#id_time_test"
        Then I see "#id_time_test" is visible
        When I input "16:20:00" in "#id_time_test"
        Then the value of "#id_time_test" is "16:20:00"
        Then I see "#id_time_test" is hidden
        Then I see a visible placeholder for "#id_time_test"
        Then I see the placeholder text change to "16:20:00"

    Scenario: Time validation
        Given I open the time test page
        When I click on the placeholder for "#id_time_test"
        When I input "invalid time!" in "#id_time_test"
        Then I see the following error: Enter a valid time.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_time_test"
        Then I see "#id_time_test" is visible
