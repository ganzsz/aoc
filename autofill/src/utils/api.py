import requests
from os.path import exists


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "github.com/ganzsz/aoc, reddit:u/ganzsz, email:hansderooij3@gmail.com"
}
COOKIES = {"session": SESSION}


def get_input(day, YEAR):
    url = get_url(YEAR, day)
    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if not response.ok:
        raise RuntimeError(
            f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
        )
    return response.text[:-1]
