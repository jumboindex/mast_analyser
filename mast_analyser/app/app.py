from helpers.csv_reader import load_csv
from veiws.masts import Masts
from pprint import pprint

file = load_csv()
mast_list = Masts(file)

class App:

    def sort_by_rent(self):
        masts_sorted_by_rent = mast_list.sort_by_rent()
        highest_rent = masts_sorted_by_rent[0].current_rent
        lowest_rent = masts_sorted_by_rent[-1].current_rent
        return print("Masts sorted by rent. highest rent: {}, lowest rent: {}.".format(highest_rent, lowest_rent))

    def rent_top_five(self):
        top_five_masts = mast_list.rent_top_five()   
        return [print("Mast name: {}, Rent: {}".format(mast.name, mast.current_rent)) for mast in top_five_masts]

    def filter_by_lease_years(self):
        filtered_list = mast_list.filter_by_lease_years()
        return [pprint(vars(mast)) for mast in filtered_list]

    def caluculate_total_rent(self):
        total = mast_list.calculate_rent_total()
        return print("Total rent for all items in list: {}".format(total))

    def get_tenant_count(self):
        tenants = mast_list.get_masts_by_tenant()
        return [print(key,':',value) for key, value in tenants.items()]   
    
    def get_masts_by_lease_range(self):
        masts_filtered_by_date = mast_list.get_masts_by_lease_range()   
        return [print("Mast Name: {}, Lease Start Date: {}".format(mast.name, mast.lease_start))
        for mast in masts_filtered_by_date]