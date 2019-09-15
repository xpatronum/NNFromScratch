![Page_1_1](./images/_Page_1_1.png)
![Page_1_2](./images/_Page_1_2.png)

#### *`Y=forward_propagation(X)` для FullyConnected слоя*
![_FCLayer_forward_propagation](./images/__FCLayer_forward_propagation.png)

#### *Архитектура слоев*

![_ArchitectureLayer](./images/_ArchiterctureLayer.png)

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

![_LossFunctionMSE](./images/_LossFunctionMSE.png)

_Как только входной вектор `X` прошел все трансформации слоев - на выходе имеем вектор `Y`,
от которого считаем функцию ошибки `(6)`, и начиная с этого момента нам нужно как-то обновить веса нейрости (параметры), чтобы
минимизировать функцию ошибки. Здесь приходит на помощь..._
#### *Метод градиентного спуска*

![gradient_descent](./images/gradient_descent.png)

Обратите внимание, что теперь процесс идет в обратную сторону: выход слоев стал входом, а входы, наоборот, выходами
`∇L(X) = backward_propagation(∇L(Y), α)`, см. ниже
![sequential_backward_propagation](./images/sequential_backward_propagation.png)
![_LossFunctionMSE2](./images/_LossFunctionMSE_2.png)


#### *Вывод формул обратного распространения ошибки для слоя `FCLayer`*

![FCLayer_derivation_bp_1](./images/_ChainRuleApplicationFCLayer.png)
![FCLayer_derivation_bp_2](./images/_ChainRuleApplicationFCLayer_2.png)
![FCLayer_derivation_bp_3](./images/_ChainRuleApplicationFCLayer_3.png)


_Таким образом получаем итоговые формулые для реализации_ `backward_propagation()` слоя `FCLayer`
![FCLayer_end_bp](./images/FCLayer_bp_end.png)

_Реализация в виде кода представленана ниже_
![FCLayer_code_bp](./images/FCLayer_code_bp.png)

#### *Вывод формул обратного распространения ошибки для слоя `ActivationLayer`*

![ActivationLayer_derivation_bp_1](./images/_ChainRuleApplicationActivationLayer.png)
![ActivationLayer_derivation_bp_2](./images/_ChainRuleApplicationActivationLayer_2.png)

_Реализация в виде кода представлена ниже_
![ActivationLayer_code_bp](./images/ActivationLayer_code_bp.png)

![TheEnd](./images/TheEnd.png)
####*Связаться со мной:*
* [Vk](https://vk.com/mrtwistermrfreeman)
* [Twitter](https://twitter.com/IgorTarlinskii)
* [Facebook](https://www.facebook.com/igor.tarlinskii)
* [Telegram](@MrTwisterMrFreeman)