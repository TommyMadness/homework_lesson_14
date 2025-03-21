import allure


class FiltersPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Выбираем количество комнат: {rooms}")
    def select_rooms(self, rooms: int):
        self.browser.element('[data-mark="FilterRoomsCount"]').click()
        self.browser.element(
            f"ul._025a50318d--list--gT6p6 li:nth-child({rooms})"
        ).click()

    @allure.step("Указываем диапазон цен от {min_price} до {max_price} рублей")
    def set_price_range(self, min_price: str, max_price: str):
        self.browser.element('[data-mark="FilterPrice"]').click()
        self.browser.element('[placeholder="от"]').type(min_price)
        self.browser.element('[placeholder="до"]').type(max_price)

    @allure.step("Применяем фильтры")
    def apply_filters(self):
        self.browser.element('[data-mark="FiltersSearchButton"]').click()
