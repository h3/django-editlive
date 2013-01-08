Feature: SmallInteger field
    Functional tests for the editlive SmallInteger field

    Scenario: SmallInteger initial state
        Given I open the smallinteger test page
        Then I see "input#id_smallinteger_test[name='smallinteger_test'][type='text']"
        Then I see a "charField" editlive for "#id_smallinteger_test"
        Then I see "#id_smallinteger_test" is hidden
        Then I see a visible placeholder for "#id_smallinteger_test"

    Scenario: SmallInteger edit mode
        Given I open the smallinteger test page
        When I click on the placeholder for "#id_smallinteger_test"
        Then I see "#id_smallinteger_test" is visible

    Scenario: SmallInteger Edit and save
        Given I open the smallinteger test page
        When I click on the placeholder for "#id_smallinteger_test"
        Then I see "#id_smallinteger_test" is visible
        When I input "1" in "#id_smallinteger_test"
        Then the value of "#id_smallinteger_test" is "1"
        Then I see "#id_smallinteger_test" is hidden
        Then I see a visible placeholder for "#id_smallinteger_test"
        Then I see the placeholder text change to "1"

    Scenario: SmallInteger validation
        Given I open the smallinteger test page
        When I click on the placeholder for "#id_smallinteger_test"
        When I input "a" in "#id_smallinteger_test"
        Then I see the following error: Enter a whole number.
        When I click on "h1"
        Then I see a hidden placeholder for "#id_smallinteger_test"
        Then I see "#id_smallinteger_test" is visible
