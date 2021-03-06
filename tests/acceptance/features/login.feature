Feature: Login
  Background: User registered
    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |

    When the user access the platform
    And click on sign up
    And the guest form is filled with guest data

  Scenario: Correct credentials login
    Given a user accessing the login page
    When the user fill the login form with "correct" credentials
    Then the user should be redirected to "home"

  Scenario: Incorrect credentials login
    Given a user accessing the login page
    When the user fill the login form with "incorrect" credentials
    Then the user should be redirected to "login"
