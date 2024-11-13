class Property:
    def __init__(self, address: str, rent:float, value: float, tax_rate: float, loan_total: float):

        self.address = address
        self.rent = rent
        self.value = value
        self.tax_rate = tax_rate
        self.loan_total = loan_total
    
    def calculate_annual_noi(self) -> float:
        annual_property_tax = self.calculate_property_tax()
        return (self.rent*12) - annual_property_tax

    def calculate_property_tax(self) -> float:
        return self.value*(self.tax_rate/100)


class Portfolio:
    def __init__(self) -> None:
        self.properties = []

    def add_property(self, property: Property):
        self.properties.append(property)
    
    def calculate_total_noi(self) -> float:
        total_noi = sum(p.calculate_annual_noi() for p in self.properties)
        print(f"Total NOI for the portfolio: ${total_noi}")
        return total_noi
    
class TreeNode:
    def __init__(self, property: Property):
        self.property = property
        self.left = None
        self.right = None
    

class PropertyBST:
    def __init__(self):
        self.root = None
    
    def insert(self, property: Property):
        if self.root is None:
            return TreeNode(property)
        self._insert_recursive(self.root, property)

    def _insert_recursive(self, node: TreeNode, property: Property):
        if property.value < node.property.value:
            if node.left is None:
                node.left = TreeNode(property)
            else:
                self._insert_recursive(node.left, property)
        else:
            if node.right is NOne:
                node.right = TreeNode(property)
            else:
                self._insert_recursive(node.right, property)
    
# Creating Property instances
property_1 = Property(address="10322 Urban Oak Trail, Houston, TX", rent=2065, value=272300, tax_rate=2.19, loan_total=160000)
property_2 = Property(address="9619 Blue Water Hyssop, Conroe, TX", rent=2065, value=361000, tax_rate=2.19, loan_total=0)
property_3 = Property(address="8125 Loma Terrace Rd, El Paso, TX", rent=1250, value=183700, tax_rate=2, loan_total=0)

#Creating Portfolio instance
portfolio = Portfolio()
portfolio.add_property(property_1)
portfolio.add_property(property_2)
portfolio.add_property(property_3)
portfolio.calculate_total_noi()
