from pprint import pprint
from functools import reduce

"""
constructor class for list of mast objects

"""
class Masts:
    def __init__(self, mast_list):
        self.mast_list = mast_list
        self.mast_filtered_by_lease_years = []
    
    # method for question 1a - return list of sorted mast objects by rent 
    def sort_by_rent(self):
        sorted_masts = sorted(self.mast_list, key= lambda mast: mast.current_rent, reverse=True)  
        return sorted_masts

    # method for question 1b - return top five sorted mast objects and print name + rent
    def rent_top_five(self):
        sorted_masts = self.sort_by_rent()
        for mast in sorted_masts[:5]:
            print("Mast name: {}, Rent: {}".format(mast.name, mast.current_rent))
        return sorted_masts[:5]

    # method for question 2a - return filtered list of mast objects by lease years. Use of list comprehension.
    def filter_by_lease_years(self, lease = 25):
        filtered_list = [mast for mast in self.mast_list if mast.lease_years == 25]
        # using pprint(vars()) to avoid as statement like print("Mast name: {}, Address: {}, ...".format(1, 2, ...))
        # prints attributes of object to console.
        for mast in filtered_list:
            pprint(vars(mast))

        self.mast_filtered_by_lease_years = filtered_list      
        return filtered_list
    # method for question 2b - returns rent toal for self.mast_filtered_by_lease_years 
    def calculate_rent_total(self):
        # attempted to use reduce to no avail :(
        # total = reduce(lambda accumulator, mast:  accumulator + mast.current_rent , filtered_list)
        rent_list = []
        for mast in self.mast_filtered_by_lease_years:
            rent_list.append(mast.current_rent)
        total = sum(rent_list)
        print("Total rent for all items in list: {}".format(total))
        return total
    # method for question 3a - returns a dictionary to console.
    # data is not normalised and varations for tenant names exist. This could be resolved programmatically,
    # but it would be wise to check with user as varience could be legetimate. In the real world I would get 
    # the user to tidy up data at source or correct CSV - normalising data seems to be outside scope for question.
    def get_masts_by_tenant(self):
        tenants = dict()
        for mast in self.mast_list:
            if mast.tenant_name not in tenants.keys():
                tenants[mast.tenant_name] = 1
            else:
                 tenants[mast.tenant_name] += 1
        print(tenants)
        return tenants            

    

       

