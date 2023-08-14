from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        link_topup = request.args.get('url')  # Get the 'url' parameter from the query

        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run browser in headless mode

        with webdriver.Chrome(options=chrome_options) as driver:
            driver.get('https://www.arcshop.in.th/topup/truewalletGift')
            
            # Delete the 'arcshop' cookie if it exists
            if 'arcshop' in [cookie['name'] for cookie in driver.get_cookies()]:
                driver.delete_cookie('arcshop')
            
            # Add the updated 'arcshop' cookie
            arcshop_cookie = {
                'name': 'arcshop',
                'value': '7bkpbngo1p0qk5mi7nigs37nek8rntck',
                'domain': 'www.arcshop.in.th'
            }
            driver.add_cookie(arcshop_cookie)
            
            # Delete the 'arcshopaccount' cookie if it exists
            if 'arcshopaccount' in [cookie['name'] for cookie in driver.get_cookies()]:
                driver.delete_cookie('arcshopaccount')
            
            # Add the updated 'arcshopaccount' cookie
            arcshopaccount_cookie = {
                'name': 'arcshopaccount',
                'value': 'kqODrMcgCDSKGtXPJlsxaooXiGaeyqfmWMhAEQzdHbAcdrjjtuIvwHvUNxpiVTTs',
                'domain': 'www.arcshop.in.th'
            }
            driver.add_cookie(arcshopaccount_cookie)
            
            driver.get('https://www.arcshop.in.th/topup/truewalletGift')
            input_element = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/form/div[2]/div[1]/input")
            input_element.send_keys(link_topup)

            result = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/form/div[2]/div[1]/div")
            result.click()
            time.sleep(1)
            print(result.text)
            if result.text == "ไม่พบข้อมูลลิงค์ซองของขวัญ, กรุณาตรวจสอบใหม่อีกครั้ง":
                print("ลิ้งมึงไม่ถูก")
                response = {
                    "message": "ไม่พบข้อมูลลิงค์ซองของขวัญ"
                }
                return response
            else:
                numbers = re.findall(r'\d+', result.text)

                if numbers:
                    extracted_number = numbers[0]
                    response = {
                        "message": "พบข้อมูลลิ้งซองของขวัญ",
                        "amount": extracted_number
                    }
                    return response
                else:
                    response = {
                    "message": "ไม่พบข้อมูลลิงค์ซองของขวัญ"
                    }
                    return response
            


            
            time.sleep(30)
    except Exception as error:
        print('Selenium Error:', error)
        return 'An error occurred while fetching the data.', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
