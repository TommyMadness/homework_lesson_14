import re

import allure
from selene import have, be, query
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
            browser.all('[data-mark="FiltersSearchButton"]').element_by(
                have.text("Найти")
            ).click()

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
            browser.all('[data-name="SummaryHeader"]').element_by(
                have.text("Найдено" + "объявлений")
            )

    @allure.title("Фильтрация по наличию видео")
    def test_filter_by_photo(self, setup_browser, close_popup):
        browser = setup_browser

        with allure.step("Открываем страницу поиска квартир с произвольным запросом"):
            browser.open("/")
            close_popup()
            browser.element('a[href*="kupit"]').click()
            browser.element('[data-mark="FiltersSearchButton"]').click()

        with allure.step("Переходим в фильтры"):
            browser.element('[data-name="AdvancedFiltersContainer"]').click()
        with allure.step("Включаем фильтр 'С видео'"):
            browser.all("span").element_by(have.text("Видео")).click()
            browser.all("span").element_by(have.text("Показать")).click()

        with allure.step("Проверяем, что у каждого объявления есть иконка видео"):
            browser.element('[data-name="FeatureLabels"] svg').wait_until(visible)
            listings = browser.all('[data-testid="offer-card"]')

            for listing in listings:
                listing.element('[data-name="FeatureLabels"] svg').should(be.visible)

    @allure.title("Сортировка по цене")
    def test_sort_by_price(self, setup_browser, close_popup):
        browser = setup_browser

        with allure.step("Открываем страницу поиска квартир с произвольным запросом"):
            browser.open("/")
            close_popup()
            browser.element('a[href*="kupit"]').click()
            browser.element('[data-mark="FiltersSearchButton"]').click()

        with allure.step("Выбираем сортировку по возрастанию цены"):
            browser.element('[data-mark="SortDropdownButton"]').click()
            browser.all('[data-name="SelectPopupOption"]').element_by(
                have.text("По цене (сначала дешевле)")
            ).click()

        with allure.step("Ожидаем обновления списка объявлений"):
            browser.wait_until(
                lambda: len(
                    browser.all(
                        '[data-name="GeneralInfoSectionRowComponent"] [data-mark="MainPrice"]'
                    )
                )
                > 5
            )

        with allure.step("Проверяем, что объявления отсортированы по возрастанию цены"):
            price_elements = browser.all(
                '[data-name="GeneralInfoSectionRowComponent"] [data-mark="MainPrice"]'
            )

            prices = [price.get(query.text) for price in price_elements]

            price_values = [
                int(re.search(r"\d[\d\s]*", price).group().replace(" ", ""))
                for price in prices
                if re.search(r"\d[\d\s]*", price)
            ]

            price_values = list(dict.fromkeys(price_values))

            assert price_values == sorted(
                price_values
            ), f"Цены не отсортированы по возрастанию: {price_values}"

