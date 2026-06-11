from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    print("msg")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

    article_count = driver.find_element(By.CSS_SELECTOR, value="td.hp-statistieken div p b").text

    print(article_count)

    driver.quit()
