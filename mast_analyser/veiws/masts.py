from datetime import datetime
from pprint import pprint

"""
constructor class for list of mast objects. 

params: mast_list - list of mast objects

methods for each question.

"""
class Masts:
    def __init__(self, mast_list):
        self.mast_list = mast_list
    
    # method for question 1a - return list of sorted mast objects by rent 
    def sort_by_rent(self):
        sorted_masts = sorted(self.mast_list, key= lambda mast: mast.current_rent, reverse=True)  
        return sorted_masts

    # method for question 1b - return top five sorted mast objects
    def rent_top_five(self):
        sorted_masts = self.sort_by_rent()    
        return sorted_masts[:5]

    # method for question 2a - return filtered list of mast objects by lease years.
    def filter_by_lease_years(self, lease = 25):
        filtered_list = [mast for mast in self.mast_list if mast.lease_years == 25]     
        return filtered_list

    # method for question 2b - returns rent toal for self.mast_filtered_by_lease_years 
    def calculate_rent_total(self):
        mast_filtered_by_lease_years = self.filter_by_lease_years()
        rent_list = [mast.current_rent for mast in mast_filtered_by_lease_years]   
        total = sum(rent_list)
        return total

    # method for question 3a - returns a dictionary to console.
    # data is not normalised and varations for tenant names exist. This could be resolved programmatically,
    # but it would be wise to check with user as varience could be legitimate. In the real world I would get 
    # the user to tidy up data at source or user to correct CSV - normalising data seems to be outside scope for question.
    def get_masts_by_tenant(self):
        tenants = dict()
        for mast in self.mast_list:
            if mast.tenant_name not in tenants.keys():
                tenants[mast.tenant_name] = 1
            else:
                tenants[mast.tenant_name] += 1     
        return tenants

    # method for question 4a - returns filtered list of mast objects with date in range, converts lease start to correct format
    def get_masts_by_lease_range(self, start_date = '01 Jun 1999', end_date = '31 Aug 2007'):
        # create a list of masts, converting date strings to datetime objects 
        masts_filtered_by_date = [mast for mast in self.mast_list 
        if datetime.strptime(start_date, '%d %b %Y') <= datetime.strptime(mast.lease_start, '%d %b %Y' ) 
        if datetime.strptime(end_date, '%d %b %Y') >= datetime.strptime(mast.lease_start, '%d %b %Y') ]
        # format lease start date correctly for output
        for mast in masts_filtered_by_date:
            date_object = datetime.strptime(mast.lease_start, '%d %b %Y')
            mast.lease_start = datetime.strftime(date_object, '%d %m %Y')
        return masts_filtered_by_date

             

    

       

