import pytest
import yaml
from module import Site

with open('datatest.yaml') as f:
    data = yaml.safe_load(f)

site = Site(data['address'])


def test_1(site, set_locator1, set_locator2, set_locator3, set_locator4, set_locator_success):
    selector1 = set_locator1
    input1 = site.find_element('xpath', selector1)
    input1.send_keys(data['username_01'])
    selector2 = set_locator2
    input2 = site.find_element('xpath', selector2)
    input2.send_keys(data['password_01'])
    selector3 = set_locator3
    input3 = site.find_element('css', selector3)
    input3.click()
    set_locator_success = set_locator_success
    find1 = site.find_element('xpath', set_locator_success)
    assert find1.text == 'Hello, testUserGroup4637'


if __name__ == '__main__':
    pytest.main(['-vv'])