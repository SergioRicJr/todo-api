
def sanitize_data(data):
    """
    Strips whitespace from the beginning and end of strings in the provided dictionary.

    The function iterates over each key-value pair in the dictionary. If the value is a string,
    it strips whitespace from the beginning and end and updates the dictionary with the sanitized string.

    Args:
    - data (dict): Dictionary containing data to be sanitized.

    Returns:
    - dict: Dictionary with sanitized strings.
    """
    
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.strip()
    return data