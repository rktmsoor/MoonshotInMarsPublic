import pandas
import os
from faker import Factory
import random,string
#import datetime
from datetime import datetime
from faker.providers import address

faker = Factory.create()
faker.add_provider(address)

acc_actv = 'Y,N'.split(',')
status = 'open,close'.split(',')
business_cd='abc,bbc,cbc,dbc,ebc,fbc,gbc,hbc,ibc,jbc,kbc,lbc'.split(',')
line_of_business='retail,investment,corporate,highNetworth'.split(',')
clnt_role='holder,beneficiary,signatory'.split(',')
gender='Male,Female,NA'.split(',')
branch='calcutta,bombay,delhi,bangalore,madras'.split(',')
sec_typ_nm='stocks,mutualfund,derivatives,currency'.split(',')
filename="C:\\RAKTIM\\acc.csv"
filename_clntAcc="C:\\RAKTIM\\clntAcc.csv"
filename_clnt="C:\\RAKTIM\\clnt.csv"
filename_secrty="C:\\RAKTIM\\sec.csv"
def date_between(d1, d2):
    f = '%b%d-%Y'
    return faker.date_time_between_dates(datetime.strptime(d1, f), datetime.strptime(d2, f))

def fakerecord():
    return {'acc_unique_id': faker.numerify('########'),  # random number eg:235533
            'bus_cd': random.choice(business_cd),  # choice of business code
            'name': faker.first_name(),  # different name
            'dt_opened':date_between('mar01-2015', 'mar15-2015') ,  # open date
            'dt_closed': date_between('mar01-2018', 'mar15-2019'),  # close date
            'line_of_bus_cd': random.choice(line_of_business),  # line of business
			'stat_cd': random.choice(status),
			'clnt_unique_id': faker.numerify('#####'),
			'brnch_cd':random.choice(branch),
			'lng_nm':faker.name(),
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time':date_between('jan01-2019', 'mar10-2019') 
            
            }
			
def fakerecord_clntAcc():
    return {'acc_unique_id': faker.numerify('########'),  # random number eg:235533
            'bus_cd': random.choice(business_cd),  # choice of business code
            'clnt_id': faker.numerify('#####'),  # different name
            'br_cd':random.choice(branch) ,  # open date
            'clnt_rl_id': faker.numerify('########'),  # close date
            'clnt_rl_nm': faker.first_name(),  # line of business
			'clnt_to_acc_is_actv': random.choice(acc_actv),
			'clnt_to_acc_strt_dt': date_between('mar01-2015', 'mar15-2015'),
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time':date_between('jan01-2019', 'mar10-2019') 
            
            }
			
def fakerecord_clnt():
    return {'clnt_id': faker.numerify('#####'),  # random number eg:235533
            'br_cd': random.choice(branch),  # choice of business code
            'clnt_unique_id': faker.numerify('#####'),  # different name
            'pr_line_of_bus_cd': 'NA',  # open date
            'pr_line_of_bus_nm': 'NA' ,  # close date
            'clnt_fl_nm': faker.name(),  # line of business
			'clnt_online_in': random.choice(acc_actv),
			'del_in': random.choice(acc_actv),
			'clnt_first_name':faker.first_name() ,
			'clnt_last_name':faker.last_name() ,
			'city':faker.city() , 
			'country_cd' : faker.country_code() ,
			'country' : faker.country(),
			'dm_clnt_unique_id' : faker.numerify('#####'),
			'clnt_start_dt' : date_between('mar01-2015', 'mar15-2015'),
			'clnt_role_id' : random.choice(clnt_role),
			'clnt_role_nm' : random.choice(clnt_role),
			'clnt_gender_in' : random.choice(gender),
			'clnt_employer_name' : faker.company(),
			'clnt_city_of_birth' : faker.city(),
			'clnt_country_of_birth' : faker.country_code() ,
			'clnt_date_of_birth' : date_between('jan01-1970', 'mar10-1975'),
			'clnt_addr_1' : faker.address(),
			'clnt_addr_2' :faker.street_address(),
			'clnt_addr_3' :'NA',
			'clnt_postal_cd' : faker.zipcode(),
			'clnt_city_nm' : faker.city(),
			'clnt_country_cd' : faker.country_code(),
			'clnt_country_nm' : faker.country(),
			'src_upd_time' :date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time' :date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time' :date_between('jan01-2019', 'mar10-2019') 

            
            }
			
			
