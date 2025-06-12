import requests
from dotenv import load_dotenv
import os
from models import create_table, Repository, SessionLocal

load_dotenv()

class DataRepositories:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('GITHUB_TOKEN')
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def list_repositories(self):
        
        '''
        utilize o endpoint https://api.github.com/users/OWNER para obter dados gerais de uma conta do GitHub;
        selecione o campo public_repos do JSON extraído para obter a quantidade de repositórios públicos existentes em uma conta do GitHub;
        modifique o código do método lista_repositorios substituindo o valor fixo 20 pelo número real de páginas de repositórios da conta do GitHub em análise.
        '''
        repos_list = []

        for page_num in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list

    def repos_name(self, repos_list): 
        repo_names = [] 
        for page in repos_list:
            if page:  # Only process if page is not None and not empty
                for repo in page:
                    try:
                        repo_names.append(repo['name'])
                    except (KeyError, TypeError): 
                        pass
        return repo_names

    def languages_name(self, repos_list):
        repo_languages=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass

        return repo_languages
    
    def created_date(self, repos_list):
        repos_created_date=[]
        for page in repos_list:
            for repo in page:
                try:
                    repos_created_date.append(repo['created_at'])
                except:
                    pass

        return repos_created_date
    
    def updated_date(self, repos_list):
        repos_updated_date=[]
        for page in repos_list:
            for repo in page:
                try:
                    repos_updated_date.append(repo['updated_at'])
                except:
                    pass

        return repos_updated_date
    
    
    def save_repos_to_db(self, names, languages, created_dates, updated_dates):
        create_table()
        session = SessionLocal()

        try:
            if not (len(names) == len(languages) == len(created_dates) == len(updated_dates)):
                print("Warning: Lists have different lengths. Data might be inconsistent.")

            for i in range(len(names)):
                try:
                    repo_entry = Repository(
                        repository_name=names[i],
                        language=languages[i] if i < len(languages) else None,
                        created_at=created_dates[i] if i < len(created_dates) else None,
                        updated_at=updated_dates[i] if i < len(updated_dates) else None
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

