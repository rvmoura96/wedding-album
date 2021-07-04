Feature: Timeline
  Background: User registered and logged
    Given a guest data
      | name  | last_name | email                 |
      | Sokka | Waters    | sokka.waters@mail.com |
    When the guest form is filled with guest data
    When the user fill the login form with "correct" credentials
    Given the user access the photo submission page
    When the user try submmit a "photo"
    #TODO: PHOTO APPROVEMENT STEP

    Scenario: Há fotos na Timeline
      When a user access the timeline
      Then the timeline should list all approved photos
