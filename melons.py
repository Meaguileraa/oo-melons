"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, tax, order_type):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)
        #what's in the parenthesis on line 30 comes from line 5
        #based on what is in the super class "AbstractMelonOrder"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international" 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
