Feature: Field tests
    Functional tests for the editlive Char field

    Scenario: Charfield Initial state
        Given I access the url "/test/char/"
        Then I see "input#id_char_test[name='char_test'][type='text'][maxlength='250']"
        Then the value of "#id_char_test" is "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        Then I see a "charField" editlive for "#id_char_test"
        Then I see "#id_char_test" is hidden
        Then I see a visible placeholder for "#id_char_test"

    Scenario: Charfield Edit mode
        Given I access the url "/test/char/"
        When I click on the placeholder for "#id_char_test"
        Then I see "#id_char_test" is visible

    Scenario: Charfield Edit and save
        Given I access the url "/test/char/"
        When I click on the placeholder for "#id_char_test"
        Then I see "#id_char_test" is visible
#       When I input "Hello World" in "#id_char_test"
#       Then the value of "#id_char_test" is "Hello World"

    Scenario: Slugfield Initial state
        Given I access the url "/test/slug/"
        Then I see "input#id_slug_test[name='slug_test'][type='text'][maxlength='50']"
        Then I see a "charField" editlive for "#id_slug_test"
        Then I see "#id_slug_test" is hidden
        Then I see a visible placeholder for "#id_slug_test"

    Scenario: Slugfield Edit mode
        Given I access the url "/test/slug/"
        When I click on the placeholder for "#id_slug_test"
        Then I see "#id_slug_test" is visible


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


#   Scenario: Date Initial state
#       Given I access the url "/test/date/"
#       Then I see "input#id_date_test[name='date_test'][type='text']"
#       Then I see a "dateField" editlive for "#id_date_test"
#       Then I see "#id_date_test" is hidden
#       Then I see a visible placeholder for "#id_date_test"

#   Scenario: Date Edit mode
#       Given I access the url "/test/date/"
#       When I click on the placeholder for "#id_date_test"
#       Then I see "#id_date_test" is visible


#   Scenario: Datetime Initial state
#       Given I access the url "/test/datetime/"
#       Then I see "input#id_datetime_test[name='datetime_test'][type='text']"
#       Then I see a "datetimeField" editlive for "#id_datetime_test"
#       Then I see "#id_datetime_test" is hidden
#       Then I see a visible placeholder for "#id_datetime_test"

#   Scenario: Datetime Edit mode
#       Given I access the url "/test/datetime/"
#       When I click on the placeholder for "#id_datetime_test"
#       Then I see "#id_datetime_test" is visible

