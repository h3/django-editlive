Feature: Slug field tests
    Functional tests for the editlive Slug field

    Scenario: Slug Initial state
        Given I open the slug test page
        Then I see "input#id_slug_test[name='slug_test'][type='text'][maxlength='50']"
        Then I see a "charField" editlive for "#id_slug_test"
        Then I see "#id_slug_test" is hidden
        Then I see a visible placeholder for "#id_slug_test"

    Scenario: Slug Edit mode
        Given I open the slug test page
        When I click on the placeholder for "#id_slug_test"
        Then I see "#id_slug_test" is visible

    Scenario: Slug Edit and save
        Given I open the slug test page
        When I click on the placeholder for "#id_slug_test"
        Then I see "#id_slug_test" is visible
        When I input "Hello-World" in "#id_slug_test"
        Then the value of "#id_slug_test" is "Hello-World"
        Then I see "#id_slug_test" is hidden
        Then I see a visible placeholder for "#id_slug_test"
        Then I see the placeholder text change to "Hello-World"

    Scenario: Slug invalid
        Given I open the slug test page
        When I click on the placeholder for "#id_slug_test"
        When I input "invalid slug!" in "#id_slug_test"
        Then I see the following error: Enter a valid
