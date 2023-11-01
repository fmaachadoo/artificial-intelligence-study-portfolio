# Discussões sobre resolução de problemas por busca

## Sugestões de Aprimoramento

1. **Algoritmos Híbridos**: Combinar diferentes tipos de algoritmos de busca pode fornecer um meio termo entre eficácia e eficiência. Por exemplo, usar algoritmos genéticos para explorar o espaço de busca e em seguida refinar os resultados com Busca Local.

2. **Aprendizado de Máquina para Heurísticas**: Utilizar técnicas de aprendizado de máquina para gerar heurísticas adaptativas pode melhorar o desempenho dos algoritmos de busca informada.

3. **Modelos Probabilísticos**: Incorporar modelos probabilísticos para lidar com incerteza pode tornar os algoritmos mais robustos em ambientes dinâmicos e incertos.

4. **Paralelismo e Distribuição**: Técnicas de computação paralela podem ser aplicadas para melhorar a eficiência computacional, tornando os algoritmos mais práticos para aplicações em tempo real.

5. **Otimização Multiobjetivo**: Adaptar algoritmos para considerar múltiplos objetivos pode torná-los mais versáteis e aplicáveis a uma gama mais ampla de problemas.

> Enquanto os algoritmos de busca continuam sendo uma parte vital da caixa de 
> ferramentas de IA, há espaço substancial para melhorias. Abordagens 
> interdisciplinares que combinam teoria da otimização, aprendizado de máquina e 
> métodos estatísticos são particularmente promissoras para abordar as limitações 
> existentes e levar a eficácia desses algoritmos a novos patamares.


## Heurística adicional

Uma técnica muito utilizada em IA que talvez esteja relacionado com este 
assunto seja o cálculo do gradiente descendente.
O Gradiente Descendente é uma técnica de otimização usada para encontrar o 
mínimo local de uma função. Embora não seja um algoritmo de busca no sentido 
tradicional, ele tem algumas semelhanças e diferenças importantes em relação 
aos algoritmos de busca, especialmente no contexto da Inteligência Artificial.

#### Relação com Algoritmos de Busca

1. **Objetivo de Otimização**: Tanto os algoritmos de busca quanto o Gradiente 
Descendente visam encontrar soluções ótimas ou aproximadas para um determinado 
problema. No caso dos algoritmos de busca, o objetivo é frequentemente 
encontrar o caminho mais curto ou de menor custo, enquanto o Gradiente 
Descendente busca minimizar uma função de custo.

2. **Espaço de Soluções**: Ambos operam em um espaço de soluções definido, mas 
enquanto os algoritmos de busca geralmente trabalham em espaços discretos 
(como um grafo ou uma árvore), o Gradiente Descendente opera em espaços 
contínuos.

3. **Informação Local vs. Global**: O Gradiente Descendente utiliza informações 
locais sobre a inclinação da função de custo para se mover em direção ao 
mínimo. Isso é semelhante a algoritmos de busca local como o **Hill Climbing**, 
que também fazem movimentos locais para encontrar uma solução ótima.

4. **Heurísticas**: Em algoritmos de busca informada, as heurísticas são usadas
 para guiar a busca. No Gradiente Descendente, o próprio gradiente atua como 
 uma espécie de "heurística", direcionando o algoritmo para onde a função 
 decresce mais rapidamente.

# Bibliografia

https://pt.d2l.ai/chapter_optimization/sgd.html

http://cursos.leg.ufpr.br/ML4all/apoio/Gradiente.html

https://didatica.tech/gradiente-descendente-estocastico/