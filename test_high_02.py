import pytest
from plugin_manager import PluginManager

def test_plugin_priority():
    pm = PluginManager()

    result = []

    @pm.register_plugin(priority=5)
    def plugin_high_priority(data):
        result.append("high")
        return data

    @pm.register_plugin(priority=1)
    def plugin_highest_priority(data):
        result.append("highest")
        return data

    @pm.register_plugin(priority=10)
    def plugin_low_priority(data):
        result.append("low")
        return data

    pm.run_pipeline("test")

    assert result == ["highest", "high", "low"], "Плагины выполняются не в порядке приоритета"

def test_data_transformation():
    pm = PluginManager()

    @pm.register_plugin(priority=5)
    def to_upper(data):
        return data.upper()

    @pm.register_plugin(priority=10)
    def add_exclamation(data):
        return data + "!"

    result = pm.run_pipeline("hello")

    assert result == "HELLO!", "Трансформация данных работает некорректно"

def test_fault_tolerance():
    pm = PluginManager()

    result = []

    @pm.register_plugin(priority=5)
    def working_plugin_1(data):
        result.append("before")
        return "intermediate"

    @pm.register_plugin(priority=7)
    def failing_plugin(data):
        result.append("fail")
        raise ValueError("Плагин сломался")

    @pm.register_plugin(priority=10)
    def working_plugin_2(data):
        result.append("after")
        return data + "_final"

    final_result = pm.run_pipeline("start")

    assert "before" in result
    assert "fail" in result
    assert "after" in result
    assert final_result == "intermediate_final", "Пайплайн не продолжился после ошибки"