import pytest
from typing import Iterator

from helpers.opc_client import OPCClient


@pytest.fixture
def opc_client() -> Iterator[OPCClient]:
    client = OPCClient(url="opc.tcp://localhost:4840/freeopcua/server/")
    client.connect()
    yield client
    client.disconnect()