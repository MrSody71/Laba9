import pytest
from datetime import datetime
from expense_tracker import ExpenseTracker

def test_category_filter():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "Еда", "Завтрак", "2025-03-01")
    tracker.add_expense(200, "Транспорт", "Автобус", "2025-03-02")
    tracker.add_expense(150, "Еда", "Обед", "2025-03-03")

    assert tracker.get_total("Еда") == 250
    assert tracker.get_total("Транспорт") == 200
    assert tracker.get_total("Одежда") == 0

def test_total_sum():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "Еда", "Завтрак", "2025-03-01")
    tracker.add_expense(200, "Транспорт", "Автобус", "2025-03-02")
    tracker.add_expense(50, "Еда", "Ужин", "2025-03-03")

    assert tracker.get_total() == 350

def test_date_range_filter():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "Еда", "Завтрак", "2025-03-01")
    tracker.add_expense(200, "Транспорт", "Автобус", "2025-03-02")
    tracker.add_expense(150, "Еда", "Обед", "2025-03-03")
    tracker.add_expense(300, "Одежда", "Куртка", "2025-03-04")

    result = tracker.get_by_date_range("2025-03-02", "2025-03-03")
    assert len(result) == 2
    assert result[0]['category'] == "Транспорт"
    assert result[1]['category'] == "Еда"

    result_all = tracker.get_by_date_range("2025-03-01", "2025-03-04")
    assert len(result_all) == 4

def test_top_categories_by_amount_not_count():
    tracker = ExpenseTracker()
    tracker.add_expense(50, "Еда", "Завтрак", "2025-03-01")
    tracker.add_expense(50, "Еда", "Обед", "2025-03-01")
    tracker.add_expense(50, "Еда", "Ужин", "2025-03-01")
    tracker.add_expense(100, "Одежда", "Куртка", "2025-03-02")
    tracker.add_expense(100, "Одежда", "Ботинки", "2025-03-02")
    tracker.add_expense(180, "Развлечения", "Концерт", "2025-03-03")

    top = tracker.get_top_categories(3)
    assert len(top) == 3
    assert top[0][0] == "Одежда"  
    assert top[1][0] == "Развлечения"  
    assert top[2][0] == "Еда"  

if __name__ == "__main__":
    pytest.main(["-v", "test_medium_05.py"])