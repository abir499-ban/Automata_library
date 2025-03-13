import os
from datetime import datetime

def makeFile(latex_code):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    directory = os.path.join(base_dir, 'my_samples')

    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    unique_file_name = "code_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".tex"

    file_path = os.path.join(directory, unique_file_name)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(latex_code)

        print(f"LaTeX file saved at: {file_path}")
        return file_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None
