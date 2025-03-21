import allure
from selene import be, have, query
from selene.support.shared import browser
import re


class SearchResultsPage:

    @allure.step("Проверяем, что результаты поиска отображаются")
    def verify_results_loaded(self):
        browser.element('[data-name="SummaryHeader"]').wait_until(be.visible)
        browser.all('[data-name="SummaryHeader"]').element_by(have.text("Найдено"))

    @allure.step("Включаем фильтр 'Только с видео'")
    def filter_by_video(self):
        browser.element('[data-name="AdvancedFiltersContainer"]').click()
        browser.all("span").element_by(have.text("Видео")).click()
        browser.all("span").element_by(have.text("Показать")).click()

    @allure.step("Проверяем, что у каждого объявления есть иконка видео")
    def verify_all_listings_have_video_icon(self):
        browser.element('[data-name="FeatureLabels"] svg').wait_until(be.visible)
        listings = browser.all('[data-testid="offer-card"]')

        for listing in listings:
            listing.element('[data-name="FeatureLabels"] svg').should(be.visible)

    @allure.step("Переход на страницу поиска квартир")
    def go_to_search_results(self):
        browser.element('a[href*="kupit"]').click()
        browser.element('[data-mark="FiltersSearchButton"]').click()

    @allure.step("Выбираем сортировку по возрастанию цены")
    def sort_by_price_ascending(self):
        browser.element('[data-mark="SortDropdownButton"]').click()
        browser.all('[data-name="SelectPopupOption"]').element_by(
            have.text("По цене (сначала дешевле)")
        ).click()

    @allure.step("Ожидаем обновления списка объявлений")
    def wait_for_results_to_update(self):
        browser.wait_until(
            lambda: len(
                browser.all(
                    '[data-name="GeneralInfoSectionRowComponent"] [data-mark="MainPrice"]'
                )
            )
            > 5
        )

    @allure.step("Проверяем, что объявления отсортированы по возрастанию цены")
    def verify_sorted_by_price(self):
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
