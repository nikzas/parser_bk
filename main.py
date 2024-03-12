from browser_data import ParserAviator
import pandas as pd

if __name__ == "__main__":
    # Разделить столбцами цифры в csv
    st = ParserAviator()
    starting_massive = st.corr_text_series()
    while True:
        m2 = st.corr_text_series()



        # output_csv = st.save_in_csv(out_massive)
