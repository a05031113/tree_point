# tree_point

## How to use?

1. Pull the image from docker hub

```
docker pull a05031113/tree_point
```

2. Run with port 3000

```
docker run -p 3000:3000 a05031113/tree_point
```

## APIs

- POST /api/user/add

```js
Request_body = {
    "data": {
        "username": "example"
    }
}

Responses:
    200: {
        "register": true,
        "message": "register success"
    }
    400: {
        "error": true,
        "message": "user already exist"
    }
    500: {
        "error": true,
        "message": SyntaxError
    }
```

- POST /api/point/received

```js
Request_body = {
    "data": {
        "username": "example",
        "received": 500
    }
}
Responses:
    200: {
        "success": true,
        "received points": 500
    }
    400: {
        "error": true,
        "message": "user not exist"
    }
    500: {
        "error": true,
        "message": SyntaxError
    }
```

- POST /api/point/used

```js
Request_body = {
    "data": {
        "username": "example",
        "used": 200
    }
}
Responses:
    200: {
        "success": true,
        "used points": 200
    }
    400: {
        "error": true,
        "message": "user not exist"
    }
    400: {
        "error": true,
        "message": "not enough points"
    }
    500: {
        "error": true,
        "message": SyntaxError
    }
```

- GET /api/point/

```js
Request_body = {
    "data": {
        "username": "example",
    }
}
Responses:
    200: {
        "success": true,
        "total points": 300
    }
    400: {
        "error": true,
        "message": "user not exist"
    }
    500: {
        "error": true,
        "message": SyntaxError
    }
```

## Architecture

![](/Architecture.png)

## Backend language and framework

- Python
- Flask

## Database

- AWS RDS (MySQL)  
  ![](/data_structure.png)
