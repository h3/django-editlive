Feature: Smallsmallinteger field
    Functional tests for the editlive Smallsmallinteger field

    Scenario: Initial state
        Given I access the url "/test/smallinteger/"
        Then I see "input#id_smallinteger_test[name='smallinteger_test'][type='text']"
        Then I see a "charField" editlive for "#id_smallinteger_test"
        Then I see "#id_smallinteger_test" is hidden
        Then I see a visible placeholder for "#id_smallinteger_test"

    Scenario: Edit mode
        Given I access the url "/test/smallinteger/"
        When I click on the placeholder for "#id_smallinteger_test"
        Then I see "#id_smallinteger_test" is visible
