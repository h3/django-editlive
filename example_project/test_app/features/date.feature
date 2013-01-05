Feature: Date field tests
    Functional tests for the editlive Date field

    Scenario: Date Initial state
        Given I open the date test page
        Then I see "input#id_date_test[name='date_test'][type='text']"
        Then I see a "dateField" editlive for "#id_date_test"
        Then I see "#id_date_test" is hidden
        Then I see a visible placeholder for "#id_date_test"

    Scenario: Date Edit mode
        Given I open the date test page
        When I click on the placeholder for "#id_date_test"
        Then I see "#id_date_test" is visible

#   Scenario: Date Edit and save
#       Given I open the date test page
#       When I click on the placeholder for "#id_date_test"
#       Then I see "#id_date_test" is visible
#       When I input "01/01/2013" in "#id_date_test"
#       Then the value of "#id_date_test" is "2013-01-01"
#       Then I see "#id_date_test" is hidden
#       Then I see a visible placeholder for "#id_date_test"
