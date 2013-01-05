Feature: Char field tests
    Functional tests for the editlive Char field

    Scenario: Char Initial state
        Given I open the char test page
        Then I see "input#id_char_test[name='char_test'][type='text'][maxlength='250']"
        Then the value of "#id_char_test" is "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        Then I see a "charField" editlive for "#id_char_test"
        Then I see "#id_char_test" is hidden
        Then I see a visible placeholder for "#id_char_test"

    Scenario: Char Edit mode
        Given I open the char test page
        When I click on the placeholder for "#id_char_test"
        Then I see "#id_char_test" is visible

    Scenario: Char Edit and save
        Given I open the char test page
        When I click on the placeholder for "#id_char_test"
        Then I see "#id_char_test" is visible
        When I input "Hello World" in "#id_char_test"
        Then the value of "#id_char_test" is "Hello World"
        Then I see "#id_char_test" is hidden
        Then I see a visible placeholder for "#id_char_test"
        Then I see the placeholder text change to "Hello World"
