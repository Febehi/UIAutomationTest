@allure.label.epic:Products CRUD
Feature: Products CRUD


@allure.label.story:SuccessScenario
@AddProduct_OK
  Scenario Outline: Add Product Functionality
    Given I am on the Dashboard interface
    When I click on the Add Product Button
    Then I received Add Product Form
    And I enter a product "<product>"
    And I enter a description "<description>"
    And I enter a price "<price>"
    And I enter a discount "<discount>"
    And I click on the Add Product button
    Then Click on the OK button

    Examples:
      | product  | description     | price | discount |
      | P1       | It's a Product1 | 200   | 20       |


@allure.label.story:SuccessScenario
@cancelAddProduct_OK
   Scenario: Cancel Add Product Functionality
    Given I am on the Dashboard interface
    When I click on the Add Product Button
    Then I click on the cancel button    


@allure.label.story:SuccessScenario
@DeleteProduct_OK
  Scenario Outline: Delete Product Functionality
    Given I am on the Dashboard interface
    When I click on the Delete Button
    Then I should receive a success alert "<alert>"
    And check the product deletion
    Then Click on the OK button

    Examples:
      | alert          |
      | Product deleted|

@allure.label.story:SuccessScenario
@UpdateProduct_OK
  Scenario Outline: Update Product Functionality
    Given I am on the Dashboard interface
    When I click on the Edit Button
    Then I received Edit Product Form
    And I enter a product "<product>"
    And I enter a description "<description>"
    And I enter a price "<price>"
    And I enter a discount "<discount>"
    And I click on the Edit Product button
    Then Click on the OK button

    Examples:
      | product  | description     | price | discount |
      | P1       | It's a Product1 | 200   | 20       |


@allure.label.story:SuccessScenario
@cancelUpdateProduct_OK
   Scenario: Cancel Update Product Functionality
    Given I am on the Dashboard interface
    When I click on the Edit Button
    Then I click on the cancel button    
