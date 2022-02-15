class POM:
    
    #HarcodedValues as Names or urls
    URL = 'https://www.way2automation.com/angularjs-protractor/webtables/'
    FIRSTNAME = 'ER'
    LASTNAME = 'Test'
    USERNAME = 'TestER'
    PASSWORD = 'QATEST'
    EMAIL = 'test@test.com'
    CELLPHONE = '777888991'
    USER_NOVAK = 'novak'
    CUSTOMER = 'Company AAA'
    CREATE_BUTTON = 'button'
    ROLE = 'Sales Team'

    #Web Elements
    Table_Element = 'smart-table table table-striped'
    Btn_Create_User = 'btn btn-link pull-right'
    Btn_Delete_User = '//button[@ng-click="delUser()"]'
    Btn_Ok_Deletion = '//button[@class="btn ng-scope ng-binding btn-primary"]'
    Txt_Create_User_General_Class = 'ng-scope'
    Btn_Save_User = '//button[@class="btn btn-success"]'
    Txt_First_Name = '//input[@name="FirstName"]'
    Txt_Last_Name = '//input[@name="LastName"]'
    Txt_User_Name = '//input[@name="UserName"]'
    Txt_Password = '//input[@name="Password"]'
    Txt_Email = '//input[@name="Email"]'
    Txt_Cell_Phone = '//input[@name="Mobilephone"]'
    Rdb_Customer_Option = '//input[@name="optionsRadios"]' 
    Cmb_Role = '//option[@value="0"]'
    Main_Grid = '//tr[@ng-repeat="dataRow in displayedCollection"]'
    
