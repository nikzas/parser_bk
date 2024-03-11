from browser_data import ParserAviator


if __name__ == "__main__":
    # Разделить столбцами цифры в csv
    st = ParserAviator()
    m1 = st.corr_text_series()
    while True:
        m2 = st.corr_text_series()
        find_index = st.get_out_index(m1, m2)
        out_massive = st.result_cnt(m1, find_index)
        print(out_massive)
        # output_csv = st.save_in_csv(out_massive)
