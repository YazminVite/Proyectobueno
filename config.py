import web

db_host = 'qbct6vwi8q648mrn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'fx7novrrsm6m7371'
db_user = 'dfe1pqbjkj9umxut'
db_pw = 't51us79utfemtyfy'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
