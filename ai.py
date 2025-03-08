import datetime
import os

from google import genai

class AiClient:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def get_response(self, list_of_files):
        files_string = "'"+ "','".join(list_of_files) + "'"
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Return me a list of file name and dates in format YYYY:MM:DD from the following list. Only return the list in the form of an array of objects of the form (filename, YYYY:MM:DD). Below is the list of files:"
            + files_string,
        )
        return response.text

    def get_file_date(self, file_name):
        try:
            prompt = "Return me the date from the name '"+file_name+"' in format YYYY:MM:DD. Don't add any other text. Just the result. If the name does not have a date in it, just return 'None'"
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            if "None" in response.text:
                return None
            # Validate the date
            datetime.datetime.strptime(response.text, "%Y:%m:%d")
            return response.text
        except:
            return None