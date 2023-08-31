#locators.py

class Ohrm_locators :

#test_TC_PIM_01_search (Validation on the admin page)

    #OHRM login locators
    username_inputbox = 'username' #Tagname
    password_inputbox = 'password' #Tagname
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    search_inputbox = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    pim = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    leave = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    time = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    recruitment = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    myinfo = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    performance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    directory = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    password = '(//*[@type="password"])'
    confirm_button = '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]' 
    maintenance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    buzz = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a' 

    logout_dropdown = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i'
    logout_button = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

#test_TC_PIM_02_Drop_down_toggled (Validation of Page Headers – Drop Down on Admin Page)

    admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    user_management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    user = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'
    user_role = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    user_role_admin = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span'
    user_role_ESS = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/span'
    status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'
    status_enabled = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span'
    status_disabled = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]'

# test_TC_PIM_03_Create_new_employee (Adding a New Employee under PIM)
    
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_module = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    employee_firstname = 'firstName'  #Tagname
    employee_lastname = 'lastName'   #Tagname
    create_login = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'

    login_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    login_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    confirm_password = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
 
    save_1_button = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    save_2_button = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

#test_TC_PIM_04_Check_tab_details (checking tab details)

    employee_name1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    search_button = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    click_button = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'

    pers_details = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
    cont_details = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    emer_details = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]'
    depen_details = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]'
    immigration = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]'
    job = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]'
    salary = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]'
    tax_exemp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]'
    report_to = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]'
    qualifications = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]'
    memberships = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]'


#test_TC_PIM_05_update_personal_details (Updating Employee Personal Details page post User Creation)

   
    otherid = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    licence_number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    expiry_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    ssnnumber = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    sinnumber = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    nation_dropdwn = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i'
    # nationality_drop_down= '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    indian_drop_down = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]'
    marital_status = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    # "(//*[@class='oxd-select-text-input'])[2]"
    status_married = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form'
    # '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    date_of_birth = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    gender = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    military_service = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    save_button1 = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"


#test_TC_PIM_06_add_contact_details

    contact_detail ='Contact Details'
    street ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    street_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    city = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    state = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    z_code = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    country = "(//*[@class='oxd-select-text-input'])"
    drop_down3 = "//*[@role='listbox']"     #country drop-down Xpath
    home = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'     #home number Xpath
    moblie = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    work = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    work_mail ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    other_mailid = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
    save_button2 = "(//*[@type='submit'])"

#test_TC_PIM_07_add_emergency_contact 

    emergency_contact = 'Emergency Contacts'
    emergency_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'     #name of emergency contact Xpath
    relationship = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'     #relationship of emergency contact Xpath
    home_number =   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    mobile_number_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    work_number_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    save_button3 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

#test_TC_PIM_08_add_dependents_details

    dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    dependent_add = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button"
    dependent_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    relationship_depend = "(//*[@class='oxd-select-text-input'])"
    dependent_dob = '(//*[@placeholder="yyyy-mm-dd"])'
    save_button4 = '(//*[@type="submit"])'

#test_TC_PIM_09_job_detail

    job = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    joined = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    job_title = "(//*[@class='oxd-select-text-input'])[1]"
    job_category = "(//*[@class='oxd-select-text-input'])[2]"
    sub_unit = "(//*[@class='oxd-select-text-input'])[3]"
    location = "(//*[@class='oxd-select-text-input'])[4]"
    drop_down = "//*[@role='listbox']"
    employee_status = "(//*[@class='oxd-select-text-input'])[5]"
    save_button5 = '(//*[@type="submit"])'

#test_TC_PIM_10_TC_PIM_11_update_termination_jobactivation_details

    terminate_button = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    terminate_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    terminate_reason = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]'
    terminate_reason_select = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[2]/div[2]'
    term_note = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea'
    save_term = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'
    # #cancel = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[1]'  

#test_TC_PIM_12_update_salarydetails

    salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    salary_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    salary_com = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    curr_dd = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    curr_val = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]'
    pay_dd = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
    pay_mon = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]'
    pay_amount = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    direct_deposit = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    ac_number = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[1]/label'
    ac_type = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[1]/label'
    routing_number = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/label'
    routing_amount = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[1]/label'
    ac_num_value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    ac_click = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div'
    savings = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]'
    rou_num_val = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    pim_amount = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    save_salary = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'


#test_TC_PIM_13__income_tax_exemption

    tax = 'Tax Exemptions'
    federal_status = "(//*[@class='oxd-select-text-input'])[1]"
    drop_down = "(//*[@role='listbox'])"
    fendral_exemptions = '(//*[@class="oxd-input oxd-input--active"])[2]'
    state_income = "(//*[@class='oxd-select-text-input'])[2]"
    state_status = "(//*[@class='oxd-select-text-input'])[3]"
    tax_exemptions = '(//*[@class="oxd-input oxd-input--active"])[3]'
    unemployee = "(//*[@class='oxd-select-text-input'])[4]"
    work_state = "(//*[@class='oxd-select-text-input'])[5]"
    save_button8 = "(//*[@type='submit'])"
