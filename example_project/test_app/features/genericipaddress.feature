Feature: GenericIPAddress field
    Functional tests for the editlive GenericIPAddress field

    Scenario: GenericIPAddress initial state
        Given I open the genericipaddress test page
        Then I see "input#id_genericipaddress_test[name='genericipaddress_test'][type='text']"
        Then I see a "charField" editlive for "#id_genericipaddress_test"
        Then I see "#id_genericipaddress_test" is hidden
        Then I see a visible placeholder for "#id_genericipaddress_test"

    Scenario: GenericIPAddress edit mode
        Given I open the genericipaddress test page
        When I click on the placeholder for "#id_genericipaddress_test"
        Then I see "#id_genericipaddress_test" is visible

    Scenario: GenericIPAddress edit and save
        Given I open the genericipaddress test page
        When I click on the placeholder for "#id_genericipaddress_test"
        Then I see "#id_genericipaddress_test" is visible
        When I input "192.168.0.1" in "#id_genericipaddress_test"
        Then the value of "#id_genericipaddress_test" is "192.168.0.1"
        Then I see "#id_genericipaddress_test" is hidden
        Then I see a visible placeholder for "#id_genericipaddress_test"
        Then I see the placeholder text change to "192.168.0.1"

    Scenario: GenericIPAddress validation
        Given I open the genericipaddress test page
        When I click on the placeholder for "#id_genericipaddress_test"
        When I input "blah blah" in "#id_genericipaddress_test"
        Then I see the following error: Enter a valid IPv4 or IPv6 address.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_genericipaddress_test"
        Then I see "#id_genericipaddress_test" is visible
