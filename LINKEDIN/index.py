from selenium import webdriver
from time import sleep
from selectors import login
class Linkedin:
	def __init__(self):
		self.browser = None
		pass
	def main(self,account):
		chromedriver = 'C:/users/angular_nija_avenger/downloads/chromedriver'
		browser = webdriver.Chrome(chromedriver)
		self.browser = browser
		self.login(account)
		self.get_links()
	def login(self,account):
		x = self.browser
		brow = x.get("https://www.linkedin.com/login")
		email_address = self.selector(login.EMAIL_FIELD)
		email_address.click()
		email_address.send_keys(account["email"])

		password = self.selector(login.PASSWORD_FIELD)
		password.click()
		password.send_keys(account["password"])
		
		submit = self.selector(login.LOGIN_BUTTON)
		submit.click()
		pass
	def selector(self,selector):
		return self.browser.find_element_by_css_selector(selector)

	def get_links(self):
		location = "new york"
		nitch = "real estate agents "
		combined = nitch + location
		page=5
		url = f"https://www.linkedin.com/search/results/companies/?keywords={combined}&origin=SWITCH_SEARCH_VERTICAL&page={page}"
		self.browser.get(url)
		sleep(5)
		page_count = self.selector(login.PAGE_RESULT_COUNT)
		print(page_count.text)
		pass


		# x = self.browser.find_element_by_css_selector("#username").click()
		# print(x)
		# .send_keys("notes")
		# .click().send_keys("notes")
		# browser.get("https://www.linkedin.com/login").find_element_by_css_selector("")
		pass
UserAccount = {
	"email":"linkedinboot@gmail.com",
	"password":"Sha53211"
}
Linkedin().main(UserAccount)


# <----USE THIS URL TO TEST https://www.linkedin.com/search/results/companies/?keywords=real%20estate%20in%20new%20york&origin=SWITCH_SEARCH_VERTICAL 




# self.browser.current_url


