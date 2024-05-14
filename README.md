# Access Profile Manager

Este é um gerenciador para IdentityNow.

## Execução do Projeto

Para executar o projeto, siga as instruções abaixo:

1. Clone o repositório para o seu ambiente local:
```git clone https://github.com/rr0gerio/access-profile-manager.git```

2. Navegue até o diretório do projeto:
```cd access-profile-manager```

3. Crie e ative um ambiente virtual:
```
python -m venv myenv # Crie o ambiente virtual
myenv\Scripts\activate # Ative o ambiente virtual (Windows)
source myenv/bin/activate # Ative o ambiente virtual (Linux/macOS)
```

4. Instale as dependências do projeto:
```pip install .```

5. Execute o projeto:
```python main.py```

6. Quando terminar, desative o ambiente virtual:
```deactivate```
## Criação de Executável (.exe)

Você pode criar um executável para o projeto usando a biblioteca PyInstaller. Certifique-se de ter ativado o ambiente virtual antes de prosseguir com os seguintes passos:

1. Instale a biblioteca PyInstaller:
```pip install pyinstaller```

2. Navegue até o diretório do projeto:
```cd access-profile-manager```

3. Crie o executável:
```pyinstaller main.py --onefile --name access-profile-manager```

Isso criará um executável chamado `access-profile-manager.exe` na pasta `dist/`. Você pode executar este arquivo para usar o projeto sem precisar do Python instalado.