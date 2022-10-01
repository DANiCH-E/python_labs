from behave import *

from Lab6.TDD_test.HW_TDD import *

@given('Bot')
def first_step(context):
    context.a = Calc_Test()

@when('test_1 return OK')
def test_1(context):
    context.a.test_1()

@when('test_2 return OK')
def test_2(context):
    context.a.test_2()

@then('all right')
def last_step(context):
    pass