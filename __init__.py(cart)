import json
from cart import dao
from products import Product, get_product

class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data: dict) -> "Cart":
        """Factory method to create a Cart instance from a dictionary."""
        return cls(
            id=data.get('id', 0),
            username=data.get('username', ""),
            contents=data.get('contents', []),
            cost=data.get('cost', 0.0)
        )

def get_cart(username: str) -> list[Product]:
    """Fetches the cart items for a given username."""
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        contents = cart_detail.get('contents', '[]')  # Default to an empty JSON array
        try:
            product_ids = json.loads(contents)
            if not isinstance(product_ids, list):
                continue  # Ensure product_ids is a list
        except json.JSONDecodeError:
            continue  # Skip invalid JSON content

        for product_id in product_ids:
            product = get_product(product_id)
            if product:
                items.append(product)

    return items

def add_to_cart(username: str, product_id: int):
    """Adds a product to the user's cart."""
    if not username or product_id <= 0:
        raise ValueError("Invalid username or product_id")
    dao.add_to_cart(username, product_id)

def remove_from_cart(username: str, product_id: int):
    """Removes a product from the user's cart."""
    if not username or product_id <= 0:
        raise ValueError("Invalid username or product_id")
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    """Deletes the user's cart."""
    if not username:
        raise ValueError("Invalid username")
    dao.delete_cart(username)
