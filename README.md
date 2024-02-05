# my_simple_prj
# В этом репозитории лежат мои простейшие проекты, в своей основе использующие Docker.
#
# nginx+flask+pgsql - простейший веб-сервер, Nginx в режимер reverse proxy с использованием самоподписанного сертификата
#
# prometheus - содержит проект системы мониторинга Prometheus + Alertmanager + Node-exporter + Grafana. Alertmanager настроен на телеграм бот, но токен и ид чата удалены. 
# Система собирает данные с хоста, на котором развернута, и с еще 1 узла, workunit. В Readme файле внутри папке есть конфигурация /etc/hosts. Так же внутри json файл с конфигом dashbord.
#
# node-exporter - содержит yaml файл для разворачивания node-exporter на отдельном узле.
