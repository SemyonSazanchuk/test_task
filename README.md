# Задание №1

## Запуск сервиса локально

Чтобы запустить сервис, нужно установить venv с зависимостями из requirements.txt и запустить скрипт src/main.py. Redis должен быть запущен заранее. С помощью энв переменных APP_HOST, APP_PORT, REDIS_HOST, REDIS_PORT можно задать хост и порт FastAPI приложения и Redis. По умолчанию APP_HOST="0.0.0.0", APP_PORT="8008", REDIS_HOST="localhost", REDIS_PORT="6379" для локального запуска. 

## Запуск сервиса в докере

Для запуска в докере нужно запустить cmd скрипт deployment/docker_deploy_all.cmd. При запуске в докере по умолчанию APP_HOST="0.0.0.0", APP_PORT="8008", REDIS_HOST="redis", REDIS_PORT="6379". В докере по умолчанию FastAPI приложение снаружи выставлено на порту 8009, а Redis на порту - 6380. Чтобы это изменить нужно поменять переменные EXPOSED_APP_PORT и EXPOSED_REDIS_PORT в файле deployment/.env. Все переменные для запуска в докере прописаны в deployment/.env.

# Задание №2

## Первый sql запрос на PL/pgSQL для решения задачи:

```
UPDATE full_names
SET status=short_names.status
FROM short_names
WHERE SPLIT_PART(full_names.name, '.', 1)=short_names.name;
```

## Второй sql запрос на PL/pgSQL для решения задачи:

```
ALTER TABLE full_names
RENAME TO full_names_old;
CREATE TABLE full_names AS
(SELECT full_names_old.name, short_names.status
FROM full_names_old LEFT JOIN short_names
ON SPLIT_PART(full_names_old.name, '.', 1)=short_names.name);
DROP TABLE full_names_old;
```