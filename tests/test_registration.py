import allure
from selene import have
from faker import Faker

fake = Faker()


@allure.title("Регистрация нового пользователя (валидные данные)")
def test_register_new_user(setup_browser):
    browser = setup_browser

    with allure.step("Открываем главную страницу"):
        browser.open("https://demo.opencart.com/")

    with allure.step("Переходим на страницу регистрации"):
        browser.element('a[title="My Account"]').click()
        browser.element('a[href*="register"]').click()

    with allure.step("Заполняем форму регистрации валидными данными"):
        browser.element("#input-firstname").type(fake.first_name())
        browser.element("#input-lastname").type(fake.last_name())
        browser.element("#input-email").type(fake.email())
        browser.element("#input-password").type("SecurePassword123")
        browser.element('input[name="agree"]').click()

    with allure.step("Отправляем форму регистрации"):
        browser.element('button[type="submit"]').click()

    with allure.step("Проверяем успешную регистрацию пользователя"):
        browser.element("#content h1").should(
            have.text("Your Account Has Been Created!")
        )
