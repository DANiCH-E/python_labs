Feature: Test
    Scenario: Test Builder
      Given Furniture_Builder
      When test_shatura_builder return OK
      And test_lasurit_builder return OK
      Then Good job
