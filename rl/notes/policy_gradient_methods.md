<h2> Policy Gradient methods </h2>


Policy gradient methods attempt to learn a parameterized policy $\pi(a_{t}|s_{t};\theta)=P({a_{t}|s_{t};\theta)}$ directly, such that:
 $$\theta=\argmax_{\theta} \mathbb{E}_{\pi_{\theta}}[\sum_{t=0}^{T} \gamma^{t}r_{t}]$$

To derive a function we can maximize by gradient descent, we use the Log-Derivative trick, that is:
$$
\nabla\mathbb{E}[f(x)]=\nabla_{\theta} \int_{\theta}p(x)f(x)dx = \int \nabla_{\theta} p_{\theta}(x) f(x) dx = \int \frac{p_{\theta}(x)}{p_{\theta}(x)} \nabla_{\theta} p_{\theta}(x) f(x) dx = \int p_{\theta}(x) \nabla_{\theta} \log p_{\theta}(x) f(x) dx
$$

So in the case of the expectation above, this implies:
$$
\nabla_{\theta}\mathbb{E_{\pi_{\theta}}}
$$




- [A useful link deriving most of the relevant equations](https://danieltakeshi.github.io/2017/03/28/going-deeper-into-reinforcement-learning-fundamentals-of-policy-gradients/)