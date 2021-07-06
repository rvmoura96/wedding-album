# Wedding Album challenge line of thought

The whole challenge was developed using BDD (Behaviour driven development) specially using the specification by example.

The first action taken was to break the challenge into micro challenges, using a few users stories to guide the development.

All specifications were made with a BDD framework, all scenarios and features created can be found on the path "tests/acceptance/features/" and can be read by anyone, no technical skills required.

It is written in scenarios format using a natural language (Gherkin), which describes actions a user could perform on an application and the expected behaviour for those actions.

The tests written are E2E(End-to-End) tests, this way the application was fully tested. These tests do not exclude the need of unit tests, but they can cover the most of cases. E2E tests could save you some time when developping a MVP to prove a hypothesis.

The backend was written using the web framework Django, which is used by Instagram, an application that looks like the challenge application.

All uploaded files are saved on AWS S3 as required in the challenge.


There are two kinds of users for the application the admin(the bride and engaged) and common users(guests), all photos sent by the users are sent to be approved by the admins before they become available for all users as required in the challenge.


There are some point to be improved on this solution:
 - The upload should send the photo to a queue system to check the file metadata to guarantee the file is  a real picture and reduce the photo size;
 - E2E need some refactor to apply the PageObject design pattern to improve the tests maintenance;
 - The frontend for the application should be developed in a proper framework and considering UX;
 - Django Rest Framework can be added to move some views to API calls;
 - Unit tests on application;
 - Add Docker and Docker-compose to improve environment setup;
