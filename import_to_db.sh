#!/bin/sh

for shp in `ls $IBGE_SHP_PATH/*_face.shp`
  do ogr2ogr -f "PostgreSQL" PG:"host=$IBGE_DB_HOST user=$IBGE_DB_USER dbname=$IBGE_DB_NAME password=$IBGE_DB_PASSWORD" $shp -nln streets -nlt MULTILINESTRING
done
