Feature: Slug field
    Functional tests for the editlive Slug field

    Scenario: Initial state
        Given I access the url "/editlive/test/slug/"
        Then I see "input#id_slug_test[name='slug_test'][type='text'][maxlength='50']"
        Then I see a "charField" editlive for "#id_slug_test"
        Then I see "#id_slug_test" is hidden
        Then I see a visible placeholder for "#id_slug_test"

    Scenario: Edit mode
        Given I access the url "/editlive/test/slug/"
        When I click on the placeholder for "#id_slug_test"
        Then I see "#id_slug_test" is visible
