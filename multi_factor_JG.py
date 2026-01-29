# a213_multi_factor.py
import multifactorcli as mfc

# create a multi-factor interface to a restricted app
my_auth = mfc.MultiFactorAuth()

username = "jgdabest"
password = "01bowhueywhuey"
my_auth.set_authetication(username,password)

# set the users authentication information
question = "What is the name of the first shoes you got?"
answer = "sketchers"
my_auth.set_multiFactorAuthentication(question, answer)

my_auth.run()