
# Steps to run this project

* 1. Run the following commande line in a terminal from this path

      docker-compose up -d
      docker build -t  taxi_ingest:v001 .
      docker run -t  --network=pg-network  taxi_ingest:v001 --user  root \
          --password  root \
          --host  pg-database \
          --port  5432 \
          --db  ny_taxi \
          --table_name  yellow_taxi_trips\
          --url   "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

* 2. click on http://localhost:8080 in orger to open pgadmin (login : admin@admin.com, password: root)

* 3. go to servers > new > server and Fill in the following fields:
    

        General.Name : docker localhost (as you like)

        Connexion.name : pg-database

        Connexion.user : root

        Connexion.password : root

