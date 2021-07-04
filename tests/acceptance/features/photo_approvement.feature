Feature: Photo Approvement
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


  Scenario: Approve a photo
    When an enageg login
    And an engaged access the photo approvement page
    And an engaged click on approve
    Then the approved photos number should be "1"

  @wip
  Scenario: Guest try to access photo approvement area
    When the user fill the login form with "correct" credentials
    When a guest try to access the photo approvement page
    Then the guest should be redirected to home page
