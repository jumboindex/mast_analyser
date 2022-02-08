import csv
import os
from veiws.mast_constructor import Mast

"""
Read csv file relative to current directory and returns CSV class, 
with each row being a dictionary. Create new mast object for each dictionary so 
data can updated to int / float.

params: none
returns: list of mast objects


"""
def load_csv():
    working_directory = os.getcwd()
    path_to_csv = working_directory + "\mast_analyser\data\Python Developer Test Dataset.csv"

    ##dirname = os.path.dirname(__file__)
    ##path_to_csv_1 = dirname + "\data\Python Developer Test Dataset.csv"
    mast_list = []
    ## validate path
    path_valid = os.access(path_to_csv, os.R_OK)
    
    if path_valid:
        with open(path_to_csv, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for mast in reader:
                    new_mast = Mast(mast['Property Name'],
                                    mast['Property Address [1]'],
                                    mast['Property  Address [2]'],
                                    mast['Property Address [3]'],
                                    mast['Property Address [4]'],
                                    mast['Unit Name'],
                                    mast['Tenant Name'],
                                    mast['Lease Start Date'],
                                    mast['Lease End Date'],
                                    mast['Lease Years'],
                                    mast['Current Rent'])
                    mast_list.append(new_mast)

        return mast_list
    else:
        raise Exception('file path is not valid!')                