def fakerecord_security():
    return {'sec_cd': faker.numerify('###'),  # random number eg:235533
            'bus_cd': random.choice(business_cd),  # choice of business code
            'validity_start_dt': date_between('jan01-2019', 'mar10-2018'),  # different name
            'sec_long_nm': '~~SEC' + faker.name(),  # open date
            'sec_short_nm': faker.isbn10(separator="-") ,  # close date
            'sec_tic_cd': 'TD',  # line of business
			'sec_cus_cd': 'TD',
			'sec_isn_cd': faker.isbn10(separator="-"),
			'sec_vel_cd': faker.numerify('##'),
			'sec_issue_dt': date_between('jan01-2018', 'dec31-2018'),
			'sec_exp_dt': date_between('jan01-2018', 'dec31-2018'),
			'sec_stat_nm':  random.choice(status),
			'sec_typ_nm': random.choice(sec_typ_nm),
			'sac_lvl1_cd': faker.numerify('##'),
			'sac_lvl2_cd': faker.numerify('##'),
			'sac_lvl3_cd': faker.numerify('##'),
			'sec_create_dt': date_between('jan01-2019', 'mar10-2019'),
			'sec_maturity_dt': date_between('jan01-2019', 'mar10-2019'),
			'sec_inst_rt':'TD',
			'sec_tax_rt':'TD',
			'sec_comm_rt':'TD',
			'sec_fees_rt':'TD',
			'sec_base_rt':'TD',
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time':date_between('jan01-2019', 'mar10-2019') 

            }
			
def fakerecord_psn():
    return {bus_cd : random.choice(business_cd),
			psn_dt : date_between('jan01-2019', 'mar10-2019'),
			acc_unique_id: faker.numerify('########'),
			sec_cd : faker.numerify('###'),
			psn_trd_qty : faker.numerify('######'),
			psn_sett_qty : faker.numerify('######'),
			psn_mkt_pr: faker.numerify('###'),
			psn_trd_cost_amt: 
			psn_trd_mkt_val_amt :
			psn_sett_mkt_val_amt :
			psn_net_mkt_val_amt :
			psn_trd_accr_income_amt :
			psn_sett_accr_income_amt :
			psn_trd_unrealized_gn_ls_amt :
			psn_trd_urrealized_gn_ls_amt :
			src_upd_time: date_between('jan01-2019', 'mar10-2019') ,
			rec_add_time:  date_between('jan01-2019', 'mar10-2019') ,
			rec_upd_time:  date_between('jan01-2019', 'mar10-2019') 


            }

if os.path.exists(filename):
    os.remove(filename)
	
if os.path.exists(filename_clntAcc):
    os.remove(filename_clntAcc)
	
if os.path.exists(filename_clnt):
    os.remove(filename_clnt)
	
if os.path.exists(filename_secrty):
    os.remove(filename_secrty)
			
account_data = pandas.DataFrame([fakerecord() for _ in range(1000)],columns=['acc_unique_id','bus_cd','name','dt_opened','dt_closed','line_of_bus_cd','stat_cd','clnt_unique_id','brnch_cd','lng_nm','src_upd_time','rec_add_time','rec_upd_time']).to_csv(filename, sep=',', encoding='utf-8')

client_acc = pandas.DataFrame([fakerecord_clntAcc() for _ in range(1000)]).to_csv(filename_clntAcc, sep=',', encoding='utf-8')
client = pandas.DataFrame([fakerecord_clnt() for _ in range(1000)]).to_csv(filename_clnt, sep=',', encoding='utf-8')
security = pandas.DataFrame([fakerecord_security() for _ in range(1000)]).to_csv(filename_secrty, sep=',', encoding='utf-8')
# cols = account_data.columns.tolist()
# print(cols)
# account_data = account_data.reindex_axis(['acc_unique_id','bus_cd','name','dt_opened','dt_closed','line_of_bus_cd','stat_cd','clnt_unique_id','brnch_cd','lng_nm','src_upd_time','rec_add_time','rec_upd_time'], axis=1)
# #acc_col_order = [0,1,2,3,4,5,6,7,8,9,10,11,12]
# final_acc_data = account_data[account_data.columns[acc_col_order]].to_csv(filename, sep=',', encoding='utf-8')
# #df.to_csv(file_name, sep='\t', encoding='utf-8')