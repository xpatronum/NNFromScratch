![Page_1_1](./images/_Page_1_1.png)
![Page_1_2](./images/_Page_1_2.png)

#### *`Y=forward_propagation(X)` для FullyConnected слоя*
![_FCLayer_forward_propagation](./images/__FCLayer_forward_propagation.png)

#### *Архитектура и функция ошибки*
Ниже представлена архитектура слоев и уравнение `(5)` для вычисления выходного слоя `FullyConnectedLayer`

![Page_2](./images/Page_2_bestVersion.JPG)

_Каждый слой (`FCLayer` или `ActivationLayer`) принимает входные данные - `X`, и выдает выход - `Y`._
![forard_propagation](./images/forward_propagation.png)

_Обратите внимание, что выход каждого слоя - является входом для другого, поэтому в целом процесс `Y = forward_propagation(X)`
выглядит следующим образом_
![sequential_forward_propagation](./images/sequential_forward_propagation.png)

_В коде это выглядит следующим образом._ 

Для `FCLayer`
![FCLayer_code_fp](./images/FCLayer_forward_propagation.png)

Для `ActivationLayer`
![ActivationLayer_code_fp](./images/ActivationLayer_forward_propagation.png)


#### *MSE или среднеквадратичное отклонение*
_В качестве примера, в нашей нейросети будет использоваться функция ошибки `(6)` - среднеквадратичное отклонение_

![Page_3](./images/ChainRuleProblem.JPG)

_Как только входной вектор `X` прошел все трансформации слоев - на выходе имеем вектор `Y`,
от которого считаем функцию ошибки `(6)`, и начиная с этого момента нам нужно как-то обновить веса нейрости (параметры), чтобы
минимизировать функцию ошибки. Здесь приходит на помощь..._
#### *Метод градиентного спуска*

![gradient_descent](./images/gradient_descent.png)

Обратите внимание, что теперь процесс идет в обратную сторону: выход слоев стал входом, а входы, наоборот, выходами
`∇L(X) = backward_propagation(∇L(Y), α)`, см. ниже
![sequential_backward_propagation](./images/sequential_backward_propagation.png)

#### *Применим теорему о дифференцированиии сложной функции...*

![Page_4](./images/ChainRuleWithGraphics.JPG)

#### *Вывод формул обратного распространения ошибки для слоя `FCLayer`*

![FCLayer_derivation_bp_1](./images/FCLayer_backward_propagation_derivation_1.JPG)

*Продолжение вывода на следующей странице*

![FCLayer_derivation_bp_2](./images/FCLayer_backward_propagation_derivation_2.JPG)

_Таким образом получаем итоговые формулые для реализации_ `backward_propagation()` слоя `FCLayer`
![FCLayer_end_bp](./images/FCLayer_bp_end.png)

_Реализация в виде кода представленана ниже_
![FCLayer_code_bp](./images/FCLayer_code_bp.png)

#### *Вывод формул обратного распространения ошибки для слоя `ActivationLayer`*

![ActivationLayer_derivation_bp_1](./images/ActivationLayer_bp_derivation_1.JPG)

*Продолжение вывода на следующей странице*

![ActivationLayer_derivation_bp_2](./images/ActivationLayer_bp_derivation_2.JPG)

_Реализация в виде кода представлена ниже_
![ActivationLayer_code_bp](./images/ActivationLayer_code_bp.png)


The end.