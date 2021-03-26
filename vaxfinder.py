import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


def main():

    service = Service('/Users/catemiller/vax-finder/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)

    # CVS
    print("Searching CVS")

    driver.get('https://www.cvs.com/immunizations/'
               'covid-19-vaccine?icid=coronavirus-lp-nav-vaccine')
    driver.find_element_by_link_text("California").click()

    cities = driver.find_elements_by_xpath('.//span[@class = "city"]')
    status = driver.find_elements_by_xpath('.//span[@class = "status"]')

    print("    Appointments are available in the following cities:")
    for ii in range(0, len(status)):
        if (status[ii].text == "Available"):
            print("        " + cities[ii].text)

    print("    To book an appointment: ")
    print('        https://www.cvs.com/vaccine/'
          'intake/store/covid-screener/covid-qns')

    driver.quit()

if __name__ == "__main__":
    main()
