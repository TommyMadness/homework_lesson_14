import allure
from allure_commons.types import Severity
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "atansan")
@allure.feature("Главная страница")
@allure.suite("UI-Тесты")
class TestMainPage:

    @allure.story("Проверка кликабельности кнопки 'Найти'")
    @allure.title("Кнопка 'Найти' доступна и кликабельна")
    def test_open_main_page(self, setup_browser):
        main_page = MainPage()

        main_page.open()
        main_page.close_popup()
        main_page.click_search_button()
