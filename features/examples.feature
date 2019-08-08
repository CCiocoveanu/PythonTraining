# new feature
# Tags: optional
    
Feature: A description
    
Scenario: Token generation
    Given System in healty
    When I get a token
    Then I get all the bookings

Scenario: Get specific booking
    Given System in healty
    When I get a token
    And I ask for booking 1
    Then I get details from booking 1



