CLICK_BATTLE
**
Aplicação:**

  Aplicação de uma página web simples com dois botões que incrementam toda vez que sáo clicados. 
  A aplicação foi feita para que fosse realizado um trabalho de Cultura DevOps, do curso de pós Graduação de Engenharia de Software e Teste de Software da PUC.
  O intuito do trabalho é entender os conceitos do github actions e criar um workflow de testes de CI CD.
  
  É utilizado o docker compose para criar e gerenciar um container de Redis, que foi escolhido devido sua simplicidade e rapidez.
**
CI e CD:**

   Os passos para a execução de testes, que se encontram dentro do arquivo ci-cd.yml, são:
  
     -  Baixar o código
     -  Configurar python
     -  Instalar as dependências
     -  Subir docker compose
     -  Executar os testes

    
**Como os testes foram implementados:**

  O teste unitário vai fazer a verificação de todo html da aplicação. Esse teste receberá dois argumentos, que serão os valores dos dois botões da aplicação, que incrementam quando acionados. 
  Foram passados os argumentos 1 e 2, e espera-se que dentro do html seja encontrado o valor <p>1:2</p>\n. 

  Os testes de integração são 3:

      - test_main_page -> Irá acesar o index, e fazer o teste de que dentro do html, tem a string ("<p>0:0</p>").
      - test_click_left -> Ele também irá  acesar o index, e fazer o teste de que dentro do html, tem a string "<p>0:0</p>". 
          Logo após, irá fazer um post, para clicar no botão "click_left", que vai incrementar +1. 
          Dessa forma, a verificação que o teste terá que fazer, é que a string (<p>1:0</p>) está contida no html.
      - test_click_right -> Vai realizar os mesmos testes que o test_click_right, porém para o botão direito. 

**Como a pipeline CI/CD funciona: **

  O workflow vai baixar o código, configurar o python, instalar as dependências, subir o docker compose e logo em seguida executar o comando "pytest", que irá primeiro executar o teste unitário, seguido dos de integração.


Caso seja alterado algo no html, os testes irão falhar. 
