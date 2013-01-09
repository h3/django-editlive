Feature: Integer field
    Functional tests for the editlive Integer field

    Scenario: Integer initial state
        Given I'm TestMan
        Given I open the integer test page
        Then I see "input#id_integer_test[name='integer_test'][type='text']"
        Then I see a "charField" editlive for "#id_integer_test"
        Then I see "#id_integer_test" is hidden
        Then I see a visible placeholder for "#id_integer_test"

    Scenario: Integer edit mode
        Given I'm TestMan
        Given I open the integer test page
        When I click on the placeholder for "#id_integer_test"
        Then I see "#id_integer_test" is visible

    Scenario: Integer edit and save
        Given I'm TestMan
        Given I open the integer test page
        When I click on the placeholder for "#id_integer_test"
        Then I see "#id_integer_test" is visible
        When I input "1" in "#id_integer_test"
        Then the value of "#id_integer_test" is "1"
        Then I see "#id_integer_test" is hidden
        Then I see a visible placeholder for "#id_integer_test"
        Then I see the placeholder text change to "1"

    Scenario: Integer validation
        Given I'm TestMan
        Given I open the integer test page
        When I click on the placeholder for "#id_integer_test"
        When I input "a" in "#id_integer_test"
        Then I see the following error: Enter a whole number.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_integer_test"
        Then I see "#id_integer_test" is visible

    Scenario: Anonymous mode
        Given I open the char test page
        Then I don't see ".editlive"
