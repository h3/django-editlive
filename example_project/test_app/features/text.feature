Feature: Text field tests
    Functional tests for the editlive Text field

    Scenario: Text initial state
        Given I open the text test page
        Then I see "textarea#id_text_test[name='text_test']"
        Then I see a "textField" editlive for "#id_text_test"
        Then I see "#id_text_test" is hidden
        Then I see a visible placeholder for "#id_text_test"

    Scenario: Text edit mode
        Given I open the text test page
        When I click on the placeholder for "#id_text_test"
        Then I see "#id_text_test" is visible

    Scenario: Text edit and save
        Given I open the text test page
        When I click on the placeholder for "#id_text_test"
        Then I see "#id_text_test" is visible
        When I input "Hello World" in "#id_text_test"
        Then the value of "#id_text_test" is "Hello World"
        Then I see "#id_text_test" is hidden
        Then I see a visible placeholder for "#id_text_test"
        Then I see the placeholder text change to "Hello World"
