from playwright.sync_api import sync_playwright
import pandas as pd
import numpy as np
import datetime


class ParserAviator():
    def __init__(self):
        self.page = None

    def run(self):
        """Запуск и вывод str для дальнейшей обработки"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            self.page = browser.new_page()
            self.page.goto("https://lucky-jet.gamedev-atech.cc/"
                           "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
            self.page.wait_for_selector(".sc-kAkpmW").click()  # Для клика по кнопке используем див класс находящийся во flex
            self.page.screenshot(path="example.png")
            return self.page.locator(".sc-ggpjZQ").text_content()  #Для замены используем <div id="history" # class="sc-UpCWa fohmDx">

    def corr_text_array(self):
        """Текст для array"""
        massive = pd.Series([float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != ''])
        if len(massive) == 20:
            return massive
        elif len(massive) == 21:
            return massive[1:21]
        elif len(massive) <= 19:
            massive2 = pd.Series([float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != ''])
            return massive2

    def get_data(self):
        """Запрос времени"""
        current_date = datetime.date.today().isoformat()
        return current_date

    def save_in_csv(self, data_znach):
        """Создание csv"""
        return data_znach.to_csv('result_to_{}.csv'.format(self.get_data()), encoding='utf-8')

    def found_index(self, first_cnt, st_ms):
        window_size = len(first_cnt)
        is_subset = False
        found_indices = []

        for i in range(len(st_ms) - window_size + 1):
            window = st_ms[i:i + window_size]
            if np.array_equal(window, first_cnt):
                is_subset = True
                found_indices = pd.Index(list(range(i, i + window_size)))
                break
        return found_indices