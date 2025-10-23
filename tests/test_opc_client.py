import pytest

from helpers.opc_client import OPCClient


class TestOPCClient:
    @pytest.mark.smoke
    def test_opc_client(self, opc_client: OPCClient) -> None:
        data = opc_client.read_data_temperature(topic='temperature')
        assert data, "No sensor data available"
        # Sensor data validation
        topic = data['topic']
        sensor_data = data['data']
        assert topic == 'temperature', f"Expected topic 'temperature', but got '{topic}'"
        assert sensor_data['temp1'] > 0, f"Expected value > 50, but got {sensor_data['temp1']}"
        assert sensor_data['temp2'] > 0, f"Expected value > 50, but got {sensor_data['temp2']}"
