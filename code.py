# pip install gettmpmail a-pandas-ex-dillpickle
from gettmpmail import get_tmp_email
from PrettyColorPrinter import add_printer
from a_pandas_ex_dillpickle import pd_add_dillpickle
pd_add_dillpickle()
add_printer(1)
df = get_tmp_email(n=3, timeout=5)
print(df)
# check email
# df.loc[df.aa_email=='micherladarochagois@internetkeno.com'].aa_checkmail.iloc[0]()

# salvar emails
# df.to_dillpickle('c:\\testemail.pkl')

# carregar emails
# df=pd.read_pickle(r'c:\testemail.pkl')
