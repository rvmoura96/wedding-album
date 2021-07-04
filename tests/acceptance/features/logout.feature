Feature: Logout
  Background: User registered
    Given a guest data
      | name  | last_name | email                 |
      | Sokka | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    Given a user accessing the login page
    When the user fill the login form with "correct" credentials


  Scenario: Logout success
    When the user access logout page
    Then the user should be redirected to "login"
