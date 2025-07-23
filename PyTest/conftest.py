#we create conftest file to add pytest.fixture at one place and use it globally for all the
#test files

import pytest

@pytest.fixture(scope="function")
def prework_function():
    print("fixture setup for each function")
    return "pass"

@pytest.fixture(scope="function")
def prework_function_yeild():
    yield
    print("Fixture teardown for each function")

#i think this yield func we are using after a TC ends
@pytest.fixture(scope="module")
def prework_module():
    print("fixture setup for entire module")

@pytest.fixture(scope="session")
def prework_session():
    print("fixture setup for entire session")
