# Plano de Testes Automatizados — API ViaCEP

## Objetivo

Este projeto foi desenvolvido com o objetivo de validar o comportamento da API ViaCEP em diferentes cenários de consulta de CEP.

Os testes automatizados simulam situações reais de uso em um fluxo de checkout inteligente, garantindo maior confiabilidade no preenchimento automático de endereço.

---

# Tecnologias Utilizadas

- Python 3
- Pytest
- Requests
- API ViaCEP

---

# Estrutura da Solução

O projeto foi organizado para facilitar:

- reutilização de código
- manutenção dos testes
- legibilidade
- expansão futura de cenários

A automação utiliza fixtures do Pytest e parametrização de entradas para reduzir repetição de código.

---

# Cenários Testados

| Código | Cenário | Resultado Esperado |
|--------|----------|-------------------|
| TC01 | CEP válido | Retorno correto dos dados do endereço |
| TC02 | CEP com hífen | API aceita formatação alternativa |
| TC03 | CEP inexistente | Retorno de erro controlado |
| TC04 | CEP com letras | Tratamento sem falha |
| TC05 | CEP incompleto | Resposta inválida tratada |
| TC06 | CEP vazio | Aplicação permanece estável |

---

# Descrição dos Cenários

## TC01 — Consulta válida

Valida o comportamento esperado da API quando um CEP existente é informado corretamente.

Esse cenário garante que os principais campos do endereço sejam retornados com sucesso.

---

## TC02 — CEP formatado

Verifica se a API mantém compatibilidade com CEPs contendo hífen, simulando entradas comuns feitas pelos usuários.

---

## TC03 — CEP inexistente

Avalia o comportamento da integração diante de um CEP inexistente, garantindo tratamento adequado da resposta.

---

## TC04 / TC05 / TC06 — Entradas inválidas

Esses testes verificam a robustez da aplicação diante de:

- caracteres inválidos
- CEP incompleto
- valor vazio

O objetivo é assegurar que o sistema continue estável sem falhas inesperadas.

---

# Como Executar

Instale as dependências:

```bash
pip install pytest requests
```

Execute os testes:

```bash
pytest -v
```

---

# Benefícios da Automação

- Redução de erros manuais
- Maior confiabilidade no checkout
- Cobertura de cenários críticos
- Facilidade de manutenção
- Maior estabilidade em integrações externas

---

# Considerações Finais

A automação de testes é essencial para garantir qualidade em integrações com APIs externas.

Os cenários implementados permitem validar comportamentos esperados e inesperados, aumentando a segurança e a estabilidade do sistema.