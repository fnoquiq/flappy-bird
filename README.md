# Flappy Bird

![GIF-Exemplo-Gameplay](https://github.com/fnoquiq/flappy-bird/blob/master/gameplay-example.gif)

---

### Tecnologias utilizadas

* Python 3.7.5
* PIP 19.2.3
* PyGame 2.0.0 (dev6)

---

### Instalação

Primeiramente verifique se o Python está instalado no seu computador:

`$ python --version` ou `$ python3 --version`

Isto deve retornar a seguinte mensagem:

`Python 3.7.5`

Posteriormente, verifique se o PIP (gerenciador de pacotes do Python) está instalado no seu computador:

`$ pip --version` ou `$ pip3 --version`

Espera-se que retorne algo como seguinte mensagem:

`$ pip 19.2.3 from /Users/gabriel-macbook/Desktop/flappy-bird/myenv/lib/python3.7/site-packages/pip (python 3.7)`

Antes de começar, é bom criar um ambiente virtual para fazer a instalação dos pacotes na versão
correta do projeto, isso para tentar ao máximo, não poluir o seu pc com pacotes e dependências variadas.

Com isso, execute os comandos para instalar o python-venv:

`$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev `

`$ sudo apt install -y python3-venv `

Com o python-venv instalado, crie o seu ambiente dentro do projeto

`$ python3 -m venv myEnv `

Para ativar, execute:

`$ source myEnv/bin/activate `

Feito isso, resta somente instalar as dependências usando:

`$ pip install -r requirements.txt`
