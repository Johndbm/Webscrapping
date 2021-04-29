from selenium import webdriver

####################################################
########## Sección Instrucciones e Inputs ##########
####################################################
print('Please, paste the url of the video here')
input = input()

##################################################
############## Sección de Variables ##############
##################################################
url = input

########################################################
########## Sección de Instrucciones WebDriver ##########
########################################################
# Ideas: proximamente Incluir selector de diferentes webdrivers (ej: gecko, chrome, etc...)

browser = webdriver.Firefox()
browser.get(url)

browser.find_element_by_url('https://mega.nz/file/')+'*'.click()
#browser.find_element_by_url('https://mega.nz/file/VjJR3AJa#G5QUpdZl5i4SdE6YZ4uHT8JVR9mPnIgbXe-5rboPYgs').click()

##browser.find_element_by_xpath('//*[@id="embed-code-field"]').click()