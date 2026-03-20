class SchemaValidator:
    def __init__(self, schema: dict):
        self.schema = schema
        self._errors = []

    def validate(self, data: dict) -> bool:
        self._errors.clear()
        return self._validate_schema(data, self.schema)

    def get_errors(self) -> list:
        return self._errors.copy()

    def _validate_schema(self, data, schema) -> bool:
        if not isinstance(data, dict):
            self._errors.append("Data must be a dictionary.")
            return False

        required_fields = schema.get("required", [])
        for field in required_fields:
            if field not in data:
                self._errors.append(f"Field '{field}' is required but missing.")

        for field, field_schema in schema.get("properties", {}).items():
            if field in data:
                if not self._validate_field(data[field], field_schema):
                    self._errors.append(f"Field '{field}' has invalid type.")
            elif field not in required_fields:
                continue

        return len(self._errors) == 0

    def _validate_field(self, value, field_schema) -> bool:
        expected_type = field_schema.get("type")
        if not expected_type:
            return True  

        type_map = {
            "string": str,
            "number": (int, float),
            "boolean": bool,
            "object": dict,
            "array": list
        }

        expected_python_type = type_map.get(expected_type)
        if expected_python_type is None:
            return True  

        if not isinstance(value, expected_python_type):
            return False
            
        if expected_type == "object" and "properties" in field_schema:
            return self._validate_schema(value, field_schema)
            
        if expected_type == "array" and "items" in field_schema:
            items_schema = field_schema["items"]
            return all(self._validate_field(item, items_schema) for item in value)
            
        return True