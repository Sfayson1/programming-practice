"""
TDD Practice Project

TDD Cycle:
1. RED    - Write a test for behavior that does not exist yet.
2. GREEN  - Write the minimum production code needed to pass the test.
3. REFACTOR - Improve the code while keeping all tests passing.

AAA Test Structure:
Arrange - Set up the test data and objects.
Act     - Perform the behavior being tested.
Assert  - Verify that the actual result matches the expected result.

Current concepts:
- Unit testing
- Test-Driven Development (TDD)
- OOP
- Encapsulation
- Properties
- Inheritance
"""

import unittest
from package import Package, StandardPackage, ExpressPackage


# TestPackage inherits from unittest.TestCase.
# TestCase provides testing methods such as:
# self.assertEqual() and self.assertRaises().
class TestPackage(unittest.TestCase):
    def setUp(self):
        """
        setUp() is called before each test method runs.

        This is a good place to create objects that will be used
        in multiple tests.
        """
        self.order_id = '12345'
        self.tracking_number = 'PKG001'
        self.destination = 'Orlando'
        self.weight = 10

    def make_package(self, cls=Package, **overrides):
        args = {
            'order_id': self.order_id,
            'tracking_number': self.tracking_number,
            'destination': self.destination,
            'weight': self.weight
        }
        args.update(overrides)
        return cls(**args)

    def test_package_stores_tracking_number(self):
        """
        Tests that Package stores and returns the tracking number
        provided when the object is created.
        """

        # ARRANGE:
        # Set up the data needed for the test.
        expected_tracking_number = 'PKG777'

        # ACT:
        # Perform the behavior being tested by creating a Package.
        package = self.make_package(tracking_number=expected_tracking_number)

        # ASSERT:
        # Compare the actual result with the expected result.
        self.assertEqual(
            package.tracking_number,
            expected_tracking_number
        )

    def test_package_rejects_blank_tracking_number(self):
        """
        Tests that Package rejects a blank tracking number.

        A ValueError should be raised instead of allowing an
        invalid Package to be created.
        """
        for invalid in ['', ' ', '\t']:
            with self.subTest(tracking_number=invalid):
                with self.assertRaises(ValueError):
                    self.make_package(tracking_number=invalid)

    def test_tracking_number_cannot_be_changed_directly(self):
        """
        Tests the encapsulation of tracking_number.

        The tracking number can be read through the property,
        but it cannot be directly reassigned because the property
        does not have a setter.
        """

        # ARRANGE:
        # Create a valid Package first because object creation
        # itself is not the behavior being tested here.
        package = self.make_package()

        # ACT & ASSERT:
        # Attempting to assign a new value to the read-only
        # property should raise AttributeError.
        with self.assertRaises(AttributeError):
            package.tracking_number = "PKG999"

    def test_package_stores_weight(self):
        """
        Tests that Package stores the weight supplied
        when the object is created.
        """

        # ARRANGE
        expected_weight = 25

        # ACT
        package = self.make_package(weight=expected_weight)

        # ASSERT
        self.assertEqual(package.weight, expected_weight) 

    def test_standard_package_inherits_package_behavior(self):
        """
        Tests inheritance.

        StandardPackage does not currently define its own __init__
        or weight attribute. It receives this behavior from Package,
        its parent class.
        """

        # ACT:
        # StandardPackage can use Package's constructor because
        # StandardPackage inherits from Package.
        standard_package = self.make_package(cls=StandardPackage)

        # ASSERT:
        # weight was defined by Package, not StandardPackage.
        # Accessing it here demonstrates inherited behavior.
        self.assertEqual(standard_package.weight, self.weight)
        self.assertIsInstance(standard_package, Package)

    def test_standard_package_calculates_shipping_cost(self):
        #arrange
        weight = 10
        base_cost = 5
        cost_per_lb = 1.50
        expected_cost = base_cost + (weight * cost_per_lb)
        package = self.make_package(cls=StandardPackage, weight=weight)
        
        #act
        actual_cost = package.calculate_shipping()

        #assert 
        self.assertAlmostEqual(actual_cost, expected_cost, places=2)

    def test_package_rejects_non_string_tracking_number(self):
        """
        Tests that Package rejects a non-string tracking number.

        A TypeError should be raised instead of allowing an
        invalid Package to be created.
        """
        for invalid in [None, 123, 45.67, ['PKG001'], {'id': 'PKG001'}]:
            with self.subTest(tracking_number=invalid):
                with self.assertRaises(TypeError):
                    self.make_package(tracking_number=invalid)

    def test_express_package_calculates_shipping_cost(self):
        """
        Tests that ExpressPackage calculates shipping cost correctly.

        The cost is based on the weight of the package and an additional
        express fee.
        """
        # Arrange
        weight = 10
        base_cost = 10
        express_fee = 15
        cost_per_lb = 2.50
        expected_cost = base_cost + (weight * cost_per_lb) + express_fee
        package = self.make_package(cls=ExpressPackage, weight=weight)

        # Act
        actual_cost = package.calculate_shipping()

        # Assert
        self.assertAlmostEqual(actual_cost, expected_cost, places=2)

if __name__ == "__main__":
    # Run the tests when this file is executed directly with:
    # python test_package.py
    unittest.main()