import unittest
from validator import SchemaValidator

class TestSchemaValidator(unittest.TestCase):
    
    def test_valid_data(self):
        """Полная проверка корректного словаря со всеми типами данных."""
        schema = {
            "type": "object",
            "required": ["name", "age", "is_active", "tags", "profile"],
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"},
                "is_active": {"type": "boolean"},
                "tags": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "profile": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "score": {"type": "number"}
                    }
                }
            }
        }
        
        data = {
            "name": "John",
            "age": 30,
            "is_active": True,
            "tags": ["developer", "python"],
            "profile": {
                "city": "Moscow",
                "score": 95.5
            }
        }
        
        validator = SchemaValidator(schema)
        self.assertTrue(validator.validate(data))
        self.assertEqual(validator.get_errors(), [])
    
    def test_missing_required(self):
        """Проверка ошибки, если поле из required отсутствует."""
        schema = {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"}
            }
        }
        
        data = {"age": 30}  # name отсутствует
        
        validator = SchemaValidator(schema)
        self.assertFalse(validator.validate(data))
        errors = validator.get_errors()
        self.assertIn("Field 'name' is required but missing.", errors)
    
    def test_invalid_types(self):
        """Проверка, что number не проходит там, где ожидается string."""
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"}
            }
        }
        
        data = {
            "name": 123,  # должно быть строкой
            "age": "thirty"  # должно быть числом
        }
        
        validator = SchemaValidator(schema)
        self.assertFalse(validator.validate(data))
        errors = validator.get_errors()
        self.assertIn("Field 'name' has invalid type.", errors)
        self.assertIn("Field 'age' has invalid type.", errors)
    
    def test_nested_validation(self):
        """Проверка вложенного объекта (например, профиль пользователя внутри объекта данных)."""
        schema = {
            "type": "object",
            "properties": {
                "profile": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "score": {"type": "number"}
                    }
                }
            }
        }
        
        # Корректные вложенные данные
        valid_data = {
            "profile": {
                "city": "London",
                "score": 88
            }
        }
        
        validator = SchemaValidator(schema)
        self.assertTrue(validator.validate(valid_data))
        
        # Некорректные вложенные данные (число вместо строки)
        invalid_data = {
            "profile": {
                "city": 123,
                "score": 88
            }
        }
        
        self.assertFalse(validator.validate(invalid_data))
        errors = validator.get_errors()
        self.assertIn("Field 'city' has invalid type.", errors)

if __name__ == "__main__":
    unittest.main()