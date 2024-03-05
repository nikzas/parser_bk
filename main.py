from browser_data import ParserAviator


if __name__ == "__main__":
    # Разделить столбцами цифры в csv
    start = ParserAviator()
    global_massive = start.corr_text_df()
    output_csv = start.save_to_csv(global_massive)
    while True:
        next_mass = start.corr_text_series()
        result = start.last_edit_text(global_massive, next_mass)

