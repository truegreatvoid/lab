import os
import django
from django.core.management import call_command

# Configure o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")  # Substitua 'seu_projeto' pelo nome do seu projeto
django.setup()  # Inicializa o Django

def dump_specific_tables(output_file):
    # Lista de tabelas relacionadas às models
    tables = [
        "colaborador.Colaborador",
        # "tabela.Cargo",
        # "tabela.Competencia",
        # "tabela.Departamento",
        # "tabela.Ensino",
        # "tabela.Frequencia",
        # "tabela.Materia",
        # "tabela.Matriculaturma",
        # "tabela.Nota",
        # "tabela.Periodo",
        # "tabela.Turma",
    ]
    
    # Gera o dump apenas para as tabelas especificadas
    with open(output_file, 'w') as f:
        call_command('dumpdata', *tables, stdout=f, format='json')
    print(f"Dump concluído e salvo em {output_file}")

if __name__ == "__main__":
    output_file = "CargColaboradoro.json"
    dump_specific_tables(output_file)


