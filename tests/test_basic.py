import pytest

import cookiecutter_scverse_instance


def test_package_has_version():
    assert cookiecutter_scverse_instance.__version__ is not None


@pytest.mark.skip(reason="This decorator should be removed when test passes.")
def test_example():
    assert 1 == 0  # This test is designed to fail.
