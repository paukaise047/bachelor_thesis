import openpyxl


def write_words_to_excel(words_file, excel_file):
    # Open the words file and read its content
    with open(words_file, 'r') as file:
        words_content = file.read().split(', ')

    # Create a new workbook
    workbook = openpyxl.Workbook()
    # Create a new sheet
    sheet = workbook.create_sheet(title="Words")

    # Calculate the number of rows needed based on the number of words and 7 words per row
    num_rows = (len(words_content) + 6) // 7

    # Write the words to the Excel sheet
    for i in range(num_rows):
        row_start = i * 7
        row_end = min((i + 1) * 7, len(words_content))
        sheet.append(words_content[row_start:row_end])

    # Save the workbook to the specified Excel file
    workbook.save(excel_file)

    print("Excel file created successfully with a new sheet named 'Words'.")


# Write the words from the file to the Excel file
write_words_to_excel(
    'divergent-association-task/words_script.txt',
    '/Users/paulkaiser/Desktop/Uni/Semester6/Bachelorarbeit/wordscores_82.xlsx')