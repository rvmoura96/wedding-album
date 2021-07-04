Feature: Guests register

  Scenario: Adding a guest
    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    Then the guest should be registered

  Scenario: New account with an email is already registered
    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    And the guest form is filled with guest data
    Then the number of registred users should be "1"
