import allure
from selene import have
from selene.support.conditions.not_ import visible


@allure.suite("Тесты для Cian.ru")
class TestCian:

    @allure.title("Проверка кликабельности кнопки 'Найти' на главной странице Cian")
    def test_open_main_page(self, setup_browser, close_popup):
        browser = setup_browser

        with allure.step("Открываем главную страницу сайта Cian"):
            browser.open("/")
            close_popup()

        with allure.step("Проверяем, что кнопка 'Найти' кликабельна"):
            browser.all('[data-mark="FiltersSearchButton"]').element_by(have.text("Найти")).click()

    @allure.title("Поиск квартиры по параметрам")
    def test_search_apartment_by_parameters(self, setup_browser, close_popup):
        browser = setup_browser

        with allure.step("Открываем главную страницу"):
            browser.open("/")
            close_popup()

        with allure.step("Выбираем 'Купить'"):
            browser.element('a[href*="kupit"]').click()

        with allure.step("Выбираем количество комнат '2'"):
            browser.element('[data-mark="FilterRoomsCount"]').click()
            browser.element("ul._025a50318d--list--gT6p6 li:first-child").click()

        with allure.step("Указываем цену от 5 до 10 млн рублей"):
            browser.element('[data-mark="FilterPrice"]').click()
            browser.element('[placeholder="от"]').type("5_000_000")
            browser.element('[placeholder="до"]').type("10_000_000")

        with allure.step("Нажимаем кнопку 'Найти'"):
            browser.element('[data-mark="FiltersSearchButton"]').click()

        with allure.step("Проверяем, что результаты поиска отображаются"):
            browser.element('[data-name="SummaryHeader"]').wait_until(visible)
            browser.all('[data-name="SummaryHeader"]').element_by(have.text("Найдено" + "объявлений"))
