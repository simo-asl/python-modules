from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional


class DataPro(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataPro):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, bool) and isinstance(data, (int, float)):
            return True
        elif isinstance(data, list) and len(data) > 0:
            return all(not isinstance(item, bool)
                       and isinstance(item, (float, int))
                       for item in data)
        else:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("The Data Not Valid\n")
        else:
            if isinstance(data, (int, float)):
                numeric_values = [data]
            else:
                numeric_values = data
            total_sum = sum(numeric_values)
            total_count = len(numeric_values)
            output = (f"Processed {total_count} numeric values, sum="
                      f"{total_sum}, avg={total_sum / total_count}\n")
            return output

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataPro):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("The Data Not Valid\n")
        word_tokens = data.split()
        word_count = len(word_tokens)
        char_count = len(data)

        return f"Processed text: {char_count} characters, {word_count} words\n"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataPro):
    def __init__(self) -> None:
        super().__init__()
        self._log_level_mappings = {'info': 'INFO', 'error': 'ALERT'}

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            parts = data.split(":")
            return len(parts) == 2 and all(part != "" for part in parts)
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("The Data Not Valid\n")
        else:
            error_type, message = data.split(':', 1)
            tag = self._log_level_mappings.get(
                error_type.lower(), error_type.upper())
            output = f"[{tag}] {error_type.upper()} level detected:{message}\n"
            return output

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def run_processing_suite() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    processor_instances = [
        (NumericProcessor(), [1, 2, 3, 4, 5], "Numeric"),
        (TextProcessor(), "Hello Nexus World", "Text"),
        (LogProcessor(), "Error: Connection timeout", "Log entry")
    ]
    names = ["Numeric", "Text", "Log"]
    index = 0

    for processor, test_data, data_type in processor_instances:
        try:
            print(f"Initializing {names[index]} Processor...")
            print(f'Processing data: "{test_data}"')
            result = processor.process(test_data)
            print(f"Validation: {data_type} data verified")
            print(processor.format_output(result))
            index += 1
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processor_list: List[DataPro] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    test_dataset: Dict = {
        0: [1, 2, 3],
        1: "word wordddd ",
        2: "INFO: System ready"
    }
    for index, processor in enumerate(processor_list):
        try:
            result = processor.process(test_dataset[index])
            print(f"Result: {index + 1} {result}", end="")
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == '__main__':
    run_processing_suite()
