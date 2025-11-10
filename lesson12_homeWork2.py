class Product:
    """Клас, який описує товар."""
    def __init__(self, name, price, description, size):
        self.name = name
        self.price = price
        self.description = description
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size}) — {self.price} грн | {self.description}"


class Customer:
    """Клас, який описує покупця."""
    def __init__(self, last_name, first_name, middle_name, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, тел: {self.phone}"


class Order:
    """Клас, який описує замовлення."""
    def __init__(self, customer):
        self.customer = customer
        self.items = {}  # {Product: quantity}

    def add_product(self, product, quantity=1):
        """Додає товар до замовлення."""
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def total_price(self):
        """Підрахунок сумарної вартості замовлення."""
        return sum(product.price * qty for product, qty in self.items.items())

    def __str__(self):
        lines = [f"Замовлення для: {self.customer}", "\nТовари:"]
        for product, qty in self.items.items():
            lines.append(f" - {product.name} × {qty} = {product.price * qty} грн")
        lines.append(f"\nЗагальна сума: {self.total_price()} грн")
        return "\n".join(lines)


# --- Приклад використання ---
if __name__ == "__main__":
    # створимо товари
    laptop = Product("Ноутбук Lenovo", 35000, "Ігровий ноутбук з 16 ГБ ОЗУ", "15.6''")
    mouse = Product("Миша Logitech", 800, "Безпровідна миша", "10×6×4 см")

    # створимо покупця
    customer = Customer("Іваненко", "Олег", "Петрович", "+380501234567")

    # створимо замовлення
    order = Order(customer)
    order.add_product(laptop, 1)
    order.add_product(mouse, 2)

    # виведемо інформацію про замовлення
    print(order)
