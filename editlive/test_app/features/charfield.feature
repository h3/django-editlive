Feature: charField basic tests

    Scenario: Initial state
        Given I access the url "/editlive/test/charfield/"
        Then I see a field named "char_test" with the id "id_char_test"
        Then I see a editlive of type "charField" with the field id "id_char_test"


    Scenario: Placeholder test
        Given I access the url "/editlive/test/charfield/"
        Then I click on the placeholder next to "id_char_test" and see the input field appear

