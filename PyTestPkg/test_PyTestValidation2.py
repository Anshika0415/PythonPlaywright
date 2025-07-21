#first we will create a test function which will act as a scenario then
#we will add a fixture function to run b4 each scenario or module(multiple scenario)
#scopes can be function, module/class, session
#to run multiple test files at a time use terminal commands and file name should start with test keyword


def test_scenario3(prework_function, prework_module, prework_session, prework_function_yeild):
    print("Testing scenario3 checked")
    assert prework_function == "fail"