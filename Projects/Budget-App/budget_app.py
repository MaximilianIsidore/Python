class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = sum(item["amount"] for item in self.ledger)
        return total

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            desc = item["description"][:23]
            items += f"{desc:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spends = []
    for category in categories:
        total_spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spends.append(total_spent)

    total = sum(spends)
    percentages = [(s / total) * 100 for s in spends]

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= level else "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_len = max(len(cat.name) for cat in categories)
    names = [cat.name for cat in categories]

    for i in range(max_name_len):
        chart += "     "
        for name in names:
            chart += (name[i] + "  ") if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")
