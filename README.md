   # 🚀 Sistema de Inventário — Setor de T.I.

Este repositório contém o código-fonte do **Projeto Final**  desenvolvido para a disciplina de **Banco de Dados**do curso de **Tecnólogo em IA (2º Período)** do **PIT — Piauí Instituto de Tecnologia**, sob a orientação da **Profa. Evelyn Silva**.

O objetivo do sistema é gerenciar com eficiência os ativos tecnológicos de uma organização (hardwares, softwares, licenças e periféricos), implementando uma arquitetura web persistente e integrada.

---

## 🔗 Links de Acesso Direto
Conforme os requisitos de entrega da atividade, seguem os links públicos do ecossistema do projeto:
* **Aplicação em Produção (Render):** [(https://inventario-ti-flask.onrender.com)]

---

## 👥 Componentes do Grupo
* 1- Breno Aguiar
* 2- Abraham Vasquez
* 3- Hyara Beatriz

---

## 🛠️ Stack Tecnológica de Desenvolvimento

Para viabilizar uma aplicação moderna, dinâmica e escalável, o ecossistema técnico foi dividido em três pilares fundamentais:

* **Banco de Dados Relacional:** Hospedado na nuvem através do **NEON (PostgreSQL)**, garantindo alta disponibilidade, transações ACID confiáveis e persistência íntegra de dados.
* **Back-end e API:** Construído em **Python** utilizando o framework **Flask**, responsável pelo gerenciamento de rotas, consumo de dados e barramento lógico da aplicação via ORM (*Flask-SQLAlchemy*).
* **Front-end e Telas:** Desenvolvido de forma responsiva utilizando **HTML5**, **CSS3 embedded** para garantir a renderização visual do design de forma consistente e **JavaScript** nativo para validações lógicas e comportamentais em tempo de execução.

---

## 📊 Arquitetura de Banco de Dados & Modelo ER

O banco de dados foi normalizado e estruturado sob um modelo relacional de **1:N (Um para Muitos)**, garantindo que as restrições de integridade referencial impeçam registros órfãos ou inconsistências em cascata.

### 1. Entidades e Mapeamento de Atributos

| Tabela | Atributo | Tipo de Dado | Restrições | Descrição Técnica |
| :--- | :--- | :--- | :--- | :--- |
| **CATEGORIA** | `codigo` | INT | PRIMARY KEY | Identificador numérico e exclusivo da categoria. |
| | `nome` | VARCHAR(100) | NOT NULL | Nome de agrupamento do ativo (ex: Hardware, Redes). |
| | `sigla` | VARCHAR(10) | NOT NULL | Abreviação identificadora da categoria (ex: HW, SW). |
| **ITEM** | `patrimonio` | INT | PRIMARY KEY | Número de tombamento físico exclusivo do item. |
| | `nome` | VARCHAR(100) | NOT NULL | Descrição exata do equipamento ou sistema corporativo. |
| | `valor` | DECIMAL(10,2)| - | Custo estimado de aquisição ou licença do ativo. |
| | `responsavel_email`| VARCHAR(150)| - | E-mail corporativo do técnico encarregado do bem. |
| | `localizacao` | VARCHAR(200)| - | Local físico de armazenamento (ex: CPD, Sala A). |
| | `codigo_cat` | INT | FOREIGN KEY | Chave estrangeira ligada à tabela `CATEGORIA`. |

### 2. Regras de Integridade Referencial (Dicionário do Modelo ER)
* **Cardinalidade:** Uma `CATEGORIA` pode classificar **1 ou N** itens de inventário, enquanto um `ITEM` pertence obrigatoriamente a **1 e apenas 1** categoria cadastrada.
* **Ações em Cascata:** A chave estrangeira foi mapeada via ORM com a diretriz `cascade="all, delete"`. Dessa forma, se uma categoria for removida do banco, todos os itens associados a ela são deletados automaticamente pelo banco para mitigar inconsistências.

---

## 💻 Escopo Funcional do Sistema (CRUD Completo)

A aplicação cumpre com todos os pilares do ecossistema transacional de um **CRUD Completo**:

* **[C]reate (Criar / Inserir):** Rota `/novo-item` que processa formulários de cadastro, instanciando novas linhas na tabela `ITEM` do Neon via comandos abstratos do ORM.
* **[R]ead (Ler / Consultar):** Rotas `/itens` e `/categorias` que realizam buscas completas (equivalentes ao `SELECT * FROM`) populando tabelas estilizadas na interface Web.
* **[U]pdate (Atualizar / Editar):** Rota dinâmica `/editar-item/<int:patrimonio>` que localiza o ativo pela chave primária, popula os campos do formulário com os valores correntes do Neon e atualiza as colunas após a submissão via método `POST`.
* **[D]elete (Deletar / Excluir):** Rota `/deletar-item/<int:patrimonio>` vinculada a um evento JavaScript no front-end (`onclick="return confirm()"`) que intercepta o clique do usuário para validação e remove fisicamente o registro do banco através de uma requisição segura.

---

## 🚀 Como Executar o Projeto em Ambiente de Desenvolvimento

Como o ambiente deste grupo foi limitado estritamente ao navegador (Web-Only), a aplicação foi projetada para dispensar instalações ou dependências locais, rodando inteiramente na nuvem.

### Configuração em Nuvem:
1. Os dados estruturais e os dados de inserção iniciais foram injetados por meio do console de edição do **Neon Tech (PostgreSQL)**.
2. O código-fonte foi gerenciado e versionado diretamente pelo editor web do **GitHub**.
3. O deploy contínuo (*CI/CD*) foi configurado no painel de serviços do **Render**, que mapeia o arquivo `requirements.txt` para instalar as bibliotecas do servidor automaticamente em ambiente Linux de produção, injetando as credenciais do banco por variáveis de ambiente ocultas (`DATABASE_URL`), preservando a segurança da aplicação.
