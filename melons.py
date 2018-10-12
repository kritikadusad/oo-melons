"""Classes for melon orders."""
class AbstractMelonOrder():

    def __init__(self, species, qty, country_code=None):
        """inintialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code


    def get_total(self):
        """calculate price with tax"""
        if self.species == 'Christmas':
            base_price = 5 * 1.5
        else:
            base_price = 5


        total = ((1 + self.tax) * base_price) + self.fee
       
        return total

    def set_shipped(self):
        """record when an order has shipped"""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    fee = 0
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17

    def set_fee(self):
        if self.qty < 10:
            self.fee = 3
        else:
            self.fee = 0    
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code




