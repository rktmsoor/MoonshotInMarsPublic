import pandas
import os
from faker import Factory
import random,string
#import datetime
from datetime import datetime
from faker.providers import address
import csv
import numpy as np

faker = Factory.create()
faker.add_provider(address)

acc_actv = 'Y,N'.split(',')
status = 'open,close'.split(',')
business_cd='abc,bbc,cbc,dbc,ebc,fbc,gbc,hbc,ibc,jbc,kbc,lbc'.split(',')
line_of_business='retail,investment,corporate,highNetworth'.split(',')
clnt_role='holder,beneficiary,signatory'.split(',')
gender='Male,Female,NA'.split(',')
branch='CHPL,bombay,delhi,bangalore,madras'.split(',')
sec_typ_nm='stocks,mutualfund,derivatives,currency'.split(',')
to_client_id='101,201,301,401,501'.split(',')

filename="C:\\RAKTIM\\acc.csv"
filename_clntAcc="C:\\RAKTIM\\clntAcc.csv"
filename_clnt="C:\\RAKTIM\\clnt.csv"
filename_rev="C:\\RAKTIM\\rev.csv"
filename_bal="C:\\RAKTIM\\bal.csv"
filename_secrty="C:\\RAKTIM\\sec.csv"
filename_psn="C:\\RAKTIM\\psn.csv"
filename_tran="C:\\RAKTIM\\tran.csv"
filename_clntstructrel="C:\\RAKTIM\\clntstructrel.csv"

if os.path.exists(filename):
    os.remove(filename)
	
if os.path.exists(filename_clntAcc):
    os.remove(filename_clntAcc)
	
if os.path.exists(filename_clnt):
    os.remove(filename_clnt)
	
if os.path.exists(filename_rev):
    os.remove(filename_rev)

if os.path.exists(filename_bal):
    os.remove(filename_bal)
	
if os.path.exists(filename_secrty):
    os.remove(filename_secrty)

if os.path.exists(filename_psn):
	os.remove(filename_psn)
	
if os.path.exists(filename_tran):
    os.remove(filename_tran)
	
if os.path.exists(filename_clntstructrel):
    os.remove(filename_clntstructrel)
	
np.random.seed(1000)	
def date_between(d1, d2):
    f = '%b%d-%Y'
    return faker.date_time_between_dates(datetime.strptime(d1, f), datetime.strptime(d2, f))

def fakerecord():
    return {'acc_unique_id': np.random.randint(100000),  # random number eg:235533
            'bus_cd': random.choice(business_cd),  # choice of business code
            'name': faker.first_name(),  # different name
            'dt_opened':date_between('mar01-2015', 'mar15-2015') ,  # open date
            'dt_closed': date_between('mar01-2018', 'mar15-2019'),  # close date
            'line_of_bus_cd': random.choice(line_of_business),  # line of business
			'stat_cd': random.choice(status),
			'clnt_unique_id': faker.numerify('#####'),
			'brnch_cd':random.choice(business_cd),
			'lng_nm':faker.name(),
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time':date_between('jan01-2019', 'mar10-2019') 
            
            }
			
