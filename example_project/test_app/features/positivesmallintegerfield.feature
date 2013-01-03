Feature: PositiveSmallpositivesmallinteger field
    Functional tests for the editlive PositiveSmallpositivesmallinteger field

    Scenario: Initial state
        Given I access the url "/test/positivesmallinteger/"
        Then I see "input#id_positivesmallinteger_test[name='positivesmallinteger_test'][type='text']"
        Then I see a "charField" editlive for "#id_positivesmallinteger_test"
        Then I see "#id_positivesmallinteger_test" is hidden
        Then I see a visible placeholder for "#id_positivesmallinteger_test"

    Scenario: Edit mode
        Given I access the url "/test/positivesmallinteger/"
        When I click on the placeholder for "#id_positivesmallinteger_test"
        Then I see "#id_positivesmallinteger_test" is visible
