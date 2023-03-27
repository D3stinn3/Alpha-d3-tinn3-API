from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f"%(float(self.price) * 0.4)
    
    @property
    def context_breakdown(self):
        _context = self.context
        if _context.startswith("Grade"):
            return f"{_context} is a Grader"
        elif _context.startswith("Form"):
            return f"{_context} is a Junior Secondary"
        else:
            return f"{_context} is a Senior"
    
    def get_discount(self):
        the_discount = float(self.sale_price) * 0.2
        return the_discount
    
    def get_offer(self):
        the_overall_offer = float(self.price)
        
        if self.price > 1000:
            the_offer = the_overall_offer * 2
            return the_offer
        elif self.price > 10000:
            the_offer = the_overall_offer * 4
            return the_offer
        
        return the_overall_offer