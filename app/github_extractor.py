import os

import requests
from dotenv import load_dotenv
from models import Repository, SessionLocal, create_table

load_dotenv()


class DataRepositories:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = "https://api.github.com"
        self.access_token = os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Authorization": "Bearer " + self.access_token,
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def list_repositories(self):
        """
        Função executa a consulta na API do github para pegar a lista de
        repositórios considerando a paginação até 20
        """

        repos_list = []

        for page_num in range(1, 20):
            try:
                url = f"{self.api_base_url}/users/{self.owner}/repos?page={page_num}"
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list

    def repos_name(self, repos_list):
        """
        Função que recupera da lista criada pelo list_repositories os nomes dos repositórios e
        armazena em uma lista de nome repo_names
        """
        repo_names = []
        for page in repos_list:
            if page:  # Only process if page is not None and not empty
                for repo in page:
                    try:
                        repo_names.append(repo["name"])
                    except (KeyError, TypeError):
                        pass
        return repo_names

    def languages_name(self, repos_list):
        """
        Função que recupera da lista criada pelo list_repositories 
        as linguagens dos repositórios e armazena em uma lista de linguagens de programação
        repo_languages
        """
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo["language"])
                except:
                    pass

        return repo_languages

    def created_date(self, repos_list):
        """
        Função que recupera da lista criada pelo list_repositories as datas de
        criação dos repositórios e armazena em uma lista de datas de criação
        """
        repos_created_date = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_created_date.append(repo["created_at"])
                except:
                    pass

        return repos_created_date

    def updated_date(self, repos_list):
        """
        Função que recupera da lista criada pelo list_repositories as datas de
        atualização dos repositórios e armazena em uma lista de datas de atualização
        """
        repos_updated_date = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_updated_date.append(repo["updated_at"])
                except:
                    pass

        return repos_updated_date

    def save_repos_to_db(self, names, languages, created_dates, updated_dates):
        """
        Função que cria a tabela repositories estruturada no script models e armazenas os
        dados obtidos do repositório da AMAZON
        """
        create_table()
        session = SessionLocal()

        try:
            if not (
                len(names) == len(languages) == len(created_dates) == len(updated_dates)
            ):
                print(
                    "Warning: Lists have different lengths. Data might be inconsistent."
                )

            for i in range(len(names)):
                try:
                    repo_entry = Repository(
                        repository_name=names[i],
                        language=languages[i] if i < len(languages) else None,
                        created_at=created_dates[i] if i < len(created_dates) else None,
                        updated_at=updated_dates[i] if i < len(updated_dates) else None,
                    )
                    session.add(repo_entry)
                except Exception as e:
                    print(f"Error creating record {i}: {e}")
                    continue

            session.commit()
            print(f"Successfully inserted {len(names)} records into the database.")

        except Exception as e:
            session.rollback()
            print("Error during database operation:", e)

        finally:
            session.close()
