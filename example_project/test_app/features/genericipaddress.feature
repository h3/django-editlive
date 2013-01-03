Feature: GenericIPAddress field
    Functional tests for the editlive GenericIPAddress field

    Scenario: Initial state
        Given I access the url "/test/genericipaddress/"
        Then I see "input#id_genericipaddress_test[name='genericipaddress_test'][type='text']"
        Then I see a "charField" editlive for "#id_genericipaddress_test"
        Then I see "#id_genericipaddress_test" is hidden
        Then I see a visible placeholder for "#id_genericipaddress_test"

    Scenario: Edit mode
        Given I access the url "/test/genericipaddress/"
        When I click on the placeholder for "#id_genericipaddress_test"
        Then I see "#id_genericipaddress_test" is visible
