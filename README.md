# mlops_practice_4
Practical work of the third semester of the master's program

Описание проекта:

ЦЕЛЕВАЯ ИНФРАСТРУКТУРА
- «Хранилище данных»
- «Анализ данных, эксперименты и обучение»
- «Тестирование модели»
- «Эксплуатация модели»
- «Сервер администратора»

GIT и DVC:
- sudo apt install git
- sudo python3 pip install dvc[ssh]

Для подключения к удаленному хранилищу необходимо выполнить следующие действия:
dvc remote modify --local ssh-storage password “тут надо указать пароль на data-srv”
		dvc pull

НАСТРОЙКА ДОСТУПА ПО SSH:
- sudo apt-get install ssh
- ssh-keygen

Для серверов взаимодеюствующих по протоколу ssh, необходимо обменяться открытыми ключами с помощью команды ssh-copy-id name_server@ip_address_server.

Также для корректной аутентификации по ssh необходимо добавить открытые ключи взаимодействующих хостов в autorized_keys на каждом хосте.

JENKINS

Получить и добавить ключ GPG в систему: 
- curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

Добавить адрес официального репозитория Jenkins в список пакетов apt в Ubuntu:
- echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

Обновить список пакетов:
- sudo apt update

Установить Jenkins: 
- sudo apt install jenkins

Запустить Jenkins:
- sudo systemctl start jenkins

Полезным шагом в настройке будет добавить пользователя jenkins в группу sudoers, чтобы он мог выполнять различные команды с root правами. Для этого в файл «/etc/sudoers» необходимо добавить следующую строку «jenkins ALL=(ALL) NOPASSWD: ALL»

Также потребуется узнать токен для авторизации на сайте, который хранится в специально созданном файле.

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

ANSIBLE

Установить ansible:

sudo apt install ansible

В файле hosts, необходмо указать название сервера и данные для подключения (если его нет, необходимо создать вручную)

[name]
ansible2 ansible_host=<host_id> ansible_port=22 ansible_user=<user> ansible_ssh_private_key_file=<path to secret key ssh>

Далее необходимо изменить конфигурационный файл Ansible для подключения ранее созданного файла.

sudo nano /etc/ansible/ansible.cfg

В конфигурационном файле необходимо раскомментировать строку «inventory» и указать путь до созданного файла. Из этого файла будут браться устройства, к которым можно будет подключаться.ч

Для проверки работы ansible выполнить следующую команду:

ansible all -m ping

PYTEST

sudo apt update

sudo apt install python-pytest






