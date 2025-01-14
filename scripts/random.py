import random
from faker import Faker
from apps.colaborador.models import Colaborador
from apps.tabela.models import Cargo, Departamento, Materia, Turma

# Configurando o Faker
faker = Faker('pt_BR')

# Listas específicas para escolas
ESCOLA_CARGOS = ['Diretor', 'Coordenador Pedagógico', 'Secretário', 'Professor']
DISCIPLINAS = ['Matemática', 'Português', 'História', 'Geografia', 'Ciências', 'Física', 'Química', 'Inglês']
TURMAS = [f"{ano}º Ano {letra}" for ano in range(1, 4) for letra in 'ABCD']  # Ex.: 1º Ano A, 2º Ano B, etc.

def generate_fake_escola_data(num_colaboradores=10, num_materias=10):
    # Criar cargos para a escola
    for cargo in ESCOLA_CARGOS:
        Cargo.objects.get_or_create(nome=cargo)

    # Criar departamentos padrão
    departamentos = ['Administração', 'Coordenação', 'Secretaria', 'Docência']
    for dep in departamentos:
        Departamento.objects.get_or_create(nome=dep)

    cargos = list(Cargo.objects.all())
    departamentos = list(Departamento.objects.all())

    # Criar colaboradores (professores e outros)
    for _ in range(num_colaboradores):
        nome = faker.name()
        email = faker.email()
        apelido = faker.first_name()
        cpf = faker.ssn()[:11]
        nivel = random.choice(['P', 'D', 'C', 'S'])  # Professor, Diretor, Coordenador, Secretaria
        cargo = random.choice(cargos) if cargos else None
        departamento = random.choice(departamentos) if departamentos else None

        colaborador = Colaborador.objects.create(
            nome=nome,
            email=email,
            apelido=apelido,
            cpf=cpf,
            nivel=nivel,
            cargo=cargo,
            departamento=departamento
        )
        print(f"Colaborador criado: {colaborador.nome} - Cargo: {cargo.nome}")

    # Criar turmas
    for turma_nome in TURMAS:
        Turma.objects.get_or_create(nome=turma_nome)

    # Criar matérias
    turmas = list(Turma.objects.all())
    professores = Colaborador.objects.filter(nivel='P')  # Apenas professores

    for _ in range(num_materias):
        if professores and turmas:
            professor = random.choice(professores)
            turma = random.choice(turmas)
            disciplina = random.choice(DISCIPLINAS)
            Materia.objects.get_or_create(
                nome=disciplina,
                professor=professor,
                horario=faker.time(),
                defaults={'turma': turma}
            )
            print(f"Matéria criada: {disciplina} - Professor: {professor.nome} - Turma: {turma.nome}")

# Executar o script
if __name__ == "__main__":
    print("Gerando dados falsos para a escola...")
    generate_fake_escola_data(num_colaboradores=20, num_materias=15)
    print("Dados gerados com sucesso!")
