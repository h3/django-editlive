Feature: Date field tests
    Functional tests for the editlive Date field

    Scenario: Date Initial state
        Given I access the url "/test/date/"
        Then I see "input#id_date_test[name='date_test'][type='text']"
        Then I see a "dateField" editlive for "#id_date_test"
        Then I see "#id_date_test" is hidden
        Then I see a visible placeholder for "#id_date_test"

    Scenario: Date Edit mode
        Given I access the url "/test/date/"
        When I click on the placeholder for "#id_date_test"
        Then I see "#id_date_test" is visible

