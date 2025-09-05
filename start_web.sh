#!/bin/bash

#if [[ ! -f ./backend/db/config.db ]]; then
#    echo "initilizing database ..."
#    sqlite3 ./backend/db/config.db < ./backend/db/init.sql
#fi

echo "start backend flask"
cd backend
flask run --host=0.0.0.0 --port=5000 &
cd ..

echo "start vite"
cd vite-project
npm run dev -- --host &
cd ..

echo "keep container run"
wait
