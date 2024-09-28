from DemoWebShop.lib.library import Base

class Filter_condtion(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    computer_locator=("xpath","//ul[@class='top-menu']//a[@href='/computers']")
    desktop_locator=("xpath","//img[@alt='Picture for category Desktops']")
    select_locator=("id","products-orderby")
    option_locator1=("xpath","//option[.='Name: A to Z']")
    option_locator2=("xpath","//option[.='Name: Z to A']")
    option_locator3=("xpath","//option[.='Price: Low to High']")
    option_locator4=("xpath","//option[.='Price: High to Low']")
    display_dropdown_locator=("name","products-pagesize")
    option_locator5=("xpath","//option[.='4']")
    option_locator6=("xpath","//option[.='8']")
    option_locator7=("xpath","//option[.='12']")
    price_locator1=("xpath","//a[contains(@href,'price=-1000')]")
    remove_locator=("xpath","//div[@class='remove-filter']")
    price_locator2=("xpath","//a[contains(@href,'price=1000-1200')]")
    remove_locator2=("xpath","//div[@class='remove-filter']")
    price_locator3=("xpath","//a[contains(@href,'price=1200')]")
    remove_locator3=("xpath","//div[@class='remove-filter']")
    logout_locator=("xpath","//li[.='Log out']")

    def filter_conditions(self, email, password):
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.computer_locator)
        self.click_on_a_element(self.desktop_locator)
        self.click_on_a_element(self.select_locator)
        self.select_a_option(self.select_locator,self.option_locator1)
        self.select_a_option(self.select_locator,self.option_locator2)
        self.select_a_option(self.select_locator,self.option_locator3)
        self.select_a_option(self.select_locator,self.option_locator4)
        self.select_a_option(self.display_dropdown_locator,self.option_locator5)
        self.select_a_option(self.display_dropdown_locator,self.option_locator6)
        self.select_a_option(self.display_dropdown_locator,self.option_locator7)
        self.click_on_a_element(self.price_locator1)
        # self.click_on_a_element(self.remove_locator)
        self.navigational_commands()
        self.click_on_a_element(self.price_locator2)
        self.navigational_commands()
        # self.click_on_a_element(self.remove_locator2)
        self.click_on_a_element(self.price_locator3)
        self.navigational_commands()
        # self.click_on_a_element(self.remove_locator3)
        self.click_on_a_element(self.logout_locator)