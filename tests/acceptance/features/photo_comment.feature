Feature: Photo Approvement
  Background: Super user registred and logged
    Given an engaged data
      | first_name | last_name | email              |
      | Aang       | Airs      | aang.airs@mail.com |

    Given a guest data
      | first_name | last_name | email                 |
      | Sokka      | Waters    | sokka.waters@mail.com |

    When the user access the platform
    And click on sign up
    And the guest form is filled with guest data
    And the user fill the login form with "correct" credentials
    Given the user access the photo submission page
    When the user try submmit a "photo"
    And the user access logout page
    And an enaged login
    And an engaged access the photo approvement page
    And an engaged click on "approve"
    And the user access logout page
    And the user fill the login form with "correct" credentials


    Scenario: Comment a photo
     When a user acess a photo page
     And comment "AWESOME MEMORY"
     Then the photo should have "1" commentary
