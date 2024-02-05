Файлом docker-compose.yml  будет собрана система Prometheus+Grafana+Alertmanages+NodeExporter - мониторинг системы, метрики идут с node-exporter, который развернут локально.
Alertmanager настроен на работу с телеграм ботом.
Адреса:
http://gitrepovm.test.by:9090 - prometheus
http://gitrepovm.test.by:9100 - node-exporter
http://gitrepovm.test.by:3000 - grafana
http://gitrepovm.test.by:9093 - alertmanager

Адреса указаны с учетом текущего окружения

Из конфига Alertmanager удалены токен и ид чата

grafana_my_dashboard.json - конфиг dashboard для grafana под текущий сетап


/etc/hosts
FOR promrtheus
127.0.0.1 localhost
127.0.1.1 gitrepovm.test.by gitrepovm
192.168.56.101 gitrepovm.test.by gitrepovm
192.168.56.102 workunit.test.by workunit

FOR workunit
127.0.0.1 localhost
127.0.1.1 workunit.test.by workunit
192.168.56.101 gitrepovm.test.by gitrepovm
192.168.56.102 workunit.test.by workunit
