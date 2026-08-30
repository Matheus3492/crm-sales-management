# Requisitos do Projeto — CRM Sales Management

## 1. Visão Geral

O CRM Sales Management será um sistema de gerenciamento de relacionamento com clientes e processos comerciais.

O projeto será desenvolvido inicialmente para execução local e deverá possuir uma arquitetura preparada para futura expansão para um ambiente web e multiusuário.

O sistema terá como objetivo centralizar informações de clientes, leads, negociações, atividades comerciais, propostas e indicadores de desempenho.

---

## 2. Objetivos

Os principais objetivos do sistema são:

- Centralizar os dados dos clientes.
- Organizar leads e oportunidades comerciais.
- Controlar o processo de vendas.
- Permitir acompanhamento das negociações por meio de um pipeline Kanban.
- Registrar todas as interações realizadas pelos vendedores.
- Controlar follow-ups e reuniões.
- Armazenar propostas e documentos relacionados às negociações.
- Disponibilizar indicadores comerciais.
- Permitir análise de desempenho dos vendedores.
- Auxiliar na previsão de faturamento.
- Identificar motivos de perda de oportunidades.
- Manter histórico das alterações realizadas no sistema.
- Aplicar boas práticas de segurança da informação.

---

## 3. Usuários do Sistema

O sistema terá inicialmente três perfis de usuário.

### 3.1 Administrador

Responsável pela administração geral do sistema.

Permissões previstas:

- Gerenciar usuários.
- Gerenciar perfis e permissões.
- Visualizar todos os clientes.
- Visualizar todas as negociações.
- Visualizar todos os indicadores.
- Configurar etapas do pipeline.
- Gerenciar configurações do sistema.
- Consultar logs de auditoria.

### 3.2 Gerente

Responsável pelo acompanhamento da equipe comercial.

Permissões previstas:

- Visualizar clientes da equipe.
- Visualizar negociações da equipe.
- Acompanhar atividades dos vendedores.
- Visualizar dashboards.
- Analisar indicadores comerciais.
- Acompanhar pipeline.
- Consultar informações de desempenho.

### 3.3 Vendedor

Responsável pela operação comercial.

Permissões previstas:

- Cadastrar leads.
- Cadastrar clientes.
- Criar negociações.
- Atualizar suas negociações.
- Registrar atividades.
- Criar follow-ups.
- Registrar reuniões.
- Registrar propostas.
- Anexar documentos.
- Visualizar seus indicadores.

---

## 4. Gestão de Leads

O sistema deverá permitir o cadastro e gerenciamento de leads.

Informações previstas:

- Nome da empresa.
- Nome do contato.
- Telefone.
- E-mail.
- Cidade.
- Estado.
- Região.
- Segmento.
- Origem do lead.
- Responsável.
- Data de entrada.
- Status.
- Observações.

Exemplos de origem:

- Google Ads.
- Instagram.
- Site.
- Indicação.
- WhatsApp.
- Prospecção.
- Evento.
- Outros.

---

## 5. Gestão de Clientes

O sistema deverá permitir o cadastro de clientes e empresas.

Informações previstas:

- Razão social.
- Nome fantasia.
- CNPJ.
- Telefone.
- E-mail.
- Site.
- Endereço.
- Cidade.
- Estado.
- Região.
- Segmento.
- Observações.

Um cliente poderá possuir vários contatos.

---

## 6. Gestão de Contatos

Cada empresa poderá possuir múltiplos contatos.

Informações previstas:

- Nome.
- Cargo.
- Telefone.
- WhatsApp.
- E-mail.
- Observações.

---

## 7. Negociações

Uma empresa poderá possuir uma ou mais negociações.

Cada negociação deverá possuir:

- Cliente.
- Responsável.
- Título.
- Valor estimado.
- Etapa do pipeline.
- Probabilidade de fechamento.
- Data de criação.
- Previsão de fechamento.
- Data de fechamento.
- Status.
- Motivo da perda.
- Observações.

---

## 8. Pipeline de Vendas

O sistema deverá possuir um pipeline visual no formato Kanban.

Etapas iniciais previstas:

1. Novo Lead
2. Qualificação
3. Contato Realizado
4. Reunião
5. Proposta
6. Negociação
7. Ganho
8. Perdido

As negociações poderão ser movimentadas entre as etapas.

---

## 9. Atividades Comerciais

O sistema deverá permitir registrar as interações realizadas com os clientes.

Tipos de atividade previstos:

- Ligação.
- WhatsApp.
- E-mail.
- Reunião.
- Follow-up.
- Observação.

Cada atividade deverá registrar:

- Usuário responsável.
- Data.
- Hora.
- Tipo.
- Descrição.
- Resultado.
- Próximo follow-up.

---

## 10. Reuniões

O sistema deverá permitir o agendamento e registro de reuniões.

Informações previstas:

- Cliente.
- Contato.
- Responsável.
- Data.
- Hora.
- Tipo de reunião.
- Assunto.
- Observações.
- Resultado.

---

## 11. Follow-ups

O sistema deverá permitir o agendamento de follow-ups.

Um follow-up deverá possuir:

