# API

A api está hospedada no Heroku:
https://ecodomo-api.herokuapp.com/

### Get /cupulas
Retorna um array com os nomes das cúpulas cadastradas

### Get /cupulas/\<cupula-id\>
Retorna um objeto com os atributos da cúpula
``` 
Exemplo: GET /cupulas/cupula_x
Response:  {
            "contact": {
                "cel": "819999999",
                "email": "fulana@detal.com",
                "name": "Fulana de Tal"
            },
            "cupula_id": "cupula_x",
            "location": {
                "address": "Av Jatobá",
                "city": "Petrolina",
                "name": "Escola Mãe Vitória",
                "state": "PE"
            },
            "name": "Cúpula X"
            }
```

### Get /cupulas/\<cupula-id\>/data
Retorna um objeto com os dados mais recentes monitorados da cúpula
``` 
Exemplo: GET /cupulas/cupula_x/data
Response:  {
            "date": "Tue, 30 Oct 2018 07:14:01 GMT",
            "humidity_env": "58.40",
            "humidity_soil": "22",
            "luminosity": "0.73",
            "temperature_env": "24.60",
            "temperature_soil": "24.81"
            }
```
