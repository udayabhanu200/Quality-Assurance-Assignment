1. Script is in python - Used spyder from anaconda package to write the code.
2. Tried to cover all the mail scenarios.
3. Class is used to add all the unit tests.
4. Tests can be run using class objects.
5. Just need to change input xmls with different inputs and output xmls will be generated with response.
6. Every test has separate xml output.
7. TA needs to change input xml file to check the responses.
8. Lists of 27 test cases covered:
 1. 2 for dealer id - valid, invalid
 2. 2 for dealer access id- security - authorised, unauthorised
 3. 4 for part number - No input, Available, out of stock, Not available
 4. 2 for database interferance - Added to database, Cannot be added
 5. 1 for quantity - input empty
 6. 2 for part and quantity together - success for that part and quantity, quantity not avaiable
 7. 3 for postal code - empty, exists, not exists
 8. 3 for province - empty, exists, not exists
 9. 3 for city -empty, exists, not exists
 10.3 for street-empty, exists, not exists
 10.2 for name - Empty, valid

9. Instructions to run:
a) save input xml and code file in same folder.
c) change input file name in line 10 of code to check different conditions
b) outputs will be saved in the same folder with as names mentioned in code.

10. Didn't try combinations as list becomes huge and shown one sample for part number and quantity.

11. Response design is as follows
Sample response:
<?xml version="1.0"?>

-<order>

<result>failure</result>

<error>Part Not Available</error>

</order>

12. References:
Learnt to use python library for parsing from python documentation:
https://docs.python.org/3/library/xml.etree.elementtree.html
I have done the rest on my own.



