def Dividir(a:float, b:float) -> float:
    """
    Calcula el cociente de a entre b.
    
    Parameters (Args)
    ----------
    a : float
        Numerador.
    b : float
        Denominador.
    
    Returns
    -------
    float
        El resultado de dividir a entre b.
        
    Raises
    ------
    ZeroDivisionError
        Si el denominador es cero.
    TypeError
        Si algún operando no es un valor numérico.
         
|    Examples
    --------
    >>> Dividir(5,3)
    1.6666666666666667
    >>> Dividir(8,0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a/b
