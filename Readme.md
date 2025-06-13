# Repositórios da Amazon no Github
Neste projeto, foi implementado um extrator de dados a partir do repositório da Amazon no GitHub, modelada uma base de dados relacional para armazenamento das informações coletadas via API, além do desenvolvimento de uma nova API para disponibilização e consulta desses dados. 

---
### Para Rodar

1. Instalar git, docker e docker compose
2. Clonar o repositório: `git clone git@github.com:gratidutra/gntech.git`
3. Rodar a aplicação: `docker compose up --build` ou `sudo docker compose up --build`

Acompanhe a execução via terminal e, assim que o banco de dados e a tabela repositories estiverem populados, acesse o endpoint da API por meio do link disponibilizado.

---
### API
1. run: basta clicar no link disponibilizado no terminal `http://0.0.0.0:8000` 

Ele possui uma rota `GET` que retorna o dado em json, caso deseja ver a documentação da rota digite a rota http://0.0.0.0:8000/docs

Dicionário da tabela repositories
1. **repository_name**: nome do repositório
2. **language**: linguagens utilizadas em cada repositório
3. **created_at**: data de criação do repositório (fuso horário zero)
4. **updated_at**: data da ultima atualização do repositório (fuso horário zero)
