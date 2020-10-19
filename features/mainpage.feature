Feature: PropertyFinder Countries

    Scenario Outline: Countries
        Given I load the website
        When I go to "/" page
        Then I see this country "<countries>" with <order>
        Then I click this country "<countries>"
        Given  I close browser
        Examples:
            | countries           | order  |
            | UAE                 | 0      |
            | QATAR               | 1      |
            | LEBANON             | 2      |
            | EGYPT               | 3      |
            | MOROCCO             | 4      |
            | BAHRAIN             | 5      |
            | KSA                 | 6      |