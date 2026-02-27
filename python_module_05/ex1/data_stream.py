from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_identifier: str) -> None:
        self.stream_identifier = stream_identifier
        self._analytics = {}

    @abstractmethod
    def process_batch(self, batch_data: List[Any]) -> str:
        pass

    def filter_data(self, batch_data: List[Any],
                    filter_criteria: Optional[str] = None) -> List[Any]:
        return batch_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self._analytics


class SensorStream(DataStream):
    MONITORED_FIELDS = ['temp', 'humidity', 'pressure']
    high_val = 100

    def __init__(self, stream_identifier: str) -> None:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_identifier}, Type: Environmental Data")
        super().__init__(stream_identifier)

    def filter_data(self, batch_data: List[Any],
                    filter_criteria: Optional[str] = None) -> List[Any]:
        if filter_criteria == "high":
            return [
                reading for reading in batch_data
                if (any(reading.get(field) is not None
                        and reading.get(field) > self.high_val
                        for field in self.MONITORED_FIELDS))
            ]
        return batch_data

    def process_batch(self, batch_data: List[Any]) -> str:
        if not isinstance(batch_data, list) or len(batch_data) == 0:
            raise ValueError("Data Should Be No Empty List")

        temperature_values = []
        total_readings = 0
        for entry in batch_data:
            if not (isinstance(entry, dict) and len(entry.keys()) == 1):
                raise ValueError("Dict Required And Only One Key Allowed")

            field_name, field_value = next(iter(entry.items()))

            if (not isinstance(field_name, str) or field_name
                    not in self.MONITORED_FIELDS):
                raise ValueError("Key is Invalid")

            if (isinstance(field_value, bool)
                    or not isinstance(field_value, (float, int))):
                raise ValueError("Value Should Be Number")

            if field_name == 'temp':
                temperature_values.append(field_value)
                if field_value > self.high_val:
                    print(f"Extreme Value For Temp is [{self.high_val}]")
            total_readings += 1
        self._analytics.update({
            'avg_temp': sum(temperature_values) / len(temperature_values) if
            len(temperature_values) > 0 else 0,
            'readings': total_readings
        })
        return f"Sensor analysis: {self._analytics['readings']} readings" +\
               "processed"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self._analytics


class TransactionStream(DataStream):
    VALID_OPERATIONS = ['buy', 'sell']

    def __init__(self, stream_identifier: str) -> None:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_identifier}, Type: Financial Data")
        super().__init__(stream_identifier)

    def _accumulate_transaction(
            self, operation_type: str, amount: float) -> None:
        """Helper method to accumulate transaction amounts."""
        if operation_type in self._analytics:
            self._analytics[operation_type] += amount
        else:
            self._analytics[operation_type] = amount

    def process_batch(self, batch_data: List[Any]) -> str:
        if not isinstance(batch_data, list) or len(batch_data) == 0:
            raise ValueError("Data is Invalid")

        total_operations = 0
        for entry in batch_data:
            if not (isinstance(entry, dict) and len(entry.keys()) == 1):
                raise ValueError("Data is Invalid")
            operation_type, transaction_amount = next(iter(entry.items()))
            operation_type = operation_type.lower()

            if (not isinstance(operation_type, str) or operation_type
                not in self.VALID_OPERATIONS
                    or isinstance(transaction_amount, bool)
                    or not isinstance(transaction_amount, (int, float))):
                raise ValueError("Data is Invalid")

            self._accumulate_transaction(operation_type, transaction_amount)
            total_operations += 1

        self._analytics.update({'operations': total_operations})
        buy_total = self._analytics.get('buy', 0)
        sell_total = self._analytics.get('sell', 0)
        self._analytics.update({"net_flow": buy_total - sell_total})
        return f"Transaction analysis: {self._analytics.get('operations')} " +\
            "operations"

    def filter_data(self, batch_data: List[Any],
                    filter_criteria: Optional[str] = None) -> List[Any]:
        if filter_criteria == "high":
            return [
                entry for entry in batch_data
                if any(entry.get(op) is not None and entry.get(op) > 100
                       for op in self.VALID_OPERATIONS)
            ]
        return batch_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self._analytics


