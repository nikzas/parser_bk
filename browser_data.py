from playwright.sync_api import sync_playwright
import pandas as pd
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
            self.page.wait_for_selector(".sc-ZqFbI").click()  # Для клика по кнопке используем див класс находящийся во flex
            self.page.screenshot(path="example.png")
            return self.page.locator(".sc-UpCWa").text_content()  #Для замены используем <div id="history" # class="sc-UpCWa fohmDx">

    def corr_text_df(self):
        """Текст для DataFrame"""
        massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']  # Здесь  уже float
        df = pd.DataFrame(massive)
        return df

    def corr_text_series(self):
        """Текст для Series"""
        massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']
        ser = pd.Series(massive)
        return ser

    def last_edit_text(self, first_mass, next_mass):
        first_cnt = first_mass[0:3].stack()
        index_find = next_mass[next_mass.isin(first_cnt)].index
        global_massive = pd.concat([next_mass[:index_find.values[0]], first_mass]).reset_index(drop=True)
        print(global_massive)
        return global_massive

    def get_out_index(self, mass1, mass2):
        first_cnt = mass1[0:5]
        find_index = mass2[mass2.isin(first_cnt)].index
        if not find_index.empty:
            need_count = mass2[:find_index[0]]
            return need_count
        else:
            massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']
            ser1 = pd.Series(massive)
            return ser1

    def result_cnt(self, f_m, add_numbers):
        result = pd.concat([add_numbers, f_m]).reset_index(drop=True)
        return result

    def get_data(self):
        """Запрос времени"""
        current_date = datetime.date.today().isoformat()
        return current_date

    def save_in_csv(self, data_znach):
        """Создание csv"""
        return data_znach.to_csv('result_to_{}.csv'.format(self.get_data()), encoding='utf-8')
