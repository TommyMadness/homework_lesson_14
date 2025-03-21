import allure
from selene import be, have
from selene.support.shared import browser


class MainPage:

    @allure.step("Открываем главную страницу Cian")
    def open(self):
        browser.open("https://www.cian.ru")

    @allure.step("Закрываем всплывающее окно, если оно появилось")
    def close_popup(self):
        popup_close_button = browser.element("button[title='Закрыть']")
        if popup_close_button.matching(be.visible):
            popup_close_button.click()

    @allure.step("Нажимаем кнопку 'Найти'")
    def click_search_button(self):
        browser.all('[data-mark="FiltersSearchButton"]').element_by(
            have.text("Найти")
        ).click()
