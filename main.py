from browser_data import ParserAviator


if __name__ == "__main__":
    # Разделить столбцами цифры в csv
    st = ParserAviator()
    start_mas = st.corr_text_df()
    while True:
        next_mass = st.corr_text_series()
        result = st.last_edit_text(start_mas, next_mass)
        output_csv = st.save_in_csv(result)


