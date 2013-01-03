Feature: datetimeTime field
    Functional tests for the editlive datetimeTime field

    Scenario: Initial state
        Given I access the url "/editlive/test/datetime/"
        Then I see "input#id_datetime_test[name='datetime_test'][type='text']"
        Then I see a "datetimeField" editlive for "#id_datetime_test"
        Then I see "#id_datetime_test" is hidden
        Then I see a visible placeholder for "#id_datetime_test"

    Scenario: Edit mode
        Given I access the url "/editlive/test/datetime/"
        When I click on the placeholder for "#id_datetime_test"
        Then I see "#id_datetime_test" is visible

