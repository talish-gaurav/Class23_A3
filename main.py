
country_code = {"India" : "0091" , "Australia" : "0025", "UK" : "044"}
ui = input("Please enter which country's country code woulld you like to find (enter in lower case)")

print("The country code is : ", country_code.get(ui,"Not found"))