from helpers.csv_reader import load_csv
from veiws.masts import Masts
from pprint import pprint

file = load_csv()
mast_list = Masts(file)

"""
App contains all the print logic / user interaction via console.
This has been created to separate concerns and could also be used to handle errors.

"""

class App:

    def sort_by_rent(self):
        masts_sorted_by_rent = mast_list.sort_by_rent()
        highest_rent = masts_sorted_by_rent[0].current_rent
        lowest_rent = masts_sorted_by_rent[-1].current_rent
        print("Question 1a:")
        return print("Masts sorted by rent. highest rent: {}, lowest rent: {}.".format(highest_rent, lowest_rent))

    def rent_top_five(self):
        top_five_masts = mast_list.rent_top_five()
        print("Question 1b:")   
        return [print("Mast name: {}, Rent: {}".format(mast.name, mast.current_rent)) for mast in top_five_masts]

    def filter_by_lease_years(self):
        filtered_list = mast_list.filter_by_lease_years()
        print("Question 2a:")  
        return [pprint(vars(mast)) for mast in filtered_list]

    def caluculate_total_rent(self):
        total = mast_list.calculate_rent_total()
        print("Question 2b:")  
        return print("Total rent for all items in list: {}".format(total))

    def get_tenant_count(self):
        tenants = mast_list.get_masts_by_tenant()
        print("Question 3a:")  
        return [print(key,':',value) for key, value in tenants.items()]   
    
    def get_masts_by_lease_range(self):
        masts_filtered_by_date = mast_list.get_masts_by_lease_range()
        print("Question 4a:")     
        return [print("Mast Name: {}, Lease Start Date: {}".format(mast.name, mast.lease_start))
        for mast in masts_filtered_by_date]

    def run(self):
        user_input = input("Please enter question number i.e. 1a, or all for all questions. Type exit to exit: ").strip().lower()
        if user_input == "exit":
            exit()
        else:
            self.user_input(user_input)

    def user_input(self, user_input):

        match user_input:
            case "1a":
                self.sort_by_rent()
                return self.run()
            case "1b":
                self.rent_top_five()
                return self.run()
            case "2a":
                self.filter_by_lease_years()
                return self.run()
            case "2b":
                self.caluculate_total_rent()
                return self.run()
            case "3a":
                self.get_tenant_count()
                return self.run()
            case "4a":
                self.get_masts_by_lease_range()
                return self.run()
            case "all":
                self.sort_by_rent()
                self.rent_top_five()
                self.filter_by_lease_years()
                self.caluculate_total_rent()
                self.get_tenant_count()
                self.get_masts_by_lease_range()
                return self.run()
            case _:
                print("invalid input, try again!")
                return self.run()                          
