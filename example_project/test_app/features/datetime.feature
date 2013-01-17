Feature: DateTime field tests
    Functional tests for the editlive DateTime field

    Scenario: Datetime Initial state
        Given I'm TestMan
        Given I open the datetime test page
        Then I see "input#id_datetime_test[name='datetime_test'][type='text']"
        Then I see a "datetimeField" editlive for "#id_datetime_test"
        Then I see "#id_datetime_test" is hidden
        Then I see a visible placeholder for "#id_datetime_test"

    Scenario: Datetime Edit mode
        Given I'm TestMan
        Given I open the datetime test page
        When I click on the placeholder for "#id_datetime_test"
        Then I see "#id_datetime_test" is visible

#   Scenario: Datetime Edit and save
#       Given I'm TestMan
#       Given I open the datetime test page
#       When I click on the placeholder for "#id_datetime_test"
#       Then I see "#id_datetime_test" is visible
#       When I input "2013-01-01 12:12" in "datetime_test"
#       Then the value of "#id_datetime_test" is "2013-01-01 12:12"
#       Then I see "#id_datetime_test" is hidden
#       Then I see a visible placeholder for "#id_datetime_test"

    Scenario: Datetime validation
        Given I'm TestMan
        Given I open the datetime test page
        When I click on the placeholder for "#id_datetime_test"
        When I input "2013-99-99" in "#id_datetime_test"
        Then I see the following error: Enter a valid date/time.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_datetime_test"
        Then I see "#id_datetime_test" is visible

#   Scenario: Datetime with template filters
#       Given I'm TestMan
#       Given I open the datetime test page with options "?template_filters=date:'M d, Y H:i'"
#       Then the value of the placeholder for "#id_datetime_test" is "Jan 01, 2013 00:00"
#       When I click on the placeholder for "#id_datetime_test"
#       When I input "2013-05-01" in "#id_datetime_test"
#       Then the value of the placeholder for "#id_datetime_test" is "May 01, 2013 00:00"

    Scenario: Anonymous mode
        Given I open the datetime test page
        Then I don't see ".editlive"
