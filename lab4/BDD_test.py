from behave import *
from TDD_test import *

@given("Furniture_Builder")
def first_step(context):
    context.a = Furniture_Builder_Test()

@when("test_shatura_builder return OK")
def test_shatura_builder(context):
    context.a.test_shatura_builder()

@when("test_lasurit_builder return OK")
def test_lasurit_builder(context):
    context.a.test_lasurit_builder()

@then("Good job")
def last_step(context):
    pass

