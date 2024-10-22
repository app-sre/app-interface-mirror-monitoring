from app_interface_mirror_monitoring.core import app


def test_app() -> None:
    assert app("Hello, world!") == "Hello, world!"
