from app.app import App

mast_analyser = App()

mast_analyser.sort_by_rent()
mast_analyser.rent_top_five()

mast_analyser.filter_by_lease_years()
mast_analyser.caluculate_total_rent()



