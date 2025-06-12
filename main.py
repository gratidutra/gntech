from extractor_github import DadosRepositorios


if __name__ == "__main__":
    owner = 'amzn'  # Troque para o user desejado
    dados = DadosRepositorios(owner)
    repos_list = dados.list_repositories()
    
    names = dados.repos_name(repos_list)
    languages = dados.languages_name(repos_list)
    created_dates = dados.created_date(repos_list)
    updated_dates = dados.updated_date(repos_list)

    dados.save_repos_to_db(names, languages, created_dates, updated_dates)
