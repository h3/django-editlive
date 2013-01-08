Feature: Email field
    Functional tests for the editlive Email field

    Scenario: Email Initial state
        Given I open the email test page
        Then I see "input#id_email_test[name='email_test'][type='text']"
        Then the value of "#id_email_test" is "admin@bofh.com"
        Then I see a "charField" editlive for "#id_email_test"
        Then I see "#id_email_test" is hidden
        Then I see a visible placeholder for "#id_email_test"

    Scenario: Email Edit mode
        Given I open the email test page
        When I click on the placeholder for "#id_email_test"
        Then I see "#id_email_test" is visible

    Scenario: Email Edit and save
        Given I open the email test page
        When I click on the placeholder for "#id_email_test"
        Then I see "#id_email_test" is visible
        When I input "Hello@World.com" in "#id_email_test"
        Then the value of "#id_email_test" is "Hello@World.com"
        Then I see "#id_email_test" is hidden
        Then I see a visible placeholder for "#id_email_test"
        Then I see the placeholder text change to "Hello@World.com"

    Scenario: Email validation
        Given I open the email test page
        When I click on the placeholder for "#id_email_test"
        When I input "blah blah" in "#id_email_test"
        Then I see the following error: Enter a valid e-mail address.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_email_test"
        Then I see "#id_email_test" is visible
