rate_res = {'Andhra Pradesh': 7.59, 'Maharashtra': 7.30, 'Chandigarh': 7.30, 'Madhyapradesh': 8.20, 'Rajasthan': 6,
            'U.P': 6.20, 'Assam': 5, 'Bihar': 8, 'Delhi': 8.50, 'Gujarat': 7, 'Assam': 8.6, 'Haryana': 7}
rate_com = {'Andhra Pradesh': 13, 'Maharashtra': 14, 'Chandigarh': 9, 'Madhyapradesh': 12.30, 'Rajasthan': 9.40,
            'U.P': 9.20, 'Bihar': 9, 'Delhi': 8.50, 'Gujarat': 10, 'Assam': 12, 'Haryana': 9}
rate_ind = {'Andhra Pradesh': 16.5, 'Maharashtra': 17, 'Chandigarh': 11.89, 'Madhyapradesh': 18, 'Rajasthan': 13.20,
            'U.P': 12.20, 'Assam': 13, 'Bihar': 18, 'Delhi': 15, 'Gujarat': 17, 'Assam': 16, 'Haryana': 15}
state = input('Enter State:- ')
tariff_type = input('Enter Tariff Type:- ')
avg_unit = int(input('Enter Average Monthly Unit Consumption KWh :- '))

# conn_load=input('Enter conn load:- ')

def MAIN():
    if tariff_type == 'Residential':
        a_p_rate = {v for (k, v) in rate_res.items() if state == k}
        a_p_rate = list(a_p_rate)
        average_monthly = avg_unit * a_p_rate[0]
        system_recomm = avg_unit * 12 / 1450
        tree_saved = round(system_recomm * 30)
        print(f'AVERAGE MONTHLY BILL:- {average_monthly} INR ')
        print('KW SYSTEM RECOMMENDED :- ', system_recomm)
        print(f'YOUR CONTRIBUTION TO THE ENVIRONMENT :- {tree_saved} TREES ADDED')
        # return average_monthly,system_recomm,tree_saved

    elif tariff_type == 'Commercial':
        a_p_rate = {v for (k, v) in rate_com.items() if state == k}
        a_p_rate = list(a_p_rate)
        average_monthly = avg_unit * a_p_rate[0]
        system_recomm = avg_unit * 12 / 1450
        tree_saved = round(system_recomm * 30)
        print(f'AVERAGE MONTHLY BILL :- {average_monthly} INR ')
        print('KW SYSTEM RECOMMENDED :- ', system_recomm)
        print(f'YOUR CONTRIBUTION TO THE ENVIRONMENT :- {tree_saved} TREES ADDED')
        # return average_monthly,system_recomm,tree_saved

    elif tariff_type == 'Industrial':

        a_p_rate = {v for (k, v) in rate_ind.items() if state == k}
        a_p_rate = list(a_p_rate)
        average_monthly = avg_unit * a_p_rate[0]
        system_recomm = avg_unit * 12 / 1450
        tree_saved = round(system_recomm * 30)
        print(f'AVERAGE MONTHLY BILL :- {average_monthly} INR ')
        print('KW SYSTEM RECOMMENDED :- ', system_recomm)
        print(f'YOUR CONTRIBUTION TO THE ENVIRONMENT :-{tree_saved} TREES ADDED')
        # return average_monthly,system_recomm,tree_saved


MAIN()