def fakerecord_clnt():
    return {'clnt_id': 'CL' + faker.numerify('#####'),  # random number eg:235533
            'br_cd': random.choice(business_cd),  # choice of business code
            'clnt_unique_id': np.random.randint(10000),  # different name
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
    return {'sec_cd': np.random.randint(1000),  # random number eg:235533
            'bus_cd': random.choice(business_cd),  # choice of business code
            'validity_start_dt': date_between('jan01-2019', 'mar10-2019'),  # different name
            'sec_long_nm': '~~SEC' + faker.first_name(),  # open date
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
			
			
account_data = pandas.DataFrame([fakerecord() for _ in range(1000)],columns=['acc_unique_id','bus_cd','name','dt_opened','dt_closed','line_of_bus_cd','stat_cd','clnt_unique_id','brnch_cd','lng_nm','src_upd_time','rec_add_time','rec_upd_time'])#.to_csv(filename, sep=',', encoding='utf-8')

acc_unique_id=account_data[['acc_unique_id']]

#client_acc = pandas.DataFrame([fakerecord_clntAcc() for _ in range(1000)]).to_csv(filename_clntAcc, sep=',', encoding='utf-8')
client = pandas.DataFrame([fakerecord_clnt() for _ in range(1000)])#.to_csv(filename_clnt, sep=',', encoding='utf-8')

clnt_uqe_id = client[['clnt_unique_id']]
#print(newdf)

security = pandas.DataFrame([fakerecord_security() for _ in range(1000)])#.to_csv(filename_secrty, sep=',', encoding='utf-8')
sec_cd=security[['sec_cd']]


def fakerecord_clntAcc():
    return {#'acc_unique_id': faker.numerify('########'),  # random number eg:235533
            'bus_cd': random.choice(business_cd),  # choice of business code
            #'clnt_id': random.choice(newdf),  # different name
            'br_cd':random.choice(business_cd) ,  # open date
            'clnt_rl_id': faker.numerify('########'),  # close date
            'clnt_rl_nm': faker.first_name(),  # line of business
			'clnt_to_acc_is_actv': random.choice(acc_actv),
			'clnt_to_acc_strt_dt': date_between('mar01-2015', 'mar15-2015'),
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time':date_between('jan01-2019', 'mar10-2019') 
            
            }
			
			
def fakerecord_rev():
    return {'feed_dt':date_between('jan01-2018', 'dec31-2018') ,
			'fin_acc_unique_id':'TD',
			#'acc_unique_id':faker.numerify('########'),
			'bus_cd':random.choice(business_cd), 
			'acc_appl_id':'TD',
			'prod_lvl_1':'P1' + faker.numerify('##'),
			'prod_lvl_2':'P2' + faker.numerify('##'),
			'prod_lvl_3':'P3' + faker.numerify('##'),
			'prod_lvl_4':'P4' + faker.numerify('##'),
			'prod_lvl_5':'P5' + faker.numerify('##'),
			#'clnt_unique_id':faker.numerify('#####'),
			'bac_code':'TD',
			'fin_data_typ':'TD',
			'rev_year_month':'2016',
			'revenue_amt':faker.numerify('######'),
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time': date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time': date_between('jan01-2019', 'mar10-2019') 

			
            }
			
def fakerecord_bal():
    return {'feed_dt':date_between('jan01-2018', 'dec31-2018') ,
			'fin_acc_unique_id':'TD',
			#'acc_unique_id':faker.numerify('########'),
			'bus_cd':random.choice(business_cd), 
			'acc_appl_id':'TD',
			'prod_lvl_1':'P1' + faker.numerify('##'),
			'prod_lvl_2':'P2' + faker.numerify('##'),
			'prod_lvl_3':'P3' + faker.numerify('##'),
			'prod_lvl_4':'P4' + faker.numerify('##'),
			'prod_lvl_5':'P5' + faker.numerify('##'),
			#'clnt_unique_id':faker.numerify('#####'),
			'bac_code':'TD',
			'rev_year_month':'201601',
			'avg_balance':faker.numerify('######'),
			'revenue_amt':faker.numerify('######'),
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time': date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time': date_between('jan01-2019', 'mar10-2019') 

			
            }	
			
def fakerecord_psn():
    return {'bus_cd' : random.choice(business_cd),
			'psn_dt' : date_between('jan01-2017', 'dec31-2017'),
			#'acc_unique_id': faker.numerify('########'),
			#'sec_cd' : faker.numerify('###'),
			'psn_trd_qty' : faker.numerify('######'),
			'psn_sett_qty' : faker.numerify('######'),
			'psn_mkt_pr': faker.numerify('###'),
			'psn_trd_cost_amt': faker.numerify('######'),
			'psn_trd_mkt_val_amt' : faker.numerify('######'),
			'psn_sett_mkt_val_amt' : faker.numerify('######'),
			'psn_net_mkt_val_amt' : faker.numerify('######'),
			'psn_trd_accr_income_amt' : faker.numerify('######'),
			'psn_sett_accr_income_amt' : faker.numerify('######'),
			'psn_trd_unrealized_gn_ls_amt' :faker.numerify('######'),
			'psn_trd_urrealized_gn_ls_amt' :faker.numerify('######'),
			'src_upd_time': date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time':  date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time':  date_between('jan01-2019', 'mar10-2019') 


            }
			
def fakerecord_trans():
    return {'bus_cd':random.choice(business_cd),
			'blot_cd':'Y',
			'tran_post_dt':date_between('jan01-2017', 'dec31-2017'),
			#'acc_unique_id':faker.numerify('########'), 
			#'sec_cd':faker.numerify('###'),
			'tran_unique_id':'TRAN'+faker.numerify('########'),
			'sec_cash_cd':'TD',
			'sec_cash_nm':'TD',
			'tran_traded_dt':date_between('jan01-2016', 'dec31-2016'),
			'tran_sett_dt':date_between('jan01-2016', 'dec31-2016'),
			'src_tran_stat_cd':'TD',
			'tran_stat_cd':'TD',
			'tran_cancel_in':random.choice(acc_actv),
			'tran_rev_in':'TD',
			'src_tran_typ_cd':'TD',
			'tran_typ_cd':'TD',
			'tran_typ_nm':'TD',
			'tran_amt':faker.numerify('########'), 
			'forex_rt':'TD',
			'tran_gross_amt':faker.numerify('########'), 
			'tran_price':faker.numerify('########'), 
			'tran_net_amt':faker.numerify('########'), 
			'tran_prn_cash_amt':faker.numerify('########'), 
			'tran_income_cash_amt':faker.numerify('########'), 
			'tran_mkt_val_amt':faker.numerify('########'), 
			'tran_accr_intr_amt':faker.numerify('########'), 
			'tran_gain_loss_amt':faker.numerify('########'), 
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time': date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time': date_between('jan01-2019', 'mar10-2019') 



            }
			
def fakerecord_clntstructrel():
    return {#'clnt_id':faker.numerify('#####'),
			'br_cd':random.choice(business_cd),
			'booking_br_nm':random.choice(business_cd),
			'from_clnt_in':'Y',
			'primary_rel_in':'Y',
			'clnt_rel_type_cd':'TD',
			'clnt_rel_type_nm':'TD',
			'role_rel_type_cd':'TD',
			'role_rel_type_nm':'TD',
			'from_clnt_role_id':'0',
			'from_clnt_role_nm':'client',
			'to_clnt_role_id':'1',
			'to_clnt_role_nm':'cost center',
			'role_rel_start_dt':date_between('jan01-2019', 'mar10-2019'),
			'to_clnt_id':random.choice(to_client_id),
			'to_br_cd':'TD',
			'src_upd_time':date_between('jan01-2019', 'mar10-2019') ,
			'rec_add_time': date_between('jan01-2019', 'mar10-2019') ,
			'rec_upd_time': date_between('jan01-2019', 'mar10-2019') 
			
            }
			
client_acc = pandas.DataFrame([fakerecord_clntAcc() for _ in range(1000)])#.to_csv(filename_clntAcc, sep=',', encoding='utf-8')
final_clntAccRel = pandas.concat([acc_unique_id,client_acc, clnt_uqe_id], axis=1).to_csv(filename_clntAcc, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)
#client_acc=pandas.concat([acc_unique_id, result], axis=1).to_csv(filename_clntAcc, sep=',', encoding='utf-8')
rev_data=pandas.DataFrame([fakerecord_rev() for _ in range(10000)])#.to_csv(filename_rev, sep=',', encoding='utf-8')
final_rev = pandas.concat([acc_unique_id,client_acc, rev_data], axis=1).to_csv(filename_rev, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)
bal_data=pandas.DataFrame([fakerecord_bal() for _ in range(10000)])#.to_csv(filename_bal, sep=',', encoding='utf-8')
final_bal= pandas.concat([acc_unique_id,client_acc, bal_data], axis=1).to_csv(filename_bal, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)

#####Position dataframe
position=pandas.DataFrame([fakerecord_psn() for _ in range(1000)])#.to_csv(filename_psn, sep=',', encoding='utf-8')
final_position= pandas.concat([acc_unique_id,position, sec_cd], axis=1).to_csv(filename_psn, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)


#####Transaction
transaction=pandas.DataFrame([fakerecord_trans() for _ in range(10000)])#.to_csv(filename_tran, sep=',', encoding='utf-8')
transaction_final=pandas.concat([acc_unique_id,transaction, sec_cd], axis=1).to_csv(filename_tran, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)

clntstructrel=pandas.DataFrame([fakerecord_clntstructrel() for _ in range(10000)])#.to_csv(filename_clntstructrel, sep=',', encoding='utf-8')
clntstructrel_final=pandas.concat([clnt_uqe_id,clntstructrel], axis=1).to_csv(filename_clntstructrel, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)

client.to_csv(filename_clnt, sep=',', encoding='utf-8',index=False, quoting=csv.QUOTE_NONNUMERIC)
account_data.to_csv(filename, sep=',', encoding='utf-8', index=False, quoting=csv.QUOTE_NONNUMERIC)
security.to_csv(filename_secrty, sep=',', encoding='utf-8', index=False, quoting=csv.QUOTE_NONNUMERIC)
