Здесь лежит проект запуска приложения из папки 4(но без nginx), исходно сделанного в docker-compose, в среде k8s.
Шаги пробразования проекта docker-compose для запуска в k8s:

-Билдим docker-compose
 docker-compose build

-Сохранием образ flask-test
 docker image save 4-for-k8s_flask-test -o flask-test

-Загружаем образ в локальный репозиторий, который может видеть k8s или, как в моем случае, в minikube
 minikube image load flask-test
 minikube image tag docker.io/library/4-for-k8s_flask-test flask-test
 minikube image ls - посмотреть образы в minikube

-Качаем и предоставляем права программер-конвертеру
 curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-linux-amd64 -o kompose
 chmod +x kompose 

-Запускаем ее
 ./kompose covert
 Она создает кучу yaml файлов

-Вносим изменения в файл flask-test-deployment.yaml
 ...
 image: flask-test
 imagePullPolicy: Never
 name: flask-test
 ...
 Добавляем строку imagePullPolicy: Never так как это показано выше. Это необходимо, чтобы k8s не искал образ flask-test в интернете, а использовал локальный, который мы уже закинули в minikube.

-"Закидываем" их в k8s
 kubectl apply -f flask-test-deployment.yaml,flask-test-service.yaml,my-prj-net-networkpolicy.yaml,pgsql-data-persistentvolumeclaim.yaml,pgsql-test-deployment.yaml,pgsql-test-service.yaml
 *Чтобы удалить их из k8s заменить apply на delete

-Делаем в etc/hosts запись
 (minikube ip) local.test.by - команда в скобках нужная чтобы узнать какой IP записать


-Запускаем dashboard для удобства отслеживания и мелкого редактирования
 minikube dashboard

-Заходим в dashboard -- Services -- flask-test -- Edit
 ищем type: ClusterIp меняем на NodePort, а в раздел Ports вниз добавляем nodePort:30007

-В браузере заходим http://local.test.by:30007 - Все должно рабоать

__________________________________________________________________________________
Далее описан метод с использование "маршрутизатора" Ingress-nginx. При использовании этого варианта не надо редактировать сервис flask-test через dashboard


-Включаем плагин для minikube
 minikube addons enable ingress - по сути это nginx в режиме обратного прокси
 kubectl get pods -n ingress-nginx - проверием что все ок

-Создаем для него файл конфигурации app-ingress.yaml
 kubectl apply -f app-ingress.yaml - закидываем в k8s
 kubectl get ingress - проверяем

-Подключаемся через браузер http://local.test.by:80

Инфа по Ingress для minkube https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/

Тут есть проблема метод POST  не работает, выдаетс яошибка 405. Так как в версии без nginx-ingress этой проблемы нет, то можно ссылаться на проблемы с Ingress-nginx.
Файл yaml для ingress это моя последняя на 17.02.2024 версия, проблема не решена. Важное замечание это все делается локально в minikube
____________________________________________________________________________________

Имена папок, файлов, образов могут отличаться для каждого конкретного случая использования.
