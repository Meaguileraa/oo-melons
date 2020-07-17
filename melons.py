"""Classes for melon orders."""

from random import randint 
#randint (includes 5 and 9) vs randrange (start stop step, doesnt include 9)

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, tax, order_type):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_base_price(self):
        """Change the base price to a random integer for splurge pricing"""

        base_price = randint(5, 9)
        
        return base_price 


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        #base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas melons":
            base_price = base_price * 1.5 
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3
        
            #international orders less than 10 get $3 added
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """Orders need to pass security inspection."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.0)
        self.passed_inspection = False #until a successful inspection occurs

    def mark_inspection(self, passed):
        self.passed_inspection = passed 


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)
        #based on what is in the super class "AbstractMelonOrder"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
