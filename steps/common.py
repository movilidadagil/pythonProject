from behave import given, when, then

from base.base import base


@given(u'I load the website')
def step_impl_load_website(context):
    base.load_website()


@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    base.goto_page(page)

