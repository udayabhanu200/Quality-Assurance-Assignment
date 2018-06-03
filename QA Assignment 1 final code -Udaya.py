# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:23:06 2018

@author: bhanu
"""


import xml.etree.ElementTree as ET                                  #importing XML parsing library
e = ET.parse('input1.xml').getroot()                                # parsing the input file named input1, it gives error if input file format is wrong
orderitems = e.findall('quantity')      
g = e.find('orderitems/item/partnumber').text                       #reading part number from XML
h = e.find('dealer/dealerid').text                                  #reading dealer id from XML
i = e.find('dealer/dealeraccesskey').text                           #reading dealer access key from XML 
j = e.find('deliveryaddress/postalcode').text                       #reading postal code from XML
k = e.find('deliveryaddress/province').text                         #reading province from XML
l = e.find('deliveryaddress/city').text                             #reading city from XML 
m = e.find('deliveryaddress/street').text                           #reading street from XML
n = e.find('deliveryaddress/name').text                         #reading name from XML
o= int(e.find('orderitems/item/quantity').text)                     #reading quantity from XML
partNumber = ['1111','2222','3333','12345']                               #Created mock array for part number
dealerID = ['1f1','2f2','3f3','4f4','XXX-1234-ABCD-1234']                 #Created mock array for dealer id
dealerAccess =['kkklas8882kk23nllfjj88290','sgsadfgdfg','sdgfafhsffghj']  #Created mock array for dealer access
postalCode =['B2T1A4','B3H3M5','B3H4R2']                                  #Created mock array for postal code
province=['NS','ON','NB']                                                 # Created mock for province
City=['Halifax','Toronto']                                                #Created mock for city
Street=['35 Streetname', 'Seymour street']                                #Created mock for street



class Order:                           #Created class named order to validate order details
    
    
    def show(elem):
        print(elem.tag)
        print(elem.text)
        for child in elem.findall('*'):
            show(child)

    # Dealer ID validation section 

    def dealerIDFail(self,h):                             # Security check function - Check if dealer id is valid - Failure case - input h from input xml file
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='failure'
        error = ET.SubElement(order, 'error')
        error.text = "Dealer not registered"              # format and content to write in output xml
        for dealer in dealerID:
            if (h != dealer):                             #input is h taken from input1 xml file, dealer from mock #comparing input dealer id with mock data and if not equal send failure
                response = open('dealerinvalid.xml', "wb")  # output xml file generated with name delaerinvalid     
                response.write(ET.tostring(order))
                response.close()

    def dealerIDSuccess(self,h):                         # Security check function - Check if dealer id is valid- Success case
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
    
        error = ET.SubElement(order, 'error')
        error.text = "Dealer registered"
    
        for dealer in dealerID:
            if (h == dealer):
                response = open('dealervalid.xml', "wb")
                response.write(ET.tostring(order))
                response.close()




    # Dealer Access ID validation section 

    def dealerauthorised(self,i):                        # Security check function - Check if dealer access is valid- Success case
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')           
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "Dealer Authorised"
    
        for access in dealerAccess:                      #access is dealer access id from mock of dealer access
            if (i == access):                            #input is i which is dealer access id from input xml
                response = open('dealerauthorised.xml', "wb")
                response.write(ET.tostring(order))
                response.close()  
                
    def dealerunauthorised(self,i):                     # Security check function - Check if dealer access is valid- Failure case
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "Dealer Authorised"
    
        for access in dealerAccess:
            if (i != access):
                response = open('dealerunauthorised.xml', "wb")
                response.write(ET.tostring(order))
                response.close()                




    # Part Number validation section

    def partnumberAvailable(self,g):                  #Check part number availability- Success case- Available
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "Available"
        for partno in partNumber:
            if (g == partno):
                response = open('partavailable.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
                print (g) 
                print(partno)
               



    def partnumberOutofstock(self,g):              #Check part number availability- Failure case- Out of stock
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Out of stock"
        for partno in partNumber:
            if (g != partno):
                response = open('partoutofstock.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
            
    def partnumberNoInput(self,g):                 #Check part number availability- Failure case- No input
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please give proper part number as input"
        if (g == ''):
            response = open('partnoinput.xml', "wb")
            response.write(ET.tostring(order))
            response.close()           
            
            
           
    def partnumberNotAvailable(self,g):         #Check part number availability- Failure case- Not available
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Not Available"
        for partno in partNumber:
              if (g != partno):
                  response = open('partnotavailable.xml', "wb")
                  response.write(ET.tostring(order))
                  response.close()
                  
  



                
    # Quantity validation section              
                  
    def QuantityFailEmpty(self,o):            # Check quantity input- Empty input case
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please enter the quantity of parts!"
        if (o == ''):
                response = open('quantityempty.xml', "wb")
                response.write(ET.tostring(order))
                response.close() 




    #Quantity and part number validation section                 
                  
    def partandquantitycheck(self,o,g):         #Check part number and quantity availability - Combination 
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "Your order is successful"
        for partno in partNumber:
            if (g == partno and o <= 30):
                response = open('pq.xml', "wb")
                response.write(ET.tostring(order))
                response.close()                  

    def partandquantitycheckfail(self,o,g):         #Check part number and quantity availability - Combination 
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Fail'
        error = ET.SubElement(order, 'error')
        error.text = "Quantity Not available"
        for partno in partNumber:
            if (g == partno and o <= 30):
                response = open('partquantitynotavailable.xml', "wb")
                response.write(ET.tostring(order))
                response.close()



    #Database interface validation section
    def dbinterface_fail(self,g):  #Database check- Fail case- Order data cannot be added to database
    
      order = ET.Element('order')
      result = ET.SubElement(order, 'result')
      result.text ='Failure'
      error = ET.SubElement(order, 'error')
      error.text = "Record cannot be added to database"
      for partno in partNumber:
            if (g != partno):
                response = open('dbfail.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
                
                
    def dbinterface_success(self,g):     #Database check- Success case- Order data can be added to database
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "Record added to database!"
        for partno in partNumber:
            if (g == partno):
                response = open('dbpass.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
                print (g)
                print(partno)
                

   #Delivery address validation section

    # Delivery address Postal code validation Section
    def XMLformatPostalCodeEmpty(self,j):          #Check postal code - Failure case- Empty input
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please enter a postal code"
        if (j == ''):
                response = open('postalcodeempty.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
        
    def XMLformatPostalCodeExist(self,j):         #Check postal code - Success case- Input matches with database mock
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "We deliver to this postal code"
        for postalcode in postalCode:
            if (j == postalcode):
                response = open('postalcodeexits.xml', "wb")
                response.write(ET.tostring(order))
                response.close()  
            
    def XMLformatPostalCodeNotExist(self,j):  #Check postal code - Failure case- Input doesn't matches with database mock
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Postal Code wrong or we dont deliver to this postal code"
        for postalcode in postalCode:
            if (j != postalcode and j !=''):
                response = open('postalcodedoesnotexist.xml', "wb")
                response.write(ET.tostring(order))
                response.close()            
      
    

   # Delivery address Province validation Section
                         
    def XMLformatProvinceEmpty(self,k):             #Check province - Failure case - Empty province
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please enter correct province"
        if (k == ''):
                response = open('provinceempty.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
                
    def XMLformatProvinceExist(self,k):          #Check province- Success case- Known province    
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "We deliver to this province"
        for p in province:
            if (k == p):
                response = open('provinceexists.xml', "wb")
                response.write(ET.tostring(order))
                response.close()  
            
    def XMLformatProvinceNotExist(self,k):    #Check province - Failure case - Wrong or unknown province
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Province wrong or we dont deliver to this province"
        for p in province:
            if (k != p and k !=''):
                response = open('provincenotexists.xml', "wb")
                response.write(ET.tostring(order))
                response.close()
 

    # Delivery address city validation Section           
    def XMLformatCityNotExist(self,l):        #Check city- Failure case - Wrong city- Not in mock database
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "City wrong or we dont deliver to this city"
        for c in City:
            if (l != c and l !=''):
                response = open('citynotexists.xml', "wb")
                response.write(ET.tostring(order))
                response.close()                
    
    
    def XMLformatCityExist(self,l):       #Check city- Success case - City exists in mock data
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "We deliver to this city"
        for c in City:
            if (l == c):
                response = open('cityexists.xml', "wb")
                response.write(ET.tostring(order))
                response.close()    


    def XMLformatCityEmpty(self,l):      #Check city- Failure case - Empty city
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please enter correct City"
        if (l == ''):
                response = open('cityempty.xml', "wb")
                response.write(ET.tostring(order))
                response.close()    

    # Delivery address street validation Section

    def XMLformatStreetNotExist(self,m):    # Check Street - Failure - Not in mock data
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Street wrong or we dont deliver to this city"
        for s in Street:
            if (m != s and m !=''):
                response = open('streetnotexists.xml', "wb")
                response.write(ET.tostring(order))
                response.close()                
    
    
    def XMLformatStreetExist(self,m): # Check Street - Success - Exists in mock data
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "We deliver to this street"
        for s in Street:
            if (m == s):
                response = open('streetexists.xml', "wb")
                response.write(ET.tostring(order))
                response.close()    


    def XMLformatStreetEmpty(self,m):# Check Street - Failure - Empty street name
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please enter correct Street"
        if (m == ''):
                response = open('streetempty.xml', "wb")
                response.write(ET.tostring(order))
                response.close()

    ## Delivery address Name validation Section
                
    def XMLformatNameEmpty(self,n):      #Check name  -Failure - empty name
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Failure'
        error = ET.SubElement(order, 'error')
        error.text = "Please enter the name for delivery!"
        if (n == ''):
                response = open('nameempty.xml', "wb")
                response.write(ET.tostring(order))
                response.close()                

    def XMLformatName(self,n):            #Check name  -Suucess - Name accepted if input is a string
    
        order = ET.Element('order')
        result = ET.SubElement(order, 'result')
        result.text ='Success'
        error = ET.SubElement(order, 'error')
        error.text = "Name Registered"
        if (type(n) == type('bhanu')):    #n is input- Checking if input is a string or not
                response = open('namevalid.xml', "wb")
                response.write(ET.tostring(order))
                response.close()               

                

                              
#Test the program by executing the functions 
#Outputs are generated and saved in the same location where script is saved                

d1 = Order()
d1.dealerIDFail(h)
d1.dealerIDSuccess(h)
d1.dealerauthorised(i)
d1.dealerunauthorised(i)
d1.partnumberAvailable(g)
d1.partnumberOutofstock(g)
d1.partnumberNotAvailable(g)
d1.partnumberNoInput(g)
d1.QuantityFailEmpty(o)
d1.partandquantitycheck(o,g)
d1.partandquantitycheckfail(o,g)
d1.dbinterface_fail(g)
d1.dbinterface_success(g)
d1.XMLformatPostalCodeEmpty(j)
d1.XMLformatPostalCodeExist(j)
d1.XMLformatPostalCodeNotExist(j)
d1.XMLformatProvinceEmpty(k)
d1.XMLformatProvinceExist(k)
d1.XMLformatProvinceNotExist(k)
d1.XMLformatCityNotExist(l)
d1.XMLformatCityExist(l)
d1.XMLformatCityEmpty(l)
d1.XMLformatStreetNotExist(m)
d1.XMLformatStreetExist(m)
d1.XMLformatStreetEmpty(m)
d1.XMLformatNameEmpty(n)
d1.XMLformatName(n)

