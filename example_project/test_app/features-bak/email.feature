Feature: Email field
    Functional tests for the editlive Email field

    Scenario: Initial state
        Given I access the url "/test/email/"
        Then I see "input#id_email_test[name='email_test'][type='text']"
        Then I see a "charField" editlive for "#id_email_test"
        Then I see "#id_email_test" is hidden
        Then I see a visible placeholder for "#id_email_test"

    Scenario: Edit mode
        Given I access the url "/test/email/"
        When I click on the placeholder for "#id_email_test"
        Then I see "#id_email_test" is visible
