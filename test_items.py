import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_korzina(browser):
    browser.get(link)
    # Nahodim knopku kupit
    
    knopka = browser.find_element_by_css_selector('button.btn:nth-child(3)')
    return knopka
    time.sleep(10)
    assert 'button.btn:nth-child(3)' == knopka

    time.sleep(5)