from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_scores_service(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')

    my_driver = webdriver.Chrome(chrome_options=options)
    my_driver.get(url)
    score_web_element = my_driver.find_element_by_tag_name("h1")
    text = score_web_element.get_attribute("innerHTML")
    split_text = text.split(" ")
    score = int(split_text[3])
    if score in range(1, 1000):
        return True
    return False


def main():
    bol = test_scores_service("localhost:8080/score")
    status_code = 0
    if not bol:
        status_code = 1
    print(f"the test ended with status code {status_code}")
    return status_code


if __name__ == "__main__":
    main()
