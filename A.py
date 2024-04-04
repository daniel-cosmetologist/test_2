#######################################

# A. Обработка ссылок на GitHub проекты

#######################################

import re

def extract_project_names(urls):
    pattern = r"https?://github\.com/([\w-]+)/([\w-]+)(\.git)?"
    for url in urls:
        match = re.search(pattern, url)
        if match:
            print(match.group(2))
        else:
            print(f"Неверный формат URL: {url}")
    pass

def run():
    urls = [
        "https://github.com/miguelgrinberg/Flask-SocketIO",
        "https://github.com/miguelgrinberg/Flask-SocketIO.git",
        "https://not-a-github-link.com"
    ]
    extract_project_names(urls)