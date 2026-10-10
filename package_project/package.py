class Package:
    """
    Base class representing a package.

    This class stores information shared by all package types.
    Other package types, such as StandardPackage, can inherit
    these attributes and behaviors.
    """

    def __init__(self, order_id, tracking_number, destination, weight):
        # Validate the tracking number before storing it.

        #Tracking number cannot be blank or whitespace-only. It must be a non-empty string.

        if not isinstance(tracking_number, str):
            raise TypeError("Tracking number must be a string")

        # .strip() removes leading and trailing whitespace, so whitespace-only values become '', 
        # which is falsy and gets rejected.

        if not tracking_number.strip():
            raise ValueError("Tracking number cannot be blank")

        # Public attributes:
        # These can currently be read and changed directly.
        self.order_id = order_id
        self.destination = destination
        self.weight = weight

        # Encapsulation:
        # The leading underscore indicates that this attribute is
        # intended for internal use by the class.
        self._tracking_number = tracking_number

    @property
    def tracking_number(self):
        """
        Getter for the tracking number.

        @property allows outside code to read tracking_number
        like a normal attribute without directly accessing
        _tracking_number.
        """
        return self._tracking_number


# Inheritance:
# StandardPackage is a child/subclass of Package.
# Because it inherits from Package, it currently receives Package's
# constructor, attributes, validation, and properties.
class StandardPackage(Package):
    """
    A package that is shipped using standard shipping.

    It inherits construction and validation from Package and 
    adds its own behavior for calculating shipping cost.
    """
  
    def calculate_shipping(self):
        """
        Calculates the shipping cost for a package.

        The cost is based on the weight of the package.
        """

        # Calculate the shipping cost based on weight.
        # $5 base cost + $1.50 per pound.
        base_cost = 5
        cost_per_lb = 1.50
        return base_cost + (self.weight * cost_per_lb)
    
class ExpressPackage(Package):
    """
    A package that is shipped using express shipping.

    It inherits construction and validation from Package and 
    adds its own behavior for calculating shipping cost.
    """

    def calculate_shipping(self):
        """
        Calculates the shipping cost for an express package.

        The cost is based on the weight of the package and an additional
        express fee.
        """

        # Calculate the shipping cost based on weight and an express fee.
        base_cost = 10
        cost_per_lb = 2.50
        express_fee = 15
        return base_cost + (self.weight * cost_per_lb) + express_fee