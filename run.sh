#!/bin/sh

sh set_env_vars.sh
sh import_to_db.sh
python -c 'from database import add_name_column; add_name_column()'
python -c 'from database import update_names; update_names()'
sh export_to_geojson.sh
