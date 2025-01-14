import os
import django
from django.core.management import call_command

# Configure o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")  # Substitua 'seu_projeto' pelo nome do seu projeto
django.setup()  # Inicializa o Django

def load_fixtures(folder_path):
    # Lista todos os arquivos na pasta
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):  # Verifica se o arquivo é JSON
            file_path = os.path.join(folder_path, file_name)
            print(f"Carregando {file_name}...")
            try:
                call_command('loaddata', file_path)
                print(f"{file_name} carregado com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar {file_name}: {e}")

if __name__ == "__main__":
    fixtures_folder = "./fixture/dump"  # Caminho para a pasta onde estão os arquivos JSON
    load_fixtures(fixtures_folder)
