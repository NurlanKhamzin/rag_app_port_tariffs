import pandas as pd

def read_csv_content(file_path, content_column='content'):
    """
    Reads a CSV file, extracts and cleans the content from the specified column.

    Parameters:
    - file_path (str): Path to the CSV file.
    - content_column (str): The column containing the text content.

    Returns:
    - str: A combined string of all cleaned text from the content column.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Ensure the specified content column exists
        if content_column not in df.columns:
            raise KeyError(f"Column '{content_column}' not found in the CSV file.")

        # Drop NaN values and filter for string data
        content = df[content_column].dropna()
        content = content[content.apply(lambda x: isinstance(x, str))]

        # Combine all rows into a single string
        combined_text = ' '.join(content.tolist())
        return combined_text

    except Exception as e:
        raise RuntimeError(f"Error reading or processing the CSV file: {e}")
