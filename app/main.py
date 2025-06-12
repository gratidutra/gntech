from github_extractor import DataRepositories

if __name__ == "__main__":
    print("Iniciando a consulta na API")
    owner = "amzn"
    data = DataRepositories(owner)
    repos_list = data.list_repositories()

    names = data.repos_name(repos_list)
    languages = data.languages_name(repos_list)
    created_dates = data.created_date(repos_list)
    updated_dates = data.updated_date(repos_list)

    data.save_repos_to_db(names, languages, created_dates, updated_dates)

    print("Dados armazenados com Sucesso!")
