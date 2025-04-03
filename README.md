# Автоматизация тестирования сайта Demoblaze

Этот проект представляет собой набор автоматизированных тестов для сайта [Demoblaze](https://www.demoblaze.com/index.html), разработанных с использованием Python, Playwright, pytest и Allure.

## Технологии

* **Python:** Основной язык программирования для написания тестов.
* **Playwright:** Библиотека для автоматизации браузера, обеспечивающая надежное и быстрое выполнение тестов.
* **pytest:** Фреймворк для запуска тестов и управления тестовыми наборами.
* **Allure:** Библиотека для создания подробных и наглядных отчетов о результатах тестирования.

## Установка


1.  **Клонируйте репозиторий**:
    ```
    git clone https://github.com/PolaArtInt/Demoblaze/
    ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    ```
    
    Для Linux/macOS:
    ```bash
    source venv/bin/activate
    ```
   
   Для Windows:
   ```bash
    venv/Scripts/activate.ps1
    ```

3. **Установите зависимости:**
   
   ```bash
    pip install -r requirements.txt
   ```

4. **Запуск тестов**
   Для того, чтобы запустить все тесты, выполните следующую команду в корне проекта:

    ```bash
    pytest
    ```

## Запуск тестов

Для запуска всех тестов выполните следующую команду:

```bash
pytest tests/ --alluredir=allure-results
```

Для запуска отдельных тестов или тестовых наборов используйте стандартные возможности pytest.

## Структура проекта

```
Demoblaze/
├── tests/              # Каталог с тестовыми файлами
│   ├── test_login.py     # Тесты для страницы логина
│   ├── test_product.py   # Тесты для страницы товара
│   └── ...
├── pages/              # Каталог с объектами страниц (Page Objects)
│   ├── login_page.py     # Объект страницы логина
│   ├── product_page.py   # Объект страницы товара
│   └── ...
├── utils/              # Каталог с вспомогательными функциями и классами
│   ├── ...
├── allure-results/     # Каталог для результатов Allure
├── README.md           # Этот файл
└── requirements.txt    # Файл с зависимостями проекта
```

## Дополнительная информация

* В каталоге pages/ находятся объекты страниц (Page Objects), которые упрощают взаимодействие с элементами сайта.
* В каталоге utils/ находятся вспомогательные функции и классы, которые используются в тестах.
* В файле requirements.txt перечислены все зависимости проекта.
* Для запуска тестов в headless режиме используйте опцию --headed=false.
* Для запуска тестов в определенном браузере используйте опцию --browser=<browser_name>, где <browser_name> может быть chromium, firefox или webkit.

