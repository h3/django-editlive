Feature: IPAddress field
    Functional tests for the editlive IPAddress field

    Scenario: Initial state
        Given I'm TestMan
        Given I open the ipaddress test page
        Then I see "input#id_ipaddress_test[name='ipaddress_test'][type='text']"
        Then I see a "charField" editlive for "#id_ipaddress_test"
        Then I see "#id_ipaddress_test" is hidden
        Then I see a visible placeholder for "#id_ipaddress_test"

    Scenario: Edit mode
        Given I'm TestMan
        Given I open the ipaddress test page
        When I click on the placeholder for "#id_ipaddress_test"
        Then I see "#id_ipaddress_test" is visible

    Scenario: IPAddress edit and save
        Given I'm TestMan
        Given I open the ipaddress test page
        When I click on the placeholder for "#id_ipaddress_test"
        Then I see "#id_ipaddress_test" is visible
        When I input "192.168.0.1" in "#id_ipaddress_test"
        Then the value of "#id_ipaddress_test" is "192.168.0.1"
        Then I see "#id_ipaddress_test" is hidden
        Then I see a visible placeholder for "#id_ipaddress_test"
        Then I see the placeholder text change to "192.168.0.1"

    Scenario: IPAddress invalid
        Given I'm TestMan
        Given I open the ipaddress test page
        When I click on the placeholder for "#id_ipaddress_test"
        When I input "blah blah" in "#id_ipaddress_test"
        Then I see the following error: Enter a valid IPv4 address.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_ipaddress_test"
        Then I see "#id_ipaddress_test" is visible

    Scenario: Anonymous mode
        Given I open the char test page
        Then I don't see ".editlive"
