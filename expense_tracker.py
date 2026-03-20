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

    def get_total(self, category=None) -> float:
        """
        Возвращает общую сумму расходов. Если указана категория — только по ней.

        :param category: Категория для фильтрации (опционально)
        :return: Сумма расходов
        """
        if category:
            return sum(exp['amount'] for exp in self.expenses if exp['category'] == category)
        return sum(exp['amount'] for exp in self.expenses)

    def get_by_category(self) -> dict:
        """
        Возвращает словарь, где ключи — названия категорий, а значения — суммарные траты в них.

        :return: Словарь с категориями и суммами
        """
        category_totals = {}
        for exp in self.expenses:
            cat = exp['category']
            category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
        return category_totals
