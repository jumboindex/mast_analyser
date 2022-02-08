"""
constructor class for list of mast objects

"""
class Masts:
    def __init__(self, mast_list):
        self.mast_list = mast_list
    
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
        

