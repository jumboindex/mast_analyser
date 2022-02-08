from helpers.csv_reader import load_csv
from veiws.masts import Masts

file = load_csv()
mast_list = Masts(file)

class App:
    def sort_by_rent(self):
        return mast_list.sort_by_rent()

    def rent_top_five(self):
        return mast_list.rent_top_five()        

    def filter_by_lease_years(self):
        return mast_list.filter_by_lease_years()

    def caluculate_total_rent(self):
        return mast_list.calculate_rent_total() 

    def get_tenant_count(self):
        return mast_list.get_masts_by_tenant()
    
    def get_masts_by_lease_range(self):
        return mast_list.get_masts_by_lease_range()    