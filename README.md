# csv-import



## Install requirment
for install requirment you need python3 and pip
```
pip install -r requirements.txt
```

## Run
first run  
```
./import
```
after see [finish] run
```
./runwebapp
```
## Why I choose this solution
### import data to memory
for import data to memory in this app, I use python [csv] package because if I want to show how we can manipulate data and for better performance it's better use sql bulk insert
##### Other ways
dbcsv bulk importer or Panda 
### Save data in DB
for saving data into DB it in this app I use Sqlalchemy because it's fast and DB agnostic
### DB
SQLite because our data is very small,
### Serving data 
Flask because it's fast and easy to use

### todo
##### write test 
##### handle exception
##### write better DBHandler
becuase it's insert one log but i good logger we should queue our log and after i will insert it in db for better performance

