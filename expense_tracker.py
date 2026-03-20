class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: float, category: str, description: str, date: str):
        """
        Добавляет новый расход в список.

        :param amount: Сумма расхода
        :param category: Категория расхода
        :param description: Описание расхода
        :param date: Дата в формате 'YYYY-MM-DD'
        """
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': date
        }
        self.expenses.append(expense)
