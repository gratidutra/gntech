# Repositórios da Amazon no Github
Nesse projeto foi criado um extrator do repositório da amazon do github, construido um banco para 
armazenar os dados obtidos via API e criado uma nova api para Consulta dos mesmos. 

---
### Para Rodar

1. Instalar git, docker e docker compose
2. Clonar o repositório: ``git clone git@github.com:gratidutra/gntech.git`
3. Rodar a aplicação: `docker compose up --build` ou `sudo docker compose up --build`

Acompanhe a evolução das execuções via terminal para Assim que o banco e a tabela repositories estiver populada, você possa abri o link da api
---
### API
1. run: basta clicar no link disponibilizado no terminal `http://0.0.0.0:8000` 

Ele possui uma rota get que retorna json, caso deseja ver a documentação digite a rota http://0.0.0.0:8000/docs

Dicionário da tabela repositories
1. repository_name: nome do repositório
2. language: linguagens utilizadas em cada repositório
3. creaed_at: data de criação do repositório (fuso horário zero)
4. updated_at: data da ultima atualização do repositório (fuso horário zero)
