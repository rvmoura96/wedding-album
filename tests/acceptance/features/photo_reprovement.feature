Feature: Photo reprovement
  Background: Super user registred and logged
    Given an engaged data
      | first_name | last_name | email              |
      | Aang       | Airs      | aang.airs@mail.com |
    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    When the user fill the login form with "correct" credentials
    Given the user access the photo submission page
    When the user try submmit a "photo"
    When the user access logout page


  Scenario: Reprove a photo
    When an enaged login
    And an engaged access the photo approvement page
    And an engaged click on "repprove"
    Then the total of photos should be "0"
