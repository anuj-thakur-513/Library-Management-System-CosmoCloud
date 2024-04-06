# Library Management System

A library management system built as an assignment for CosmoCloud

## Demo

https://github.com/anuj-thakur-513/Library-Management-System-CosmoCloud/assets/82753410/13a166bb-5c2b-4fc3-b8e6-225c44d4b0fe

## Deployment

If you want to use API endpoints, visit: [http://54.80.82.127/docs#/](http://54.80.82.127/docs#/)

If you want to get data from API endpoints, use: [http://54.80.82.127:80](http://54.80.82.127:80)


## Run Locally

Clone the project

```bash
  git clone https://github.com/anuj-thakur-513/Library-Management-System-CosmoCloud.git
```

Go to the project directory

```bash
  cd Library-Management-System-CosmoCloud
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

To test API Endpoints, Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Environment Variables

To run this project, you will need to add the following environment variable to your .env file

`MONGO_URI`


## API Reference

#### POST student (Create a Student)

```http
  POST /students
```

| Parameter   | Type   | Description                   |
| :---------- | :----- | :---------------------------- |
| `No Params` | `None` | Pass the data in Request Body |

#### GET all students

```http
  GET /students
```

| Parameter | Type      | Description                                                                                        |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------- |
| `Country` | `string`  | To apply filter of country                                                                         |
| `Age`     | `integer` | Only records which have age greater than equal to the provided age should be present in the result |

#### Get student

```http
  GET /students/{id}
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :----------------------------------- |
| `id`      | `string` | **Required**. Id of student to fetch |

```http
  PATCH /students/{id}
```

| Parameter | Type      | Description                          |
| :-------- | :-------- | :----------------------------------- |
| `id`      | `string`  | **Required**. Id of student to fetch |
| `name`    | `string`  | Name of the student to update        |
| `age`     | `integer` | Age of the student to update         |
| `city`    | `string`  | City of the student to update        |
| `country` | `string`  | Country of the student to update     |

```http
  DELETE /students/{id}
```

| Parameter | Type     | Description                           |
| :-------- | :------- | :------------------------------------ |
| `id`      | `string` | **Required**. Id of student to delete |
