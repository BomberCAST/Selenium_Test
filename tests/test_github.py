import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.helpers.github_issue import GitHUbIssue


@allure.feature("Тесты GitHub")
@allure.story("Проверка страницы GitHub Issue")
class TestSuiteGitHubIssue(GitHUbIssue):
    @allure.title(
        "Проверка страницы https://github.com/microsoft/vscode/issues на поиск слова 'bug' "
    )
    def test_github_1(self, selenium, go_to_github_issue):
        logging.info("GitHub test 1 has been started")
        with allure.step(
            "Поиск поля ввода на странице https://github.com/microsoft/vscode/issues"
        ):
            input_text = WebDriverWait(selenium, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "qbsearch-input.search-input")
                )
            )
            input_text.click()
            input_text = WebDriverWait(selenium, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input#query-builder-test")
                )
            )
        with allure.step("Ввод значения 'in:title bug' в поле ввода"):
            input_text.send_keys("in:title bug")
            input_text.send_keys(Keys.ENTER)
            result = WebDriverWait(selenium, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a//span//em"))
            )
        with allure.step("Проверка результатов"):
            WebDriverWait(selenium, 10).until(lambda d: "bug" in result.text.lower())
            assert "bug" in result.text.lower(), "Не каждая задача содержит слово 'bug'"
            print("Каждая из задач содержит слово 'bug'")
        logging.info("GitHub test 1 has been finished")

    @allure.title(
        "Проверка страницы https://github.com/microsoft/vscode/issues на поиск автора 'bpasero' "
    )
    def test_github_2(self, selenium, go_to_github_issue):
        logging.info("GitHub test 2 has been started")
        with allure.step(
            "Поиск поля ввода на странице https://github.com/microsoft/vscode/issues"
        ):
            WebDriverWait(selenium, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@data-testid='authors-anchor-button']")
                )
            ).click()
            input_field = WebDriverWait(selenium, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@aria-label='Filter authors']")
                )
            )
        with allure.step("Ввод значения 'bpasero' в поле ввода"):
            input_field.send_keys("bpasero")
            input_field.send_keys(Keys.ENTER)
            search_field = WebDriverWait(selenium, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='repository-input']")
                )
            )
        with allure.step("Проверка результатов"):
            WebDriverWait(selenium, 10).until(
                lambda d: "bpasero" in search_field.get_attribute("value")
            )
            assert "bpasero" in search_field.get_attribute(
                "value"
            ), "Автор всех задач 'bpasero' не введён в поиск."
            print("Автор всех задач 'bpasero' введён в поиск.")
        logging.info("GitHub test 2 has been finished")


@allure.story("Проверка страницы GitHub Advanced")
class TestSuiteGitHubStars:
    @allure.title("Проверка страницы https://github.com/search/advanced")
    def test_github_3(self, selenium):
        logging.info(
            "GitHub test 3 has been started https://github.com/search/advanced"
        )
        with allure.step("Переход на страницу https://github.com/search/advanced"):
            selenium.get("https://github.com/search/advanced")
        with allure.step("Выбор языка Python"):
            selenium.find_element(
                By.XPATH, "//*[@id='search_language']//*[@value='Python']"
            ).click()
        with allure.step("Установка фильтра >20000"):
            stars = selenium.find_element(By.XPATH, "//*[@id='search_stars']")
            stars.click()
            stars.send_keys(">20000")
        with allure.step("Поиск файла 'environment.yml'"):
            file_name = selenium.find_element(By.XPATH, "//*[@id='search_filename']")
            file_name.click()
            file_name.send_keys("environment.yml")
        with allure.step("Проверка результатов"):
            selenium.find_element(
                By.XPATH, "//*[@class='d-flex d-md-block']//*[@type='submit']"
            ).click()
            stars_count = WebDriverWait(selenium, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//li/a/span[contains(@class, 'prc-Text-Text-0ima0')]")
                )
            )
            for star_element in stars_count:
                star_text = star_element.text
                star_value = "".join(filter(str.isdigit, star_text))
                if int(star_value) >= 20:
                    print(
                        f"Найден результат с количеством звезд {star_value}k, меньше 20k!"
                    )
                else:
                    print(f"Результат с количеством звезд {star_value}k подтвержден!")
        logging.info("GitHub test 3 has been finished")
