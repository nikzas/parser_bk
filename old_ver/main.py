from browser_data import ParserAviator
import pandas as pd


if __name__ == "__main__":
    st = ParserAviator()
    data_current_name = st.get_data()   # Запрос текущей даты
    a = st.corr_text_array()            # Запустили первый массив
    count = a[:5]                       # Забрали первые 5 чисел для поиска
    ALL_MASSIVE = pd.Series(a)

    while True:
        b = st.corr_text_array()  # Запустили 2 массив
        count_nehvat = b[:st.found_index(count, b)[0]]   #Наложили маску - получили числа
        ALL_MASSIVE = pd.concat([count_nehvat, ALL_MASSIVE], ignore_index=True)
        count = b[:5]
        output_csv = st.save_in_csv(ALL_MASSIVE, data_current_name)
        print(ALL_MASSIVE)


