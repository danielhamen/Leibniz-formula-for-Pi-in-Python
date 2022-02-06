def Leibniz(Accuracy=1000000):
    """
    Returns digits of Pi based off of the Gregory-Leibniz Formula

    args:
        Accuracy (int): The accuracy of the result. Higher values will return a more precise value, but will take longer (Recomended is at least 1000000 for a semi-precise result)
    """

    Denominator = 1
    AddTo = 1

    for i in range(0, Accuracy):
        Denominator = Denominator + 2
        AddTo = AddTo - (1/Denominator)
        Denominator = Denominator + 2
        AddTo = AddTo + (1/Denominator)

    Pi = AddTo * 4

    return(Pi)
