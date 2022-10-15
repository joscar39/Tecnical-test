import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ArrayChallenge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./Resource/chromedriver.exe")

    def test_001(self):  # Access to web and display the correct alert when submit correctly response of challenge
        driver = self.driver
        web = "http://localhost:3000"
        driver = self.driver
        driver.get(web)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@data-test-id = 'render-challenge']").click()
        # save the value of the table
        array_rows = []
        for c in range(1, 4):
            array_columns = []
            for r in range(0, 9):
                value_ele = None
                value_ele = driver.find_element(By.XPATH,
                                                f"//td[@data-test-id='array-item-{c}-{r}']").text  # find element for position of rows and columns
                array_columns.append(int(value_ele))
            array_rows.append(array_columns)
        # Save value index
        challenge_response = []
        for i in range(0, 3):
            lf = len(array_rows[i])
            for a in range(0, lf + 1):
                left = sum(array_rows[i][0:a])  # sum of all values starting at position 0
                right = sum(array_rows[i][
                            a + 1:])  # sum of all values starting at secund position upper of value of the var left
                if left == right:
                    challenge_response.append(
                        a)  # Save in array the index of value correct between the sum of left and right
                    print(f"Value correct for the Row 0{i+1} its: {array_rows[i][a]} and him index is: {a}")
                    break
                elif (a == lf) and (left != right):
                    challenge_response.append(
                        "null")  # if the sum values between left and right don't match returns null
                    print(f"The rows 0{i+1}, dont have index")

        # Scrolling to find button of send result
        button_send_result = driver.find_element(By.XPATH, "//span[contains(text(), 'Enviar respuestas')]")
        driver.execute_script("arguments[0].scrollIntoView();", button_send_result)

        # Send value of the result of challenge
        inputs_result = driver.find_elements(By.XPATH, "//input")
        for r in range(0, 4):
            if r == 3:
                inputs_result[r].send_keys("Joscar Sosa")
                break
            inputs_result[r].send_keys(challenge_response[r])

        # Click in button of send result and display the alert correctly
        button_send_result.click()
        time.sleep(2)
        search_text_alert = driver.find_elements(By.XPATH, "//div")
        alert_success = None
        for search in search_text_alert:
            if search_text_alert[search_text_alert.index(search)].text == "Felicitaciones, lo has conseguido. Por favor envíe su desafío ✅":
                alert_success = True
                break
            elif search_text_alert[search_text_alert.index(search)].text == "Parece que tu respuesta no fue del todo correcta ❌":
                alert_success = False
                break

        assert alert_success is True, "Error, don't displayed the correct alert"
        print("Correct alert, for the response correctly")
        driver.find_element(By.XPATH, "//span[contains(text(),'Close')]").click()
        time.sleep(2)

    def test_002(self, rws0=1, rws1=5, rws2=6):  # Access to web and display the correct alert when submit incorrectly response of the challenge
        driver = self.driver
        web = "http://localhost:3000"
        driver = self.driver
        driver.get(web)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@data-test-id = 'render-challenge']").click()

        # Scrolling to find button of send result
        button_send_result = driver.find_element(By.XPATH, "//span[contains(text(), 'Enviar respuestas')]")
        driver.execute_script("arguments[0].scrollIntoView();", button_send_result)

        # Send value incorrect of the challenge
        inputs_result = driver.find_elements(By.XPATH, "//input")

        challenge_response = [rws0, rws1, rws2]
        for r in range(0, 4):
            if r == 3:
                inputs_result[r].send_keys("Joscar Sosa")
                break
            inputs_result[r].send_keys(challenge_response[r])
            print(f"the value send as response of the rows 0{r+1} is: {challenge_response[r]}")

        # Click in button of send result and display the alert correctly
        button_send_result.click()
        time.sleep(2)
        search_text_alert = driver.find_elements(By.XPATH, "//div")
        alert_fails = None
        for search in search_text_alert:
            if search_text_alert[search_text_alert.index(search)].text == "Felicitaciones, lo has conseguido. Por favor envíe su desafío ✅":
                alert_fails = False
                break
            elif search_text_alert[search_text_alert.index(search)].text == "Parece que tu respuesta no fue del todo correcta ❌":
                alert_fails = True
                break
        assert alert_fails is True, "Error, dont view the correct alert"
        print("Correct alert, for the response incorrect")
        driver.find_element(By.XPATH, "//span[contains(text(),'Close')]").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ArrayChallenge)
    unittest.TextTestRunner(verbosity=2).run(suite)
