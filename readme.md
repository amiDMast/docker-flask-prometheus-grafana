# Docker: Flask-Prometheus-Grafana

> Генерация метрик в приложении -> сбор с помощью Prometheus -> вывод в Grafana

### Для запуска используйте start.sh

Делаем скрипт исполняемым и запускаем его.

```sh
sudo chmod +x start.sh 
sh start.sh
```

В конце выполнения будет выведена на терминал информация о контейнере приложения: helth-status и ready-status

### Запуск отдельно: Prometheus, Grafana & Dashboards

```sh
docker-compose up -d prometheus
docker-compose up -d grafana
docker-compose up -d grafana-dashboards
```


### Запуск приложения отдельно

```sh
docker-compose up -d --build python-application
```

### Генерация запроса путем открытия страницы приложения (Python application) в браузере

```
http://localhost
```

### Grafana
```
http://localhost:3000
```
### Prometheus
```
http://localhost:9091
```

