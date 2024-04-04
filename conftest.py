import pytest
import yaml
from module import Site

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def set_locator4():
    return '''h2'''


@pytest.fixture()
def set_locator5():
    return '''#create-btn'''


@pytest.fixture()
def set_locator_create_post():
    return '''//*[@id="app"]/main/div/div/h1'''


@pytest.fixture()
def set_locator6():
    return '''//*[@id="create-item"]/div/div/div[1]/div/label/input'''

@pytest.fixture()
def set_locator7():
    return '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'''

@pytest.fixture()
def set_locator8():
    return '''//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'''

@pytest.fixture()
def set_locator9():
    return '''#create-item > div > div > div:nth-child(7) > div > button > div'''

@pytest.fixture()
def set_locator_new_post():
    return '''//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2'''

@pytest.fixture()
def status_error():
    return '401'


@pytest.fixture()
def set_locator_success():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


# //*[@id="app"]/main/nav/ul/li[3]/a

@pytest.fixture(scope='session')
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()
