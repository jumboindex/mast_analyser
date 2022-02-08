import unittest
from app.app import App

app = App()

class TestApp(unittest.TestCase):

    def test_sort_by_rent(self):
        
        #setup
        list_length = 42
        highest_rent = 28327.09
        second_highest_rent = 23950.0
        lowest_rent = 6600.0
        second_lowest_rent = 9500.0

        #exercise
        sorted_list = app.sort_by_rent()
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
        top_five_masts = app.rent_top_five()
        top_five_length = len(top_five_masts)

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
        filtered_list = app.filter_by_lease_years()
        filtered_list_length = len(filtered_list)

        #test 
        self.assertEqual(list_length, filtered_list_length)
        self.assertEqual(filtered_list[0].lease_years, lease_years)
        self.assertEqual(filtered_list[1].lease_years, lease_years)
        self.assertEqual(filtered_list[2].lease_years, lease_years)
        self.assertEqual(filtered_list[3].lease_years, lease_years)

    def test_caculate_rent_total(self):

        #setup
        total = 46500

        #exercise
        #generate list 
        app.filter_by_lease_years()
        #calculate total
        result = app.caluculate_total_rent()

        #test
        self.assertEqual(result, total)


if __name__ == '__main__':
    unittest.main()
