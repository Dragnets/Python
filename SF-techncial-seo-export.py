import pandas as pd

def column_label_to_index(column_label):
    """ Convert Excel-style column label to zero-based column index. """
    column_index = 0
    for i, char in enumerate(reversed(column_label)):
        column_index += (ord(char.upper()) - ord('A') + 1) * (26 ** i)
    return column_index - 1

def remove_columns(file_path, columns_to_remove, output_file):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)
        
        # Convert column labels to indices
        indices_to_remove = [column_label_to_index(label) for label in columns_to_remove if column_label_to_index(label) < len(df.columns)]
        
        # Drop the specified columns by index
        df.drop(df.columns[indices_to_remove], axis=1, inplace=True)
        
        # Save the modified DataFrame back to an Excel file
        df.to_excel(output_file, index=False)
        print(f"File saved as {output_file} after removing specified columns.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage of the function
if __name__ == "__main__":
    input_file_path = "internal_all.xlsx"
    output_file_path = "modified_internal_all.xlsx"
    columns_to_remove = ['H', 'I', 'K', 'L', 'K', 'N', 'P', 'R', 'S', 'T', 'V', 'X', 'Y', 'AC', 'AD', 'AC', 'AD','AE', 'AF', 'AG', 'AI', 'AJ', 'AM', 'AO', 'AP', 'AQ', 'AS', 'AT', 'AU', 'AV', 'AW','AX', 'AZ', 'BA', 'BB', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK']  # Excel columns to be removed

    remove_columns(input_file_path, columns_to_remove, output_file_path)
