#first we will create a test function which will act as a scenario then
#we will add a fixture function to run b4 each scenario or module(multiple scenario)

def test_scenario1(prework_function, prework_module, prework_session, prework_function_yeild):
    print("Testing scenario1 checked")
    assert prework_function == "pass"

def test_scenario2(prework_function, prework_module, prework_session, prework_function_yeild):
    print("Testing scenario2 checked")
    #here we will not assert the returned value from, prework_function == "pass"