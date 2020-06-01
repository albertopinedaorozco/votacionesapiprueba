# votacionesapiprueba

## Python + Django + Rest Framework

### Methods
- GET
- POST
- PUT 
- DELETE


| Entity  |Endpoint  | GET  | POST  | PUT | DELETE  |
| :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
|  Users | /api/v1/users/signup/  | - | Registra usuarios |  Nuevo usuario <br>{"username": "","first_name": "","last_name": "","email": "",  "numero_celular": "","direccion": "","municipio": "","foto": ""} | * Update user |  - |
|   | /users/:id  |  * Get user |  - | -  |  * Delete user |
|   |  /login |  - |  Login user <br>{'username':'', password:''}  | -  |  - |

*Required authentication
```
headers: {
	'Authorization': 'Token <token-generado-al user>',
	'Content-Type': 'application/json'
}
```

## Clone the project
```
git clone <url project>
```
## enter folder
```
cd <project folder>
```

## Run the project

### Install the project
```
pip install pipenv (Si no se encuentra instalado)
pipenv install django==3.0
```
### Execute de enviroment
```
pipenv shell
```
luego
```
python manage.py runserver
```

