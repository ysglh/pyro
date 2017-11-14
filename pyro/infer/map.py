from pyro import poutine
from pyro.infer.svi import SVI


def MAP(model, optim, *args, **kwargs):
    """
    :param model: the model (callable containing Pyro primitives)
    :param optim: a wrapper for a PyTorch optimizer
    :type optim: pyro.optim.PyroOptim

    Maximum A Posteriori inference.

    MAP inference is useful for finding point estimates of latent variables.
    This implementation uses ``poutine.lower`` to replace each ``pyro.sample``
    site in a model with a ``pyro.param`` site for optimization plus a
    ``pyro.observe`` site to represent the prior. To perform Maximum
    Likelihood inference for a variable, create that variable using a
    ``pyro.param`` statement rather than a ``pyro.sample`` statement.
    """
    model = poutine.lower(model)

    def guide(*args, **kwargs):
        pass

    return SVI(model, guide, optim, loss="ELBO", *args, **kwargs)
