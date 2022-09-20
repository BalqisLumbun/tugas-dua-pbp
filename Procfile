release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_watchlist_data.json'
web: gunicorn katalog.wsgi --log-file -
web: gunicorn mywatchlist.wsgi --log-file -