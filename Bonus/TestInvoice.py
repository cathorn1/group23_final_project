import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 37.5


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTax(invoice, products):
    invoice.calculateTax(products, 0.2)

    assert invoice.calculateTax(products, 0.2) == 0.06


def test_CanCalculatetotalPurePrice(products):
    invoice = Invoice()
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 31.88


def test_CanCalculatetotalPrice(products):
    invoice = Invoice()
    invoice.totalPrice(products)
    print(invoice.totalPrice(products))

    assert invoice.totalPrice( products) == 31.939999999999998


class Invoice:
    def __init__(self):
        self.items = {}

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
            total_impure_price = round(total_impure_price, 2)
            return total_impure_price

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def calculateTax(self, products, taxPercentage):
        total_sales_price = 0
        total_sales_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        total_sales_tax = total_sales_price * (taxPercentage / 100)
        total_sales_tax = round(total_sales_tax, 2)
        return total_sales_tax

    def totalPrice(self, products):
        total_price = self.totalImpurePrice(products) - self.totalDiscount(products) + self.calculateTax(products, 0.2)

        return total_price