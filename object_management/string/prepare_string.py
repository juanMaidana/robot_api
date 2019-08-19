def prepare_string(string, *replacements):
    """Prepare string according to enumerated replacements

    Example: prepare_string('$R(0)_project_$R(1)', vipre, datetime).
    Return example: 'vipre_project_datetime'.
    :param string, always use '$R(<number>)' for value to be replaced.
    :param replacements, should have a format [R0,.., Rn].
    :returns: string with values replaced.
    """
    for i in range(0, len(replacements)):
        string = string.replace("$R(" + str(i) + ")", replacements[i])
    return string
