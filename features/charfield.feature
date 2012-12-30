Feature: charField basic tests

    Scenario: Initial state
        Given I access the url "/editlive/functional/charfield/"
        Then I see a "charfield" editlive named "char_test" with the id "id_char_test"
