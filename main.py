from browser_data import ParserAviator
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Разделить столбцами цифры в csv
    st = ParserAviator()
    all_massive = pd.Series()
    while True:
        starting_massive = st.corr_text_array()  # Запустили первый массив
        first_count = starting_massive[:5]  # Забрали первые 5 чисел для поиска
        second_count = st.corr_text_array()  # Запустили 2 массив
        indexes = st.found_index(first_count, second_count)
        add_mask = second_count[:indexes[0]]        #Наложили маску - получили числа
        all_massive = np.concatenate((all_massive, starting_massive), axis=0)


        #output_csv = st.save_in_csv(all_massive)



