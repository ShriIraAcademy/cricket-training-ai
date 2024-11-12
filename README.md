# cricket-training-ai

python manage.py runserver

<!-- curl -X POST http://127.0.0.1:8000/api/predict/ -H "Content-Type: application/json" -d '{"input_data": [0.5, 0.6, 0.1]}' -->
curl -X POST http://127.0.0.1:8000/api/predict/ -H "Content-Type: application/json" -d '{"input_data": [[175], [70], [22], [30]]}'
