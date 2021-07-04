Feature: Submit Photo
  Background: User registered and logged
    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    When the user fill the login form with "correct" credentials

  Scenario: With a valid photo
    Given the user access the photo submission page
    When the user try submmit a "photo"
    Then the number of photos to be approved should be "1"

  Scenario: With a invalid photo
    Given the user access the photo submission page
    When the user try submmit a "pdf"
    Then the number of photos to be approved should be "0"
