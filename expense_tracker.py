from datetime import datetime

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

    def get_by_date_range(self, start: str, end: str) -> list:
        """
        Возвращает список расходов за период (включая границы).

        :param start: Начальная дата в формате 'YYYY-MM-DD'
        :param end: Конечная дата в формате 'YYYY-MM-DD'
        :return: Список расходов в заданном диапазоне
        """
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')
        result = []
        for exp in self.expenses:
            exp_date = datetime.strptime(exp['date'], '%Y-%m-%d')
            if start_date <= exp_date <= end_date:
                result.append(exp)
        return result

    def get_top_categories(self, n=5) -> list:
        """
        Возвращает список из n самых затратных категорий (название, сумма), отсортированный по убыванию суммы.

        :param n: Количество возвращаемых категорий
        :return: Список кортежей (категория, сумма)
        """
        category_totals = self.get_by_category()
        sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
        return sorted_categories[:n]
