# Backend Django Rest API héberge sur Heroku

## API pour la gestion des Conférences :

### URL de base de l'API :

```http
https://emsi-django-backend.herokuapp.com/api/
```

### I - Gestion Conférences :

#### 1 - Liste Conférences ( Request Method: GET ) :

```http
https://emsi-django-backend.herokuapp.com/api/conferences/
```
Format de Réponse Json :

```javascript

[
    {
        "id": 2,
        "titre": "Conf\u00e9rence 1",
        "description": "Conf\u00e9rence 1",
        "details": "Conf\u00e9rence 1",
        "date_debut": "2022-06-01",
        "date_fin": "2022-06-03",
        "frais": 150,
        "amphi": 1,
        "conferencier": 2
    },
    {
        "id": 3,
        "titre": "Conf\u00e9rence 3",
        "description": "Conf\u00e9rence 3",
        "details": "Conf\u00e9rence 3",
        "date_debut": "2022-07-11",
        "date_fin": "2022-07-13",
        "frais": 120,
        "amphi": 5,
        "conferencier": 4
    }
]

```
####  2 - Ajouter Conférence (Request Method: POST) :

```http
https://emsi-django-backend.herokuapp.com/api/conferences/
```

Format de données envoyés en Json :

```javascript
{
    "titre": "Conférence 3",
    "description": "Conférence 3",
    "details": "Conférence 3",
    "date_debut": "2022-08-10",
    "date_fin": "2022-08-13",
    "frais": "250"
}
```

####  3 - Modifier Conférence (Request Method: PUT) :

```http
https://emsi-django-backend.herokuapp.com/api/conferences/[id_conference]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_conference` | `entier` | **Required**. Id conférence à modifié |

```javascript
{
 "id": 3,
    "titre": "Conférence 3",
    "description": "Conférence 3",
    "details": "Conférence 3",
    "date_debut": "2022-08-10",
    "date_fin": "2022-08-13",
    "frais": "250",
    "amphi": 5,
    "conferencier": 4
}
```



#### 4 - Supprimer Conférence (Request Method: DELETE) :

```http
https://emsi-django-backend.herokuapp.com/api/conferences/[id_conference]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_conference` | `entier` | **Required**. Id conférence à supprimé |


### II - Gestion Participants :

#### 1 - Liste Participants ( Request Method: GET ) :


```http
https://emsi-django-backend.herokuapp.com/api/participants/
```

Format de Réponse Json :

```javascript
[
    {
        "id": 1,
        "nom": "Achrafi",
        "prenom": "Achraf",
        "cin": "GH589632",
        "telephone": "0619740790",
        "email": "emaildevtesttest@gmail.com",
        "type": "Conferencier"
    },
    {
        "id": 2,
        "nom": "M'RHARY",
        "prenom": "FATIMA-EZ-ZAHRA",
        "cin": "T313098",
        "telephone": "0622322342",
        "email": "fatimaezahra.mrhary@gmail.com",
        "type": "Conferencier"
    }
]
```

####  2 - Ajouter participant (Request Method: POST) :

```http
https://emsi-django-backend.herokuapp.com/api/participants/
```

Format de données envoyés en Json :

```javascript
{
    "nom": "Rachid",
    "prenom": "Slimani",
    "cin": "bn215489",
    "telephone": "0652369874",
    "email": "rachid.slimani@test.com",
    "type": "Auditeur"
}
```

####  3 - Modifier participant (Request Method: PUT) :

```http
https://emsi-django-backend.herokuapp.com/api/participants/[id_participant]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_participant` | `entier` | **Required**. Id participant à modifié |

```javascript

{
    "id": 3,
    "nom": "Rachid",
    "prenom": "Slimani",
    "cin": "bn215489",
    "telephone": "0652369874",
    "email": "rachid.slimani@test.com",
    "type": "Auditeur"
}
```



#### 4 - Supprimer participant (Request Method: DELETE) :

```http
https://emsi-django-backend.herokuapp.com/api/conferences/[id_participant]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_participant` | `entier` | **Required**. Id participant à supprimé |

### II - Gestion Amphitheatres :

#### 1 - Liste Amphitheatres ( Request Method: GET ) :


```http
https://emsi-django-backend.herokuapp.com/api/amphitheatres/
```

Format de Réponse Json :

```javascript
[
    {
        "id": 1,
        "nom": "Amphi 1",
        "numero": 1,
        "capacite": 100,
        "cout": 100
    },
    {
        "id": 2,
        "nom": "Amphi2",
        "numero": 2,
        "capacite": 260,
        "cout": 198
    }
]
```

####  2 - Ajouter amphitheatre (Request Method: POST) :

```http
https://emsi-django-backend.herokuapp.com/api/amphitheatres/
```

Format de données envoyés en Json :

```javascript
    {
        "nom": "Amphi 3",
        "numero": 2,
        "capacite": 260,
        "cout": 198
    }
```

####  3 - Modifier amphitheatre (Request Method: PUT) :

```http
https://emsi-django-backend.herokuapp.com/api/amphitheatres/[id_amphitheatre]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_amphitheatre` | `entier` | **Required**. Id amphitheatre à modifié |

```javascript

 {
        "id": 2,
        "nom": "Amphi22",
        "numero": 22,
        "capacite": 260,
        "cout": 198
    }
```



#### 4 - Supprimer participant (Request Method: DELETE) :

```http
https://emsi-django-backend.herokuapp.com/api/amphitheatres/[id_amphitheatre]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_amphitheatre` | `entier` | **Required**. Id amphitheatre à supprimé |
