from selenium import webdriver
import sys
#def main(argv):
#    print ('mierda' + str(argv[0]))
#input  : arg1 = link
#       : arg2 = filetxt to write the find 
def main(argv):
    #start_urls = 'http://www.radiosdelperu.pe/radio-sicuani'
    if 'http' in str(argv[0]):    
        start_urls = str(argv[0])
        #driver = webdriver.Firefox()
        #driver.get(start_urls)
        profile = webdriver.FirefoxProfile()
        profile.set_preference("media.volume_scale", "0.0")
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.minimize_window()
        driver.get(start_urls)
        #driver.minimize_window()
        driver.implicitly_wait(5)
        driver.refresh()
        driver.implicitly_wait(5)
        #tr = driver.page_source 
        #tr = str(tr)
        fil = open('global_sources.txt','a')
        #lol = driver.find_element_by_id('radio-player').get_attribute("src")
        lol = driver.find_element_by_css_selector('audio').get_attribute("src")
        print (lol)
        fil.write(argv[0] + ' >> ' + lol + '\n')
        #next = driver.find_element_by_xpath('//td[@class="pagn-next"]/a')
        driver.close()
    else:
        print ('[ERROR] ' +str(argv[0]) + '  > no es link. ')
    pass

if __name__ == "__main__":
    main(sys.argv[1:])