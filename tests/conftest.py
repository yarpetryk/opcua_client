import os
from dotenv import load_dotenv
import pytest
from typing import Iterator

from helpers.opc_client import OPCClient


load_dotenv()

@pytest.fixture
def opc_client(auth) -> Iterator[OPCClient]:
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