class EventStream(DataStream):
    ERROR_EVENT_KEYWORD = 'error'

    def __init__(self, stream_identifier: str) -> None:
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_identifier}, Type: System Events")
        super().__init__(stream_identifier)

    def process_batch(self, batch_data: List[Any]) -> str:
        if not isinstance(batch_data, list):
            raise ValueError("Data is Invalid")

        processed_events = 0
        for event_entry in batch_data:
            if (not (isinstance(event_entry, str)
                     and event_entry and event_entry != '\0')):
                raise ValueError("Data is Invalid")
            if event_entry.lower() == self.ERROR_EVENT_KEYWORD:
                self._analytics['error_count'] = self._analytics.get(
                    'error_count', 0) + 1

            processed_events += 1
        if 'error_count' not in self._analytics:
            self._analytics.update({'error_count': 0})
        return f"Event analysis: {len(batch_data)} events"

    def filter_data(self, batch_data: List[Any],
                    filter_criteria: Optional[str] = None) -> List[Any]:
        if filter_criteria == 'high':
            return [
                event for event in batch_data
                if event.lower() == self.ERROR_EVENT_KEYWORD
            ]
        return batch_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self._analytics


class StreamProcessor():
    STREAM_TYPE_STATS = {
        'SensorStream': 'readings',
        'TransactionStream': 'operations',
        'EventStream': 'error_count'
    }
    STREAM_OUTPUT_TEMPLATES = {
        'SensorStream': "- Sensor data: {} readings processed",
        'TransactionStream': "- Transaction data: {} operations processed",
        'EventStream': "- Event data: {} events processed"
    }
    STREAM_RESULT_KEYS = {
        'SensorStream': 'sensor_count',
        'TransactionStream': 'transaction_count',
        'EventStream': 'events_count'
    }

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream_instance: DataStream) -> None:
        self.streams.append(stream_instance)

    def process_streams(self, batch_data: Any) -> None:
        for index, stream_instance in enumerate(self.streams):
            analytics = stream_instance.get_stats()
            stream_instance.process_batch(batch_data[index])

            stream_type = stream_instance.__class__.__name__
            if stream_type in self.STREAM_TYPE_STATS:
                stat_key = self.STREAM_TYPE_STATS[stream_type]
                stat_value = analytics.get(stat_key)
                output_template = self.STREAM_OUTPUT_TEMPLATES[stream_type]
                print(output_template.format(stat_value))

    def filter_streams(self, batch_data: Any) -> Dict[str, int]:
        result = {key: 0 for key in self.STREAM_RESULT_KEYS.values()}

        for idx, stream_instance in enumerate(self.streams):
            stream_type = stream_instance.__class__.__name__
            if stream_type in self.STREAM_RESULT_KEYS:
                result_key = self.STREAM_RESULT_KEYS[stream_type]
                filtered_count = len(stream_instance.filter_data(
                    batch_data[idx], 'high'))
                result[result_key] = filtered_count

        return result


def run_stream_analysis() -> None:
    stream_test_configs = [
        (SensorStream('SENSOR_001'), [{"temp": 24.5}, {"humidity": 55},
                                      {'pressure': 1012}], 'sensor'),
        (TransactionStream('TRANS_001'), [{'buy': 300}, {'sell': 120},
                                          {'buy': 70}], 'transaction'),
        (EventStream('EVENT_001'), ['logged', 'error', 'info'], 'event')
    ]
    stream_instances = []

    for stream_obj, test_dataset, stream_label in stream_test_configs:
        try:
            print(f"Processing {stream_label} batch: {test_dataset}")
            analysis_result = stream_obj.process_batch(test_dataset)
            stream_stats = stream_obj.get_stats()

            if stream_label == 'sensor':
                print(
                      f"{analysis_result}, "
                      f"avg temp: {stream_stats.get('avg_temp')}°C\n"
                      )
            elif stream_label == 'transaction':
                net_val = stream_stats.get('net_flow')
                sign = '+' if net_val > 0 else ''
                print(f"{analysis_result}, net flow: {sign}{net_val} units\n")
            elif stream_label == 'event':
                print(f"{analysis_result}, "
                      f"{stream_stats.get('error_count')} error dectected\n")

            stream_instances.append(stream_obj)
        except Exception as e:
            print(f"Type: {e.__class__.__name__}, {e}")
            return None

    try:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        combined_batch_data = [
            [{'temp': 120}, {"humidity": 45}, {'pressure': 98}],
            [{'buy': 80}, {'sell': 150}, {'buy': 40}],
            ['login', 'error', 'logout']
        ]
        integrated_processor = StreamProcessor()
        for stream in stream_instances:
            integrated_processor.add_stream(stream)

        print("Batch 1 Results:")
        integrated_processor.process_streams(combined_batch_data)
        print("\nStream filtering active: High-priority data only")
        filter_result = integrated_processor.filter_streams(
            combined_batch_data)
        print(f"Filtered results: "
              f"{filter_result.get('sensor_count')} ", end="")
        print(f"critical sensor alerts,"
              f"{filter_result.get('transaction_count')} large transaction\n"
              )
        print("All streams processed successfully. Nexus throughput optimal.")
    except Exception as e:
        print(f"Type: {e.__class__.__name__}, {e}")


if __name__ == '__main__':
    run_stream_analysis()
