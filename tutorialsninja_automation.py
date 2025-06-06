import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=Options()
options.add_experimental_option("detach",True)
# Chrome open
driver=webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo")


# hover effect of main menu
laptop=driver.find_element(By.XPATH,"//a[text()='Laptops & Notebooks']")
dropdown=ActionChains(driver)
dropdown.move_to_element(laptop).perform()
time.sleep(2)

# click on sub menu
laptop_sub=driver.find_element(By.XPATH,"//a[text()='Show AllLaptops & Notebooks']")
laptop_sub.click()
time.sleep(2)

# click on sub menu
laptop_hp=driver.find_element(By.XPATH,"//a[text()='HP LP3065']")
laptop_hp.click()
time.sleep(2)


# show first image in slider
slider=driver.find_element(By.XPATH,"//ul[@class='thumbnails']/li[1]")
slider.click()
time.sleep(2)

click_next=driver.find_element(By.XPATH,"//button[@title='Next (Right arrow key)']")

for i in range(2):
    click_next.click()
    time.sleep(2)

# screenshot
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
driver.save_screenshot(f"screenshots/screenshot_{timestamp}.png")


# close slider
click_close=driver.find_element(By.XPATH,"// button[ @ title = 'Close (Esc)']")
click_close.click()
time.sleep(1)

add_to_cart_scroll=driver.find_element(By.ID,"button-cart")
add_to_cart_scroll.location_once_scrolled_into_view
time.sleep(1)

# quantity
quantity=driver.find_element(By.ID,"input-quantity")
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)

quantity.send_keys('2')
time.sleep(1)


# select date 31 December 2022
calendar=driver.find_element(By.XPATH,"//i[@class='fa fa-calendar']")
calendar.click()
time.sleep(1)

calendar_next_click=driver.find_element(By.XPATH,"//th[@class='next']")

calendar_year=driver.find_element(By.XPATH,"//th[@class='picker-switch']")

while calendar_year.text != "December 2022":
    calendar_next_click.click()

calendar_day=driver.find_element(By.XPATH,"// td[text() = '31']")
calendar_day.click()
time.sleep(1)


# add to cart
add_to_cart=driver.find_element(By.ID,"button-cart")
add_to_cart.click()
time.sleep(1)

# open to cart
cart_item=driver.find_element(By.ID,"cart-total")
cart_item.click()
time.sleep(2)

# click checkout
checkout=driver.find_element(By.XPATH,"//p[@class='text-right']/a[2]")
checkout.click()
time.sleep(1)


# check guest radio button
guest_check=driver.find_element(By.XPATH,"//input[@value='guest']")
guest_check.click()
time.sleep(1)


# check guest continue button
guest_check_continue=driver.find_element(By.ID,"button-account")
guest_check_continue.click()
time.sleep(1)

# check scroll
guest_scroll=driver.find_element(By.XPATH,"//a[text()='Step 2: Billing Details ']")
guest_scroll.location_once_scrolled_into_view



# form fillup
firstname=driver.find_element(By.ID,"input-payment-firstname")
firstname.click()
time.sleep(1)
firstname.send_keys("test_first_name")


lastname=driver.find_element(By.ID,"input-payment-lastname")
lastname.click()
time.sleep(1)
lastname.send_keys("test_last_name")


email=driver.find_element(By.ID,"input-payment-email")
email.click()
time.sleep(1)
email.send_keys("test222@gmail.com")


telephone=driver.find_element(By.ID,"input-payment-telephone")
telephone.click()
time.sleep(1)
telephone.send_keys("012456789")


address1=driver.find_element(By.ID,"input-payment-address-1")
address1.click()
time.sleep(1)
address1.send_keys("Plot No. 45, Green Park, Mumbai")


city=driver.find_element(By.ID,"input-payment-city")
city.click()
time.sleep(1)
city.send_keys("Mumbai")


postcode=driver.find_element(By.ID,"input-payment-postcode")
postcode.click()
time.sleep(1)
postcode.send_keys("400001")


country=driver.find_element(By.ID,"input-payment-country")
select_country=Select(country)
select_country.select_by_visible_text('India')
time.sleep(1)

region=driver.find_element(By.ID,"input-payment-zone")
select_region=Select(region)
select_region.select_by_visible_text('Gujarat')
time.sleep(1)

# continue button
continue_guest=driver.find_element(By.ID,"button-guest")
continue_guest.click()
time.sleep(1)


continue_btn1=driver.find_element(By.ID,"button-shipping-method")
continue_btn1.click()
time.sleep(1)

agree=driver.find_element(By.XPATH,"//input[@name='agree']")
agree.click()
time.sleep(1)

continue_btn2=driver.find_element(By.ID,"button-payment-method")
continue_btn2.click()
time.sleep(2)


#print total amount
total_amount=driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover']/tfoot/tr[3]/td[2]")
print("Final Product Price : " + total_amount.text)
time.sleep(1)

#click confirm button
confirm_order=driver.find_element(By.ID,"button-confirm")
confirm_order.click()
time.sleep(1)

#click confirm button
confirm_order_msg=driver.find_element(By.XPATH,"//div[@id='content']/h1")
print(confirm_order_msg.text)
time.sleep(1)


# close browser automatically
print("Process Complete")
driver.quit()