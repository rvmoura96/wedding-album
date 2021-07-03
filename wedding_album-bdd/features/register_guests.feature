Feature: Guests register

  Scenario: Adding a guest
    Given a guest data
      | name  | last_name | email                 |
      | Sokka | Waters    | sokka.wsaters@mail.com |
    When the guests form is filled with guest data
    Then the user should be registered
