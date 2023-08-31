# test_main_2.py

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_Ohrm_modules:

      @pytest.fixture
      def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Ohrm_data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

               
      def test_TC_PIM_01_search(self, booting_function): #(TC_PIM_01 checks if Validation performed Successfully on the admin page in both uppercase and lowercase)
     
        #login
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
        self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()

        #ADMIN & admin
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.admin_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().admin).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.admin_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().admin).click()

        #PIM & pim
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.pim_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.pim_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim).click()

        #LEAVE & leave 
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.leave_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().leave).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.leave_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().leave).click()

        #TIME & time
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.time_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().time).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.time_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().time).click()

        #RECRUITMENT & recruitment 
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.recruitment_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().recruitment).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.recruitment_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().recruitment).click()

        #MY INFO & my info 
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.myinfo_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().myinfo).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.myinfo_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().myinfo).click()

        #PERFORMANCE & performance 
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.performance_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().performance).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.performance_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().performance).click()

        #DASHBOARD & dashboard 
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.dashboard_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().dashboard).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.dashboard_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().dashboard).click()

        #DIRECTORY & Directory 
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.directory_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().directory).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.directory_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().directory).click()

        #Maintenance Upper case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.maintenance_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().maintenance).click()

        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().password).send_keys(data.Ohrm_data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().confirm_button).click() 

        #Maintenance Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.maintenance_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().maintenance).click()

        #Buzz Upper & Lower case search inputs
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.buzz_upper)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().buzz).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_inputbox).send_keys(data.Ohrm_data.buzz_lower)
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().buzz).click()

        assert self.driver.title ==  self.driver.title
        print("TC_PIM_01 : Validation performed Successfully on the admin page")
      
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
        self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
        self.driver.close()


      def test_TC_PIM_02_Drop_down_toggled(self,booting_function): #(Validating of page header and drop-down in admin module)

         self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
         self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()

         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().admin).click()
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().user_management).click() 
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().user).click()   
         sleep(1)

         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().user_role).click()      
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().user_role_admin).click()      
         sleep(2)

         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().user_role).click()      
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().user_role_ESS).click()      
         sleep(2)

         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().status).click()      
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().status_enabled).click()      
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().status).click()      
         sleep(2)
         self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().status_disabled).click()      
         sleep(2)
         assert self.driver.title ==  self.driver.title
         print("TC_PIM_02 : Validation performed Successfully on page header and drop-down in admin module")
         self.driver.close()



      def test_TC_PIM_03_add_employee(self,booting_function): # (Adding a New Employee under PIM)
         
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()

          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().add_module).click() 
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().employee_firstname).send_keys(data.Ohrm_data().first_name)
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().employee_lastname).send_keys(data.Ohrm_data().last_name)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().create_login).click()
          sleep(3)
     
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().login_name).send_keys(data.Ohrm_data().login_username)           
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().login_password).send_keys(data.Ohrm_data().login_password)         
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().confirm_password).send_keys(data.Ohrm_data().confirm_password)                                 
          self.driver.find_element(by=By.XPATH, value =locators.Ohrm_locators().save_1_button).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_2_button).click() 
          
          assert self.driver.title ==  self.driver.title
          print("TC_PIM_03 : New employee Successfully added")
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
          self.driver.close()


      def test_TC_PIM_04_Check_tab_details(self,booting_function): #(checking tab details)
          sleep(3)
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
          sleep(3)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
          self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()     
          sleep(3) 
          self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
          sleep(3) 
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pers_details).text == "Personal Details"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().cont_details).text == "Contact Details"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().emer_details).text == "Emergency Contacts"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().depen_details).text == "Dependents"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().immigration).text == "Immigration"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().job).text == "Job"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().salary).text == "Salary"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().tax_exemp).text == "Tax Exemptions"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().report_to).text == "Report-to"
          assert self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().qualifications).text == "Qualifications"
          assert self.driver.find_element(by=By.XPATH, value = locators.Ohrm_locators().memberships).text == "Memberships" 
          print("TC_PIM_04 : Employee details successfully validated i.e.Personal Details, Contact Details, Emergency Contacts, Dependents, Immigration, Job, Salary, Tax Exemptions, Report-to, Qualifications, Memberships tabs are present")
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
          self.driver.close()


      def test_TC_PIM_05_update_personal_details(self, booting_function): #Updating Employee Personal Details page post User Creation
  
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
          self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
          self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
          sleep(2)
          self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
          sleep(2)           
          self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
          sleep(2)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().otherid).send_keys(12*Keys.BACKSPACE)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().otherid).send_keys(data.Ohrm_data().other_id)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().licence_number).send_keys(12*Keys.BACKSPACE)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().licence_number).send_keys(data.Ohrm_data().dr_license_number)           
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().expiry_date).send_keys(20*Keys.BACKSPACE)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().expiry_date).send_keys(data.Ohrm_data().license_exp_date)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().ssnnumber).send_keys(12*Keys.BACKSPACE)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().ssnnumber).send_keys(data.Ohrm_data().ssn_number)          
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().sinnumber).send_keys(12*Keys.BACKSPACE)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().sinnumber).send_keys(data.Ohrm_data().sin_number)                                    
     
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().nation_dropdwn).click() 
          sleep(1)
          self.driver.find_element(by=By.XPATH, value = locators.Ohrm_locators.indian_drop_down).click()
          sleep(1)     
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().marital_status).click() 
          sleep(1)

          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().status_married).click()
          sleep(1)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().date_of_birth).send_keys(20*Keys.BACKSPACE)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().date_of_birth).send_keys(data.Ohrm_data().dob)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().gender).click()  
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().military_service).send_keys(4*Keys.BACKSPACE)                       
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().military_service).send_keys(data.Ohrm_data().military_service)    
          sleep(5)
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_button1).click()                                                                                                                       
          sleep(2)        
          assert self.driver.title ==  self.driver.title
          print("TC_PIM_05 - Employee personal detials successfully updated")
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
          self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
          self.driver.close()


      def test_TC_PIM_06_add_contact_detail(self, booting_function): #test_TC_PIM_06_add_contact_details filling contact details in pim module
         
            self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
            self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
            sleep(2)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
            sleep(2)           
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
            sleep(2)
            self .driver.find_element(by=By.LINK_TEXT, value=locators.Ohrm_locators().contact_detail).click() 
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().street).send_keys(data.Ohrm_data().street)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().street_name).send_keys(data.Ohrm_data().state_name)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().city).send_keys(data.Ohrm_data().city_name)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().state).send_keys(data.Ohrm_data().state_name)           
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().z_code).send_keys(data.Ohrm_data().zip_code)
            place=self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().country)
            place.click()
            drop_downvalue2=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down3).text
            if drop_downvalue2.__contains__("Indian"):
                  self.driver.execute_script("var a=arguments[0];a.innerHTML='Indian'",place)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().home).send_keys(data.Ohrm_data().home_number)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().moblie).send_keys(data.Ohrm_data().mobile_number)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().work).send_keys(data.Ohrm_data().work_name)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().work_mail).send_keys(data.Ohrm_data().work_mailid)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().other_mailid).send_keys(data.Ohrm_data().other_mail)        
            sleep(1)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_button2).click()      
            sleep(1)  
            assert self.driver.title ==  self.driver.title
            print("TC_PIM_06 :  Employee contact detials updated successfully")
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
            self.driver.close()


      def test_TC_PIM_07_add_emergency_contact (self,booting_function): #test_TC_PIM_07_add_emergency_contact 
            
            self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
            self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
            sleep(2)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
            sleep(2)           
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
            sleep(2)          
            self.driver.find_element(by=By.LINK_TEXT, value=locators.Ohrm_locators().emergency_contact).click()  
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().emergency_add).click()  
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().name).send_keys(data.Ohrm_data().name)
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().relationship).send_keys(data.Ohrm_data().relationship)                      
            sleep(3)
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().home_number).send_keys(data.Ohrm_data().home_telephone)           
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().mobile_number_1).send_keys(data.Ohrm_data().mobile_number_1)           
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().work_number_1).send_keys(data.Ohrm_data().work_number_1)           
            sleep(3)
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_button3).click()           
            assert self.driver.title ==  self.driver.title
            print("TC_PIM_07 : Employee emergency contact detials updated successfully")
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
            self.driver.close()

      def test_TC_PIM_08_add_dependents_details(self, booting_function): #test_TC_PIM_08_add_dependents_details

            self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
            self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
            sleep(2)
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
            sleep(2)           
            self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
            sleep(2)   

            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().dependents).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().dependent_add).click() 
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().dependent_name).send_keys(data.Ohrm_data().dependent_name)
            relative = self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().relationship_depend)
            relative.click()
            dropdown3=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
            if dropdown3.__contains__("Child"):
                  self.driver.execute_script("var a=arguments[0];a.innerHTML='Child'",relative)
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().dependent_dob).send_keys(data.Ohrm_data().dependent_dob)
            sleep(5)
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_button4).click()     
            assert self.driver.title ==  self.driver.title
            print("TC_PIM_08 :  Employee dependents contact detials updated successfully")
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
            self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
            self.driver.close()


      def test_TC_PIM_09_job_detail(self, booting_function):#Add Job details in pim module
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
           sleep(1)
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
           sleep(1)           
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().job).click()
           sleep(3)

           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().joined).send_keys(data.Ohrm_data().joined_date) 
           sleep(3)
           job_name=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().job_title)
           job_name.click()
           dropdown_value4=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if dropdown_value4.__contains__("QA Engineer"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='QA Engineer'",job_name)
           job_role=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().job_category)
           job_role.click()
           dropdown_value5=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if dropdown_value5.__contains__("Professionals"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Professionals'",job_role)
                   
           sub_name=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().sub_unit)
           sub_name.click()
           dropdown_value6=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if dropdown_value6.__contains__("Engineering"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Engineering'",sub_name)    
     
           area=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().location)
           area.click()
           dropdown_value7=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if dropdown_value7.__contains__("Texas R&D"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Texas R&D'",area)    
               
           employee_position=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_status)
           employee_position.click()
           dropdown_value8=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if dropdown_value8.__contains__("Full-Time Contract"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Full-Time Contract'",employee_position)
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_button5).click()
           assert self.driver.title ==  self.driver.title
           print("TC_PIM_09 : Employee job detials updated successfully")
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
           self.driver.close()


      def test_TC_PIM_10_TC_PIM_11_update_termination_jobactivation_details(self, booting_function):   #Update termination & activation details 
              
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
           #self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name2)
           sleep(1)
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
           sleep(1)           
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().job).click()  

           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().terminate_button).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().terminate_date).send_keys(data.Ohrm_data().terminate_date)          
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().terminate_reason).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().terminate_reason_select).click() 
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().term_note).send_keys(data.Ohrm_data().terminate_note)  
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_term).click() 
           sleep(15)
           #self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().cancel).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().terminate_button).click() 
           sleep(10)
           assert self.driver.title ==  self.driver.title
           print("TC_PIM_10 & TC_PIM_11 : Termination of job detials & Job activation details updated successfully")
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
           self.driver.close()


      def test_TC_PIM_12_update_salarydetails(self,booting_function): #update employee salary details
           
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
           sleep(2)
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
           sleep(2)           
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click()  
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().salary).click()
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().salary_add).click()           
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().salary_com).send_keys(data.Ohrm_data().salary_component)
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pay_dd).click()
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pay_mon).click() 
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().curr_dd).click() 
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().curr_val).click() 
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pay_amount).send_keys("5000")
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().direct_deposit).click() 
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().ac_number)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().ac_type)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().routing_number) 
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().routing_amount) 
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().ac_num_value).send_keys("202101011004569")
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().ac_click).click()
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().savings).click()
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().rou_num_val).send_keys("8525") 
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_amount).send_keys("5000")
           sleep(1)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_salary).click()
           sleep(3)
           assert self.driver.title ==  self.driver.title
           print("Test case 12 - Employee salary details updated Successfully")
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
           self.driver.close()


      def test_TC_PIM_13__income_tax_exemption(self,booting_function): #Update Tax exemption details
           
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().username_inputbox).send_keys(data.Ohrm_data.username)
           self.driver.find_element(by=By.NAME, value=locators.Ohrm_locators().password_inputbox).send_keys(data.Ohrm_data.password)  
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().Login_button).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().pim_module).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().employee_name1).send_keys(data.Ohrm_data().employee_name1)
           sleep(5)
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().search_button).click()      
           sleep(5)           
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().click_button).click()          
           self.driver.find_element(by=By.LINK_TEXT, value=locators.Ohrm_locators().tax).click() 
           sleep(5)
           source=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().federal_status)
           source.click()
           drop_downvalue14=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if drop_downvalue14.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",source) 

           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().tax_exemptions).send_keys(4*Keys.BACKSPACE)       
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().fendral_exemptions).send_keys(data.Ohrm_data().fit_exemption)
           state=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().state_income)
           state.click()
           drop_downvalue15=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if drop_downvalue15.__contains__("Washington"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='New York'",state)
           tax=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().state_status)
           tax.click()
           drop_downvalue16=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if drop_downvalue16.__contains__("Single"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Single'",tax)

           #self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().tax_exemptions).send_keys(1*Keys.BACKSPACE)     
           self .driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().tax_exemptions).send_keys(data.Ohrm_data().sit_exemption)
           unemployee=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().unemployee)
           unemployee.click()
           drop_downvalue17=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if drop_downvalue17.__contains__("Washington"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Washington'",unemployee)
           work=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().work_state)
           work.click()
           drop_downvalue18=self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().drop_down).text
           if drop_downvalue18.__contains__("Washington"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Washington'",work)  
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().save_button8).click()           

           assert self.driver.title ==  self.driver.title
           print("TC_PIM_13 : Tax exemption details updated successfully")

           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_dropdown).click()
           self.driver.find_element(by=By.XPATH, value=locators.Ohrm_locators().logout_button).click()
           self.driver.close()
           