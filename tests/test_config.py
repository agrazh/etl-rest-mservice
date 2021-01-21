import pytest
import os.path

def test_config_exists():
    assert os.path.isfile('./app/config.yaml') == True, "Config not found."
