# Adicionando Novas Ações para o IdentityNow

Este guia fornece instruções sobre como adicionar novas ações para o IdentityNow dentro de uma estrutura de Modelo-Visão-Controlador (MVC). As três classes principais envolvidas são `ConfigModel`, `IdentityNowAPI` e `AccessProfileController`.

## Estrutura do Projeto MVC

O projeto segue uma estrutura de Modelo-Visão-Controlador (MVC) básica:

- **Model (Modelo):** Responsável pela manipulação de dados e regras de negócios. No nosso caso, inclui as classes `ConfigModel` e `IdentityNowAPI`.
  
- **View (Visão):** Responsável pela interface do usuário (UI). Para nosso propósito, a interface é a linha de comando (CLI) implementada na classe `AccessProfileCLI`.
  
- **Controller (Controlador):** Atua como intermediário entre o Modelo e a Visão. Na nossa implementação, a classe `AccessProfileController` desempenha esse papel.

## Passos para Adicionar uma Nova Ação

### 1. Identifique a Nova Ação

Antes de tudo, identifique a nova ação que deseja adicionar ao IdentityNow. Por exemplo, você pode querer adicionar uma ação para atualizar os detalhes de uma identidade.

### 2. Crie o Método Correspondente na Classe `IdentityNowAPI`

Dentro da classe `IdentityNowAPI`, crie um novo método para realizar a ação desejada. Por exemplo, se você deseja adicionar uma ação para atualizar os detalhes de uma identidade, crie um método chamado `update_identity_details`.

### 3. Implemente a Lógica da Nova Ação

No método recém-criado, implemente a lógica necessária para realizar a ação desejada. Isso pode incluir a construção da solicitação HTTP adequada e o processamento da resposta.

### 4. Documente o Novo Método

Adicione comentários explicativos ao novo método para documentar seu propósito, parâmetros e possíveis valores de retorno.

### 5. Integre a Nova Ação ao Controlador

No `AccessProfileController`, integre a nova ação chamando o método correspondente da classe `IdentityNowAPI` dentro do método apropriado. Por exemplo, se você adicionou um método `update_identity_details` à `IdentityNowAPI`, chame esse método dentro do controlador, talvez em um método chamado `update_identity`.

### 6. Atualize a Interface do Usuário (Opcional)

Se necessário, atualize a interface do usuário (CLI) para permitir que os usuários acionem a nova ação.

## Exemplo de Implementação

Suponha que desejamos adicionar uma ação para atualizar os detalhes de uma identidade. Aqui está um exemplo de como implementar isso:

1. Na classe `IdentityNowAPI`, criamos um novo método chamado `update_identity_details`.
2. Implementamos a lógica necessária dentro desse método para enviar uma solicitação HTTP PUT para atualizar os detalhes da identidade.
3. Documentamos o novo método explicando seu propósito, parâmetros e valores de retorno.
4. No `AccessProfileController`, chamamos o novo método `update_identity_details` dentro de um novo método chamado `update_identity`.
5. Se necessário, atualizamos a interface do usuário (CLI) para permitir que os usuários acionem a ação de atualização de identidade.

Com esses passos, a nova ação para atualizar os detalhes de uma identidade está integrada à estrutura MVC e pronta para uso.
