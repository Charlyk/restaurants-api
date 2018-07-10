# Restayrants API documentation

#### Update spoken languages and location

Path: `/api/restaurants`

Method: `GET`

Parameters:

> `lat`: latitude as floating number
>
> `lng`: longitude as floating number
>
> `radius`: desired distance to the restaurant

Response example

```json
[
    {
        "id": 31,
        "name": "Pepe Pizza",
        "lat": 47.0181751445307,
        "lng": 28.836341947317123,
        "hour": 1,
        "website": "http://www.pepe-pizza.md",
        "photos": [
            {
                "prefix": "https://igx.4sqi.net/img/general/",
                "suffix": "/29842181_QNSD7_UrV0xpZyQ39PSC0NAMls5nC6A6lcrudNU4bEg.jpg",
                "width": 960,
                "height": 543
            }
        ]
    },
    {
        "id": 32,
        "name": "El Paso",
        "lat": 47.01430989789881,
        "lng": 28.831709657122445,
        "hour": 1,
        "website": "http://www.el-paso.md",
        "photos": [
            {
                "prefix": "https://igx.4sqi.net/img/general/",
                "suffix": "/14834011_PPP_pY9NQPvNrnzYw3yfJo49-S8v0DeE-s1kio5XJ3M.jpg",
                "width": 960,
                "height": 720
            }
        ]
    },
    {
        "id": 33,
        "name": "Chianti",
        "lat": 47.02020244777131,
        "lng": 28.834655153727383,
        "hour": 2,
        "website": "http://chianti.md",
        "photos": [
            {
                "prefix": "https://igx.4sqi.net/img/general/",
                "suffix": "/41278096_spJ7Rdk5htV6ja45Rll7wMQqp8xaj3k_kSb4OkP5RCo.jpg",
                "width": 720,
                "height": 480
            }
        ]
    }
]
```