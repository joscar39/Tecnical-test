import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ArrayChallenge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./Resource/chromedriver.exe")

    def test_001(self):

        driver = self.driver
        web = "http://localhost:3000"
        driver = self.driver
        driver.get(web)
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@data-test-id = 'render-challenge']").click()
        # Guardar los valores de la tabla
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
                    challenge_response.append(a)  # Save in array the index of value correct between the sum of left and right
                    break
                elif (a == lf) and (left != right):
                    challenge_response.append(
                        "null")  # if the sum values between left and right don't match returns null

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

        # Click button send result
        button_send_result.click()
        alert_success = driver.find_element(By.XPATH, "")
        assert alert_succes
        time.sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ArrayChallenge)
    unittest.TextTestRunner(verbosity=2).run(suite)
