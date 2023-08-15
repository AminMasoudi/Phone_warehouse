# Phone_warehouse


## Usage:
 - build a `mariadb.cnf`
 - start mariadb with `sudo systemctl start mariadb.service`
 - create database `phones`
 - install requirements with `pip install -r req.pip`
 - migrate the tables to database with `./mmanage.py migrate`
 - and run server with `./manage.py runserver`
 - register in `http://127.0.0.1:8000/register/`
 - see swagger documentation in `/swagger/`

## TODO:
- [ ] add TestCases
- [ ] Add DOcker
- [ ] Add Docker-compose and mysql iso
- [ ] Add price to table in `/new_phone/`
- [ ] Set Debug = False :))
- [ ] publish a version :))
