# levers-sample-1
FastAPI with Postgres (Public)

# FastAPI with Postgres

A sample project built with FastAPI and Postgres

## Description

This project uses FastAPI to expose APIs the allow users to create bills with details of subbills. It exposes two APIs

* GET /api/v1/bills/bills/
* POST /api/v1/bills/bills/

GET api will get all the bills and allow the user to filter using reference, total_from and total_to

POST api allows the user to create new bills

## Getting Started

### Dependencies

* Docker
* Docker compose

### Installing

* Simply install docker and docker compose
* Clone this repo
* cd into the directory "levers_sample-2"
* Run following command
```
docker compose up -d
```

### Executing program

* Simply run the docker command
```
docker compose up -d
```
* Then open the browser to http://localhost:8888/docs

## Authors

Hasnain Ali


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GNU License - see the LICENSE.md file for details

