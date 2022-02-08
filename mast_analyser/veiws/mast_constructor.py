from datetime import datetime
"""
constructor class for indivdual masts to overcome data issues 

"""
class Mast:
    def __init__(self, name, address_1, address_2, address_3, address_4, 
                unit_name, tenant_name, lease_start, lease_end, lease_years, 
                current_rent):
        self.name = name
        self.address = "{0}, {1}, {2}, {3}".format(address_1, address_2, address_3, address_4)
        self.unit_name = unit_name
        self.tenant_name = tenant_name
        self.lease_start = lease_start
        self.lease_end = lease_end
        self.lease_years = int(lease_years)
        self.current_rent = float(current_rent)




""" self.lease_start = datetime.strptime(least_start, '%d %b %Y')
self.lease_end = datetime.strptime(lease_end, '%d %b %Y')         """