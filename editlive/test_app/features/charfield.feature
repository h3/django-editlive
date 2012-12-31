# Editlive charField tests

Feature: charField
    Functional tests for the editlive charField widget

    Scenario: Initial state
        Given I access the url "/editlive/test/charfield/"
        Then I see a field named "char_test" with the id "id_char_test"
        Then I see a editlive of type "charField" for the field id "id_char_test"
        Then I see the HTML node with the id "id_char_test" is hidden
        Then I see the placeholder for the id "id_char_test" is visible
