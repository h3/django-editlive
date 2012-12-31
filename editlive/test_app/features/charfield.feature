# Editlive charField tests

Feature: charField
    Functional tests for the editlive charField widget

    Scenario: Initial state
        Given I access the url "/editlive/test/charfield/"
        Then I see "input#id_char_test[name='char_test'][type='text'][maxlength='250']"
        Then I see a "charField" editlive for "#id_char_test"
        Then I see "#id_char_test" is hidden
        Then I see a visible placeholder for "#id_char_test"

    Scenario: Edit mode
        Given I access the url "/editlive/test/charfield/"
        When I click on the placeholder for "#id_char_test"
        Then I see "#id_char_test" is visible
