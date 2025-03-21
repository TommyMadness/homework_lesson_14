import allure
from selene.support.shared import browser


class FiltersPage:

    @allure.step("Выбираем количество комнат: {rooms}")
    def select_rooms(self, rooms: int):
        browser.element('[data-mark="FilterRoomsCount"]').click()
        browser.element(f"ul._025a50318d--list--gT6p6 li:nth-child({rooms})").click()

    @allure.step("Указываем диапазон цен от {min_price} до {max_price} рублей")
    def set_price_range(self, min_price: str, max_price: str):
        browser.element('[data-mark="FilterPrice"]').click()
        browser.element('[placeholder="от"]').type(min_price)
        browser.element('[placeholder="до"]').type(max_price)

    @allure.step("Применяем фильтры")
    def apply_filters(self):
        browser.element('[data-mark="FiltersSearchButton"]').click()
