Feature: PropertyFinder Countries

    Scenario Outline: Countries
        Given I load the website
        When I go to "/" page
        Then I see this country "<countries>"
        Examples:
            | countries           |
            | UAE                 |
            | QATAR               |
            | LEBANON             |
            | EGYPT               |
            | MOROCCO             |
            | BAHRAIN             |
            | KSA                 |
        And I click this country "<countries>"
        Examples:
            | countries           |
            | UAE                 |
            | QATAR               |
            | LEBANON             |
            | EGYPT               |
            | MOROCCO             |
            | BAHRAIN             |
            | KSA                 |