- Data.
- Hora.
- Responsável.
- Cliente.
- Negociação.
- Observação.
- Status.

Status previstos:

- Pendente.
- Realizado.
- Cancelado.
- Atrasado.

---

## 12. Propostas

O sistema deverá permitir o registro de propostas comerciais.

Informações previstas:

- Cliente.
- Negociação.
- Número da proposta.
- Data.
- Valor.
- Validade.
- Status.
- Observações.
- Arquivo relacionado.

---

## 13. Anexos

O sistema deverá permitir o armazenamento de arquivos relacionados aos clientes e negociações.

Tipos de arquivos previstos:

- PDF.
- Imagens.
- Documentos.
- Planilhas.

Cada arquivo deverá possuir informações de controle, incluindo:

- Nome.
- Tipo.
- Tamanho.
- Data de envio.
- Usuário responsável.
- Registro relacionado.

---

## 14. Dashboard

O sistema deverá disponibilizar um dashboard comercial.

### Indicadores de Leads

- Quantidade de leads.
- Leads por período.
- Leads por origem.
- Leads por vendedor.
- Leads por região.
- Leads por segmento.

### Indicadores do Funil

- Quantidade de oportunidades por etapa.
- Conversão entre etapas.
- Taxa de conversão geral.
- Quantidade de oportunidades ganhas.
- Quantidade de oportunidades perdidas.

### Indicadores Financeiros

- Valor total vendido.
- Ticket médio.
- Pipeline aberto.
- Forecast.
- Valor perdido.
- Valor das oportunidades ganhas.

### Indicadores de Vendedores

- Quantidade de atividades.
- Quantidade de negociações.
- Negociações ganhas.
- Negociações perdidas.
- Taxa de conversão.
- Ticket médio.
- Tempo médio de fechamento.

---

## 15. Forecast

O sistema deverá permitir estimar o potencial de faturamento das oportunidades abertas.

O forecast poderá utilizar o valor da negociação combinado com a probabilidade de fechamento.

Exemplo:

Valor da negociação: R$ 100.000

Probabilidade: 80%

Forecast ponderado:

R$ 80.000

---

## 16. Análise de Perdas

Quando uma negociação for marcada como perdida, o sistema deverá solicitar um motivo.

Motivos iniciais previstos:

- Preço.
- Concorrente.
- Falta de orçamento.
- Desistência.
- Prazo.
- Produto inadequado.
- Cliente sem retorno.
- Outro.

O sistema deverá permitir analisar o valor perdido por motivo.

---

## 17. Região e Segmento

O sistema deverá permitir analisar clientes e negociações por:

- Região.
- Estado.
- Cidade.
- Segmento.

Essas informações deverão estar disponíveis nos dashboards.

---

## 18. Ciclo de Vida do Cliente

O sistema deverá registrar a evolução do relacionamento com o cliente.

Exemplo:

Lead → Qualificação → Negociação → Cliente → Nova oportunidade → Nova venda

O sistema deverá manter o histórico das interações e negociações realizadas.

---

## 19. Tempo de Fechamento

O sistema deverá calcular o tempo necessário para concluir uma negociação.

O cálculo deverá considerar:

Data do primeiro contato → Data de fechamento.

Indicadores previstos:

- Tempo médio geral.
- Tempo médio por vendedor.
- Tempo médio por segmento.
- Tempo médio por região.

---

## 20. Segurança

A segurança deverá ser considerada desde o início do desenvolvimento.

Medidas previstas:

- Autenticação de usuários.
- Controle de acesso por perfil.
- Hash seguro de senhas.
- Validação de dados.
- Proteção de informações sensíveis.
- Variáveis de ambiente.
- Controle de acesso aos arquivos.
- Logs de auditoria.
- Controle de sessões.
- Proteção da API.
- Backup do banco de dados.

Informações sensíveis não deverão ser armazenadas diretamente no código-fonte.

---

## 21. Auditoria

O sistema deverá registrar ações importantes realizadas pelos usuários.

Exemplos:

- Criação de cliente.
- Alteração de cliente.
- Criação de negociação.
- Alteração de valor.
- Alteração de etapa.
- Exclusão de registro.
- Upload de arquivo.
- Alteração de usuário.

Os registros deverão possuir informações como:

- Usuário.
- Data e hora.
- Ação.
- Registro afetado.
- Valor anterior.
- Novo valor.

---

## 22. Requisitos Futuros

O projeto deverá possuir arquitetura preparada para futuras funcionalidades.

Possíveis funcionalidades:

- Integração com WhatsApp.
- Integração com e-mail.
- Integração com Google Ads.
- Integração com APIs externas.
- Cadastro de produtos.
- Controle de pedidos.
- Metas comerciais.
- Comissões.
- Automação de follow-ups.
- Aplicação mobile.
- Deploy em nuvem.
- Multiempresa.

---

## 23. Estratégia de Desenvolvimento

O sistema será desenvolvido inicialmente em ambiente local.

A arquitetura deverá permitir posteriormente a migração para um ambiente de produção.

Prioridades:

1. Segurança.
2. Organização do código.
3. Integridade dos dados.
4. Testabilidade.
5. Manutenibilidade.
6. Escalabilidade.
7. Desempenho.