class PluginManager:
    def __init__(self):
        self.plugins = []  
    def register_plugin(self, priority=10):
        """
        Декоратор для регистрации плагинов.
        Сортирует плагины по приоритету (меньше число = выше приоритет).
        """
        def decorator(func):
            self.plugins.append((func, priority))
            self.plugins.sort(key=lambda x: x[1])
            return func
        return decorator

    def run_pipeline(self, data):
        """
        Последовательно передает данные через все зарегистрированные плагины.
        Если плагин вызывает ошибку, она выводится в консоль, но выполнение продолжается.
        """
        result = data
        for plugin_func, priority in self.plugins:
            try:
                result = plugin_func(result)
            except Exception as e:
                print(f"Ошибка при выполнении плагина {plugin_func.__name__} (priority={priority}): {e}")
        return result