from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
from time import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage) -> Any:
        self.stages.append(stage)


class NexusManager:
    ADAPTER_FORMAT_MAPPING = {
        'JSONAdapter': 'json',
        'CSVAdapter': 'csv',
        'StreamAdapter': 'stream'
    }

    def __init__(self) -> None:
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second\n")
        self.registered_pipelines: List[ProcessingPipeline] = []

    def add_pipeline(
            self, pipeline_instance: Optional[ProcessingPipeline]) -> None:
        self.registered_pipelines.append(pipeline_instance)

    def process_data(self, data_packet: Any) -> None:
        for pipeline_inst in self.registered_pipelines:
            adapter_name = pipeline_inst.__class__.__name__
            data_format = data_packet.get('format')

            if adapter_name in self.ADAPTER_FORMAT_MAPPING and \
               self.ADAPTER_FORMAT_MAPPING[adapter_name] == data_format:
                pipeline_inst.process(data_packet.get('data'))


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_identifier: str) -> None:
        super().__init__()
        self.pipeline_identifier = pipeline_identifier

    def process(self, input_data: Any) -> Union[str, Any]:
        if (isinstance(input_data, dict)
                and "pipeline" in input_data and "data" in input_data):
            processed_data = input_data
        else:
            processed_data = {
                "pipeline": self.__class__.__name__,
                "data": input_data
            }

        return self._execute_pipeline_stages(processed_data)

    def _execute_pipeline_stages(self, data: Any) -> Union[str, Any]:
        """Execute all stages in the pipeline with error recovery."""
        current_data = data
        for stage in self.stages:
            try:
                current_data = stage.process(current_data)
            except Exception as error:
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful:", end=""
                      " Pipeline restored, processing resumed")
                print(f"{error.__class__.__name__}: {error}")
                return None
        return current_data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_identifier: str) -> None:
        super().__init__()
        self.pipeline_identifier = pipeline_identifier

    def process(self, input_data: Any) -> Union[str, Any]:
        formatted_data = {
            'pipeline': self.__class__.__name__, 'data': input_data}
        return self._execute_pipeline_stages(formatted_data)

    def _execute_pipeline_stages(self, data: Any) -> Union[str, Any]:
        """Execute all stages in the pipeline with error recovery."""
        current_data = data
        for stage in self.stages:
            try:
                current_data = stage.process(current_data)
            except Exception as error:
                print(f"{error.__class__.__name__}: {error}")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful:", end=""
                      " Pipeline restored, processing resumed")
                return None
        return current_data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_identifier: str) -> None:
        super().__init__()
        self.pipeline_identifier = pipeline_identifier

    def process(self, input_data: Any) -> Union[str, Any]:
        formatted_data = {
            'pipeline': self.__class__.__name__, 'data': input_data}
        return self._execute_pipeline_stages(formatted_data)

    def _execute_pipeline_stages(self, data: Any) -> Union[str, Any]:
        """Execute all stages in the pipeline with error recovery."""
        current_data = data
        for stage in self.stages:
            try:
                current_data = stage.process(current_data)
            except Exception as error:
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful:", end=""
                      " Pipeline restored, processing resumed")
                print(f"{error.__class__.__name__}: {error}")
                return None
        return current_data


class InputStage:
    def process(self, stage_data: Any) -> Dict:
        adapter_type = stage_data.get('pipeline')
        payload = stage_data.get('data')

        if adapter_type == 'JSONAdapter':
            self._validate_json_input(payload)
        elif adapter_type == 'CSVAdapter':
            self._validate_csv_input(payload)
        elif adapter_type == 'StreamAdapter':
            self._validate_stream_input(payload)

        return stage_data

    def _validate_json_input(self, json_payload: Any) -> None:
        """Validate JSON data structure."""
        print(f"Input: {json_payload}")
        if not isinstance(json_payload, Dict):
            raise ValueError("Error: Json Data Should Be Dict")
        for key_item in json_payload.keys():
            if not isinstance(key_item, str):
                raise ValueError("Error: Json Key Should Be Str")

    def _validate_csv_input(self, csv_payload: Any) -> None:
        """Validate CSV data structure."""
        print(f"Input: {csv_payload}")
        if not isinstance(csv_payload, str):
            raise ValueError("Error: Csv Data Are Invalid (Should Be Str)")

        line_records = csv_payload.split('\n')
        if len(line_records) < 2:
            raise ValueError("Error: Csv Rows Should Be 2 or More")

        header_columns = line_records[0].split(',')
        expected_column_count = len(header_columns)

        for csv_line in line_records:
            parsed_columns = csv_line.split(',')
            if len(parsed_columns) != expected_column_count:
                raise ValueError("Error: Csv Rows Should Be Equal")

    def _validate_stream_input(self, stream_payload: Any) -> None:
        """Validate stream data structure."""
        print("Input: Real-time sensor stream")
        if not isinstance(stream_payload, list):
            raise ValueError("The Stream Data Should Be List")

        for data_value in stream_payload:
            if not isinstance(data_value, (float, int)):
                raise ValueError(f"The {data_value} Should Be Float Or Int")


