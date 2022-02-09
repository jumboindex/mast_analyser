import unittest
from mast_analyser.veiws.masts import Masts
from mast_analyser.helpers.csv_reader import load_csv

file = load_csv()
masts = Masts(file)

class TestApp(unittest.TestCase):

    def test_load_csv(self):

        #exercise - should throw Exception if file cannot be loaded.
        file = load_csv()
        # test file can be read and does not Exception('file path is not valid!') which unit test should catch.
        # probably a better way to test?     
        self.assertTrue

    def test_sort_by_rent(self):
        
        #setup
        list_length = 42
        highest_rent = 28327.09
        second_highest_rent = 23950.0
        lowest_rent = 6600.0
        second_lowest_rent = 9500.0

        #exercise
        sorted_list = masts.sort_by_rent()
        #check length
        sorted_list_length = len(sorted_list)
        # grab top two rent values
        result_highest_rent = sorted_list[0].current_rent
        result_second_highest_rent = sorted_list[1].current_rent
        #grab bottom two rent values
        result_lowest_rent = sorted_list[-1].current_rent
        result_second_lowest_rent = sorted_list[-2].current_rent

        #test
        self.assertEqual(sorted_list_length, list_length)
        self.assertEqual(result_highest_rent, highest_rent)
        self.assertEqual(result_second_highest_rent, second_highest_rent)
        self.assertEqual(result_lowest_rent, lowest_rent)
        self.assertEqual(result_second_lowest_rent, second_lowest_rent)

    def test_top_five_rent(self):

        #setup 
        list_length = 5
        rent_one = 28327.09
        rent_two = 23950.0
        rent_three = 22500.0
        rent_four = 17000.0
        rent_five = 17000.0

        #exercise
        top_five_masts = masts.rent_top_five()
        top_five_length = len(top_five_masts)
        # grab rent values
        result_rent_one = top_five_masts[0].current_rent
        result_rent_two = top_five_masts[1].current_rent
        result_rent_three = top_five_masts[2].current_rent
        result_rent_four = top_five_masts[3].current_rent
        result_rent_five = top_five_masts[4].current_rent

        #test
        self.assertEqual(list_length, top_five_length)
        self.assertEqual(rent_one, result_rent_one)
        self.assertEqual(rent_two, result_rent_two)
        self.assertEqual(rent_three, result_rent_three)
        self.assertEqual(rent_four, result_rent_four)
        self.assertEqual(rent_five, result_rent_five)

    def test_filter_by_lease_years(self):    

        #setup
        list_length = 4
        lease_years = 25

        #exercise
        filtered_list = masts.filter_by_lease_years()
        filtered_list_length = len(filtered_list)

        #test - check lease years = 25
        self.assertEqual(list_length, filtered_list_length)
        self.assertEqual(filtered_list[0].lease_years, lease_years)
        self.assertEqual(filtered_list[1].lease_years, lease_years)
        self.assertEqual(filtered_list[2].lease_years, lease_years)
        self.assertEqual(filtered_list[3].lease_years, lease_years)

    def test_caculate_rent_total(self):

        #setup
        total = 46500

        #exercise
        #calculate total
        result = masts.calculate_rent_total()

        #test - check total is correct
        self.assertEqual(result, total)

    def test_get_tenant_count(self):

        #setup
        cornerstone_key = "Cornerstone Telecommunications Infrastructure"
        cornerstone_count = 16
        everything_anywhere_key = "Everything Everywhere Ltd"
        everything_anywhere_count = 4
        vodafone_key = "Vodafone Ltd."
        vodafone_count = 1

        #exercise 
        result = masts.get_masts_by_tenant()    
       
        cornerstone_count_result = result[cornerstone_key]
        everything_anywhere_result = result[everything_anywhere_key]
        vodafone_result = result[vodafone_key]
        list_of_keys = result.keys()

        #test - check selection of values are in dict
        self.assertIn(cornerstone_key, list_of_keys)
        self.assertIn(everything_anywhere_key, list_of_keys)
        self.assertIn(vodafone_key, list_of_keys)
        self.assertEqual(cornerstone_count, cornerstone_count_result)
        self.assertEqual(everything_anywhere_count, everything_anywhere_result)
        self.assertEqual(vodafone_count, vodafone_result)

    def test_get_masts_in_date_range(self):
        
        #setup
        list_length = 5
        first_lease_start_date = "24 06 1999"
        last_lease_start_date = "21 08 2007"

        #exercise 
        result = masts.get_masts_by_lease_range()
        result_length = len(result)
        result_first_lease_start_date = result[0].lease_start
        result_last_lease_start_date = result[4].lease_start

        #test - check length and first / last date are correct
        self.assertEqual(list_length, result_length)
        self.assertEqual(first_lease_start_date, result_first_lease_start_date)
        self.assertEqual(last_lease_start_date, result_last_lease_start_date)


if __name__ == '__main__':
    unittest.main()
