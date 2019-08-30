from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
driver.get(url)


product_containers = driver.find_elements_by_class_name('product-container')

# enumerate() is used
for index,product_container in enumerate(product_containers):
    time.sleep(2)
    hover = ActionChains(driver).move_to_element(product_container)
    hover.perform()

    #click on add to cart
    #('//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]/span')   is changed to
    #('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1))
    # index of the list is replaced by %s which is the index each iteration since we adding in the cart each
    # of the item

    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()

    time.sleep(5)
    #click on Continue Shopping
    driver.find_element_by_css_selector('#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > span > span > i').click()
    print(index)