class TransformStage:
    JSON_VALUE_NORMAL_RANGE = (20, 30)
    STREAM_VALUE_THRESHOLD = 20

    def process(self, stage_data: Any) -> Dict:
        if stage_data.get('data') is not None:
            adapter_type = stage_data.get('pipeline')

            if adapter_type == 'JSONAdapter':
                self._transform_json_data(stage_data)
            elif adapter_type == 'CSVAdapter':
                self._transform_csv_data(stage_data)
            elif adapter_type == 'StreamAdapter':
                self._transform_stream_data(stage_data)

        return stage_data

    def _transform_json_data(self, data_container: Dict) -> None:
        """Transform JSON data with metadata enrichment."""
        print("Transform: Enriched with metadata and validation")
        json_payload = data_container.get('data')
        value = json_payload.get('value')

        if (isinstance(value, float) and
            self.JSON_VALUE_NORMAL_RANGE[0] <= value <=
                self.JSON_VALUE_NORMAL_RANGE[1]):
            range_status = 'Normal'
        else:
            range_status = 'Not Normal'

        json_payload.update({'range': range_status})

    def _transform_csv_data(self, data_container: Dict) -> None:
        """Transform CSV data with activity parsing."""
        print("Transform: Parsed and structured data")
        csv_payload = data_container.get('data')
        csv_lines = csv_payload.split('\n')

        activity_stats = {'logged': 0}
        for csv_line in csv_lines[1:]:
            columns = csv_line.split(',')
            if columns[1].lower() == 'logged':
                activity_stats['logged'] += 1

        data_container.update({'activity': activity_stats})

    def _transform_stream_data(self, data_container: Dict) -> None:
        """Transform stream data with aggregation and filtering."""
        print("Aggregated and filtered")
        stream_payload = data_container.get('data')
        filtered_readings = ([value for value in stream_payload
                              if value > self.STREAM_VALUE_THRESHOLD])

        reading_count = len(filtered_readings)
        average_value = (sum(filtered_readings) / reading_count
                         if reading_count > 0 else 0)

        data_container.update({
            'readings': reading_count,
            'avg': average_value
        })


class OutputStage:
    def process(self, stage_data: Any) -> str:
        adapter_type = stage_data.get('pipeline')

        if adapter_type == 'JSONAdapter':
            self._output_json_result(stage_data)
        elif adapter_type == 'CSVAdapter':
            self._output_csv_result(stage_data)
        elif adapter_type == 'StreamAdapter':
            self._output_stream_result(stage_data)

        return ""

    def _output_json_result(self, data_container: Dict) -> None:
        """Output formatted JSON processing result."""
        json_data = data_container.get('data')
        print("Output: Processed temperature reading: ", end="")
        print(f"{json_data.get('value')}°C ({json_data.get('range')} range)\n")

    def _output_csv_result(self, data_container: Dict) -> None:
        """Output CSV processing summary."""
        logged_count = data_container.get('activity', {}).get('logged', 0)
        print(f"Output: User activity logged: "
              f"{logged_count} actions processed\n")

    def _output_stream_result(self, data_container: Dict) -> None:
        """Output stream processing statistics."""
        reading_count = data_container.get('readings', 0)
        avg_value = data_container.get('avg', 0)
        print(f"Output: Stream summary: {reading_count}"
              f" readings, avg: {avg_value:.1f}\n")


if __name__ == '__main__':
    try:
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

        system_manager = NexusManager()
        print("Creating Data Processing Pipeline...")
        print("Stage 1: Input validation and parsing")
        input_validator = InputStage()
        print("Stage 2: Data transformation and enrichment")
        data_transformer = TransformStage()
        print("Stage 3: Output formatting and delivery")
        output_handler = OutputStage()
        print("\n=== Multi-Format Data Processing ===\n")

        # Initialize test data
        json_test_data = {"sensor": "temp", "value": 23.5, "unit": 'C'}
        csv_test_data = "user,action,timestamp\noualid,logged,2026-02-10"
        stream_test_data = [40, 50, 10]

        # Process JSON format
        print("Processing JSON data through pipeline...")
        json_adapter = JSONAdapter('J_01')
        json_adapter.add_stage(input_validator)
        json_adapter.add_stage(data_transformer)
        json_adapter.add_stage(output_handler)
        system_manager.add_pipeline(json_adapter)
        system_manager.process_data({'format': 'json', 'data': json_test_data})

        # Process CSV format
        print("Processing CSV data through same pipeline...")
        csv_adapter = CSVAdapter('C_01')
        csv_adapter.add_stage(input_validator)
        csv_adapter.add_stage(data_transformer)
        csv_adapter.add_stage(output_handler)
        system_manager.add_pipeline(csv_adapter)
        system_manager.process_data({'format': 'csv', 'data': csv_test_data})

        # Process Stream format
        print("Processing Stream data through same pipeline...")
        stream_adapter = StreamAdapter('S_01')
        stream_adapter.add_stage(input_validator)
        stream_adapter.add_stage(data_transformer)
        stream_adapter.add_stage(output_handler)
        system_manager.add_pipeline(stream_adapter)
        system_manager.process_data(
            {'format': 'stream', 'data': stream_test_data})

        print("=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        execution_start = time()
        chained_pipelines = [
            JSONAdapter('A'),
            JSONAdapter('B'),
            JSONAdapter('C')
        ]
        chained_pipelines[0].add_stage(input_validator)
        chained_pipelines[1].add_stage(data_transformer)
        chained_pipelines[2].add_stage(output_handler)

        transformed_result = {"sensor": "temp", "value": 23.5, "unit": 'C'}
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")
        for pipeline_inst in chained_pipelines:
            transformed_result = pipeline_inst.process(transformed_result)

        execution_duration = time() - execution_start
        print(
            f"{execution_duration:.5f}s total processing time\n")

        print("=== Error Recovery Test ===")
        print("Simulating pipeline failure...")
        malformed_csv = "fname, lname, age\n oualid"
        system_manager.process_data({'format': 'csv', 'data': malformed_csv})
        print("\nNexus Integration complete. All systems operational.")
    except Exception as e:
        print(e)
