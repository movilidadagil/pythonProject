from behave import when, given, then
from base.base import base
from pages.mainpage import mainpage


@then(u'I see this country {country}')
def step_impl(context, country):
    base.verify_component_exists(country)

@then(u'I click this country {country}')
def step_impl(context, country):
    mainpage.click_country_thumb(country)




