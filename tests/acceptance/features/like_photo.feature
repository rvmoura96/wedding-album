@skip
Feature: Like photo
  Background: Super user registred and logged
    Given an engaged data
      | first_name | last_name | email              |
      | Aang       | Airs      | aang.airs@mail.com |
    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    And the user fill the login form with "correct" credentials
    Given the user access the photo submission page
    When the user try submmit a "photo"
    And the user access logout page
    And an enaged login
    And an engaged access the photo approvement page
    And an engaged click on "approve"
    And the user access logout page
    And the user fill the login form with "correct" credentials


  Scenario: Like a not liked yet photo
    When a user access the timeline
    And the user click on "like"
    Then the photo total likes should be "1"

  Scenario: Like a not liked yet photo
    When a user access the timeline
    And the user click on "like"
    And the user click on "like"
    Then the photo total likes should be "0"
