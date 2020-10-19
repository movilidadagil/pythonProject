from behave import when, given, then
from base.base import base
from pages.mainpage.mainpage import mainpage


@then(u'I see this {country} with {order}')
def step_impl(context, country, order):
    base.verify_component_exists(country,order)

@then(u'I click this {country}')
def step_impl(context, country):
    mainpage.click_country_thumb(country)




