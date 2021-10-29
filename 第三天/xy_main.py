class main:
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,passwork):
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/input[2]').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/input[3]').send_keys(passwork)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/input[4]').click()

    def getSuccess_result(self):
        return self.driver.title

    def getError_result(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/label[1]').text