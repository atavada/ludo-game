# dado-3D
Simples simulação de um dado em 3D usando PyOpenGL

#Opções de argumentos para linha de comando

Existem duas opções de argumentos implementadas ao executar o programa via linha de comando.  

 - _**slow**_: carrega as imagens dentro da pasta ```texture-slow```, as quais são mais pesadas e por isso podem resultar em diminuição da qualidade do gráfico e do processo de rotação.

 - _**fast**_: carrega as imagens dentro da pasta ```texture-fast```, as quais são mais leves e apresentam boa performance. Essa é a opção padrão de processamento das imagens, caso nenhum argumento seja inserido.

Portanto, o programa pode ser executado de três maneiras diferentes:

  ```python dice.py slow```  
  ```python dice.py fast```  
  ```python dice.py```

PS.: o processo de lançamento do dado para a obtenção de números aleatórios será implementado em breve. 
