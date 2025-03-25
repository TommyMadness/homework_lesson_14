# Проект автоматизации сайта [Cian.ru](https://cian.ru)
___

### Используемый стек:  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" width="40" height="40"/> <img src="https://plugins.jetbrains.com/files/12513/656687/icon/default.svg" width="40" height="40"/> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1200px-Telegram_logo.svg.png" width="40" height="40"/>

---

## Что тестируется:

### 🔍 Поиск и фильтрация
- Поиск квартиры с параметрами: количество комнат, диапазон цен.
- Применение фильтра "С видео".
- Проверка отображения результатов после применения фильтров.

### 📊 Сортировка
- Проверка сортировки объявлений по возрастанию цены.

### 🗺 Вид отображения
- Переключение отображения с таблицы на карту.

### 🏠 Главная страница
- Проверка кликабельности кнопки "Найти".


---

## Структура проекта:

```
.
├── .env                        # Переменные окружения
├── conftest.py                 # Общие фикстуры и настройки запуска
├── pytest.ini                  # Настройки Pytest
├── requirements.txt            # Зависимости проекта

├── tests/                      # UI-тесты
│   ├── test_main_page.py       # Тесты главной страницы
│   ├── test_filters.py         # Тесты фильтрации и поиска
│   ├── test_sorting.py         # Тесты сортировки

├── pages/                      # Page Object'ы
│   ├── main_page.py            # Главная страница
│   ├── filters_page.py         # Фильтры
│   ├── search_results_page.py  # Результаты поиска

├── utils/                      # Вспомогательные утилиты
│   ├── __init__.py
│   ├── attach.py               # Вложения в Allure (видео, скриншоты)

├── images/                     # Скриншоты и .gif для README
```


---

## Как запустить тесты:

### ⚙️ Локально:
```bash
pytest tests/ --browser_version=134.0
```

### ☁️ Через Selenoid (удаленно):
```bash
pytest tests/ --remote --browser_version=134.0
```

---

## Jenkins CI:
1. Открыть [Jenkins Job](https://jenkins.autotests.cloud/job/atansan_qa_guru_python_homework_lesson_14/)
2. Нажать `Build with parameters`
3. Выбрать нужную версию браузера и параметры запуска (пример: ***127***)
4. Нажать `Build`
5. После завершения — открыть `Allure Report`

---

## Примеры отчётов:

### 📋 Allure Report — Общий результат

### 🔍 Allure Report — Подробный результат

### 🎬 Видеозапись выполнения теста (если опция включена)

### 📬 Уведомление через Telegram бота
<img src="https://github.com/TommyMadness/homework_lesson_14/blob/main/images/Screenshot_telegram.png" width="340" height="340"/>
---

## Автор проекта:
👩‍💻 **@TommyMadness** | Telegram: `@TommyMadness`  
📍 Автоматизация UI тестов с использованием Page Object, Pytest, Selene и Allure