from browser_data import ParserAviator
import pandas as pd


# output_csv = st.save_in_csv(all_massive)


if __name__ == "__main__":
    # Разделить столбцами цифры в csv
    st = ParserAviator()
    a = st.corr_text_array()  # Запустили первый массив
    count = a[:5]  # Забрали первые 5 чисел для поиска
    ALL_MASSIVE = pd.Series(a)
    while True:
        b = st.corr_text_array()  # Запустили 2 массив
        count_nehvat = b[:st.found_index(count, b)[0]] #Наложили маску - получили числа
        ALL_MASSIVE = pd.concat([count_nehvat, ALL_MASSIVE], ignore_index=True)
        count = b[:5]
        print(ALL_MASSIVE)


