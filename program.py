import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://makeambigrams.com/ambigram-generator/')
soup = BeautifulSoup(response.text, 'lxml')


ambi_input = soup.select('#theWord')


# there's a security math problem on the form
def get_security_question():
    return list(filter(lambda x: isinstance(x, str), soup.select('#ambiform')[0].contents))[5]


def solve_security_question(question):
    a, b = [eval(s) for s in re.findall('\d+', question)]
    is_plus_operator = '+' in question
    return a + b if is_plus_operator else a - b
