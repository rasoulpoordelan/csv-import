# csv-import


## install requirment
for install requirment
```
pip install -r requirements.txt
```

## run
first run  
```
./import
```
after see [finish] run
```
./runwebapp
```


## why I choose this solution
for import data to memory in this app, I use python [csv] package because if I want to manipulate data we need this tool I other ways I can import it easily with another tool like dbcsv bulk importer or Panda and for saving data into DB it in this app I use Sqlalchemy because it's fast and DB agnostic, for DB I use SQLite because our data is very small,
for serving web app I use Flask  because it's fast and easy to use 
### todo
write test 
handle exception
write better DBHandler because it inserts one log but in the good logger, we should queue our log and after a will insert it in DB for better performance

