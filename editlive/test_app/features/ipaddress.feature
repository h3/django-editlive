Feature: IPAddress field
    Functional tests for the editlive IPAddress field

    Scenario: Initial state
        Given I access the url "/editlive/test/ipaddress/"
        Then I see "input#id_ipaddress_test[name='ipaddress_test'][type='text']"
        Then I see a "charField" editlive for "#id_ipaddress_test"
        Then I see "#id_ipaddress_test" is hidden
        Then I see a visible placeholder for "#id_ipaddress_test"

    Scenario: Edit mode
        Given I access the url "/editlive/test/ipaddress/"
        When I click on the placeholder for "#id_ipaddress_test"
        Then I see "#id_ipaddress_test" is visible
