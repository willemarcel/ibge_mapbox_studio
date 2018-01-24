#!/bin/sh

ogr2ogr -f "GeoJSON" final_data.geojson  PG:"host=$IBGE_DB_HOST user=$IBGE_DB_USER dbname=$IBGE_DB_NAME password=$IBGE_DB_PASSWORD" -sql "select name, wkb_geometry from public.streets"
