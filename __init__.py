from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict) -> "Product":
        """Factory method to create a Product instance from a dictionary."""
        return cls(
            id=data.get('id', 0),
            name=data.get('name', ""),
            description=data.get('description', ""),
            cost=data.get('cost', 0.0),
            qty=data.get('qty', 0)
        )

def list_products() -> list[Product]:
    """Fetches and returns a list of all products."""
    products = dao.list_products()
    return [Product.load(product) for product in products]

def get_product(product_id: int) -> Product:
    """Fetches and returns a product by its ID."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found")
    return Product.load(product_data)

def add_product(product: dict):
    """Adds a new product using a dictionary of product details."""
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product.keys()):
        raise ValueError(f"Product data must include {required_keys}")
    dao.add_product(product)

def update_qty(product_id: int, qty: int):
    """Updates the quantity of a specific product."""
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    if not dao.get_product(product_id):
        raise ValueError(f"Product with ID {product_id} not found")
    dao.update_qty(product_id, qty)
