Feature: QR attendance check-in
  As a university instructor
  I want students to check in using a session QR code
  So that attendance is recorded accurately

  Scenario: Record attendance using a valid session QR code
    Given a student is enrolled in the course
    And the instructor has opened an attendance session
    When the student scans the valid QR code for that session
    Then the student is marked present for the session
