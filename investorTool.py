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

    def total_value(self) -> float:
        total_val = 0
        for i in range(len(self.properties)):
            total_val += self.properties.value[i] 
        return total_val

    def average_value(self) -> float:
        average_val = 0
        for i in range(len(self.properties)):
            average_val += self.properties[i].value
        return average_val/len(self.properties)
    
    def median_value(self) -> float:
        mediann_val = 0
        for i in range(len(self.properties)):

    def highest_value(self) -> Property:
        # return property that is worth the most

    def lowest_value(self) -> Property:
        # return property that is worth the least

    def projected_value(self, years: int, growth_rate: float) -> dict:
        #calculate projected value in x years at y percent
    
    def calculate_dtv(self) -> float:
        # Debt-to-income ratio
            




    
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
            self.root = TreeNode(property)
        self._insert_recursive(self.root, property)

    def _insert_recursive(self, node: TreeNode, property: Property):
        if property.value < node.property.value:
            if node.left is None:
                node.left = TreeNode(property)
            else:
                self._insert_recursive(node.left, property)
        else:
            if node.right is None:
                node.right = TreeNode(property)
            else:
                self._insert_recursive(node.right, property)

    def search_value(self, value:float, node = None) -> Property:
        if node is None:
            return None
        if node.property.value == value:
            return property
        if node.property.value < value:
            return self.search_value(value, node.left)
        return self.search_value(value, node.right)

    def search_range(self, min_value: float, max_value: float, node = None) -> list:
        results = []
        if node is None:
            return []
        if min_value <= node.value <= max_value:
            results += self.search_range(min_value, max_value, node.left) 
            results.append(node.property)
            results += self.search_range(min_value,max_value,node.right)
        if node.value > max_value:
            results +=self.search_range(min_value, max_value, node.left)
        if node.value < min_value:
            results += self.search_range(min_value, max_value, node.right)
        return results


    
# Creating Property instances
property_1 = Property(address="10322 Urban Oak Trail, Houston, TX", rent=2065, value=272300, tax_rate=2.19, loan_total=160000)
property_2 = Property(address="9619 Blue Water Hyssop, Conroe, TX", rent=2065, value=361000, tax_rate=2.19, loan_total=0)
property_3 = Property(address="8125 Loma Terrace Rd, El Paso, TX", rent=1250, value=183700, tax_rate=2, loan_total=0)

# Creating Portfolio instance
portfolio = Portfolio()
portfolio.add_property(property_1)
portfolio.add_property(property_2)
portfolio.add_property(property_3)
portfolio.calculate_total_noi()

# Creating PropertyBST instance
portfolio_tree = PropertyBST()
portfolio_tree.insert(property_1)
portfolio_tree.insert(property_2)
portfolio_tree.insert(property_3)

