Feature: Text field tests
    Functional tests for the editlive Text field

    Scenario: Text Initial state
        Given I access the url "/test/text/"
        Then I see "textarea#id_text_test[name='text_test']"
        Then I see a "textField" editlive for "#id_text_test"
        Then I see "#id_text_test" is hidden
        Then I see a visible placeholder for "#id_text_test"

    Scenario: Text Edit mode
        Given I access the url "/test/text/"
        When I click on the placeholder for "#id_text_test"
        Then I see "#id_text_test" is visible

