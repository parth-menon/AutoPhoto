import re
import datetime


def extract_and_validate_date(filename):
    date_patterns = [
        r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
        r'\d{2}-\d{2}-\d{4}',  # MM-DD-YYYY
        r'\d{2}-\d{2}-\d{4}',  # DD-MM-YYYY
        r'\d{4}/\d{2}/\d{2}',  # YYYY/MM/DD
        r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY
        r'\d{2}/\d{2}/\d{4}',  # DD/MM/YYYY
        r'(20\d{2}(0[1-9]|1[0-2])(0[1-9]|[0-9]|3[0-9]))',  # YYYYMMDD
    ]
    date_formats = {
        r'\d{4}-\d{2}-\d{2}': "%Y-%m-%d",
        r'\d{2}-\d{2}-\d{4}': "%m-%d-%Y",
        r'\d{4}/\d{2}/\d{2}': "%Y/%m/%d",
        r'\d{2}/\d{2}/\d{4}': "%m/%d/%Y",
        r'(20\d{2}(0[1-9]|1[0-2])(0[1-9]|[0-9]|3[0-9]))': "%Y%m%d"
    }

    for pattern in date_patterns:
        match = re.search(pattern, filename)
        if match:
            date_string = match.group()
            date_format = date_formats.get(pattern, "%Y-%m-%d")  # Default to YYYY-MM-DD

            # Validate the date
            try:
                dt = datetime.datetime.strptime(date_string, date_format)
            except ValueError:
                return None

            # Format the datetime object into YYYY:MM:DD
            formatted_date_string = dt.strftime("%Y:%m:%d")

            return formatted_date_string
        else:
            continue
    return None