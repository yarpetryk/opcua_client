import os
import json
from dotenv import load_dotenv
import pytest
from typing import Iterator

from helpers.opc_client import OPCClient


load_dotenv()

@pytest.fixture
def opc_client(auth, get_configurations) -> Iterator[OPCClient]:
    url = os.getenv("URL")
    if auth:
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
    client = OPCClient(url=url, user=user, password=password)
    client.connect()
    yield client
    client.disconnect()
    
def pytest_addoption(parser):
    parser.addoption(
        "--auth",
        action="store",
        default=False,
        help="Select auth: True/False")
    
@pytest.fixture
def auth(request):
    return request.config.getoption("--auth")

@pytest.fixture
def get_configurations():
    config_data = None
    config_path = os.path.join("configs", "dev.json")
    with open(config_path) as f:
        config_data = json.load(f)
    return config_data
    