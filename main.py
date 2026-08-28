def show_products(products: list[dict[str, str | int]]) -> None:
    for product in products:
        print(
            f"{product['name']} — "
            f"{product['price']} руб. — "
            f"{product['stock']} шт."
        )


def product_search(products: list[dict[str, str | int]], name: str) -> dict[str, str | int]:
    for product in products:
        if product['name'] == name:
            return product


def main() -> None:
    products = [
    {"name": "Ноутбук", "price": 85000, "stock": 4},
    {"name": "Мышь", "price": 2500, "stock": 15},
    {"name": "Монитор", "price": 32000, "stock": 0},
    {"name": "Клавиатура", "price": 7000, "stock": 8},
]

    show_products(products)
    print(product_search(products, 'Мышь'))
  
    
if __name__ == "__main__":
   main()