# mba-webservices

# SiGeC - Sistema de Gerenciamento de Clientes 🤵‍♂️🤖🍻🍻😄

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=Em+desenvolvimento&color=GREEN&style=for-the-badge)

## 🎯 Objetivo

Esse repositório abriga o código de um sistema simples de cadastro e gerenciamento de clientes (criar, consultar,
atualizar e remover). O sistema possui 2 APIs (/clientes e /cartoes) que se comunicam com o banco de dados e um
front-end
que consome a ambas as APIs. Além disso, as a API /clientes possui chamada para a API /cartoes, e vice-versa.

## 🛠️ Tecnologias utilizadas

- Docker: devido a facilidade de subir todos os serviços (banco de dados, front-end, api). Além disso, possibilita que
  a aplicação rode como microsserviços, facilitando a manutenção do código.
- Git: ferramenta escolhida para controle de versão e integração do código
- FastAPI: framework python para desenvolvimento de APIs, escolhida devido a sua facilidade de implementação.
- Django: framework python para desenvolvimento web.
- MongoDB: 

## Pré requisitos:

- Docker-compose
- Git

## Passo a passo para a execução do Back-end:

1. Clonar projeto do GitHub:
~~~bash
$ git clone git@github.com:lynixcarvalho/mba-webservices.git
$ cd mba-webservices
~~~
2. Executar o docker-compose:
~~~bash
$ docker-compose up -d
~~~
- Usuários de Linux/Mac podem executar diretamente o script runserver.sh no lugar do comando acima:
~~~bash
$ sh runserver.sh
~~~

### Front-end

- Após subir o ambiente de back-end, a URL do front-end fica acessível no endereço localhost:9000, que pode ser acessada pelo navegador.

### Documentação da API

- Documentação da API de clientes: localhost:9100/docs no navegador.
- Documentação da API de cartões: localhost:9200/docs no navegador.

## AWS Cloud

Para os que desejarem testar as funcionalidades atuais da aplicação diretamente, podem acessar o endereço:
- Front-end: http://ec2-54-232-175-199.sa-east-1.compute.amazonaws.com
- API clientes: http://ec2-54-232-175-199.sa-east-1.compute.amazonaws.com:9100/docs
- API cartoes: http://ec2-54-232-175-199.sa-east-1.compute.amazonaws.com:9200/docs

## 👨🏽‍💻👩🏽‍💻 Desenvolvedores

[<img src="https://avatars.githubusercontent.com/alessferns" width=115><br><sub>Alessandro Fernandes Santos</sub>](https://github.com/alessferns)

[<img src="https://avatars.githubusercontent.com/KarinaFSantos" width=115><br><sub>Karina Fávero dos Santos</sub>](https://github.com/KarinaFSantos)

[<img src="https://avatars.githubusercontent.com/lynixcarvalho" width=115><br><sub>Lincoln Silva Carvalho</sub>](https://github.com/lynixcarvalho)

[<img src="https://avatars.githubusercontent.com/Makio78" width=115><br><sub>Marcelo Akio Kitahara</sub>](https://github.com/Makio78)

[<img src="https://avatars.githubusercontent.com/jrsorgato" width=115><br><sub>Osvaldo Sorgato Junior</sub>](https://github.com/jrsorgato)

[<img src="https://avatars.githubusercontent.com/VANESSA-SS" width=115><br><sub>Vanessa Santos e Silva</sub>](https://github.com/VANESSA-SS)

## Origem

Projeto realizado como requisito para conclusão da disciplina Webservices do MBA Full Stack Development - FIAP 2022

Prof. Eduardo Galego 
