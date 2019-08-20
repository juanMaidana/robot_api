from json import dumps, loads
from object_management.string.html_tags import Html5Tags

__tagger = Html5Tags.get_tagger()


def str_html(data):
    """Format a string for html.

    Initially this function is only checking if a dict is present as data.
    Formats that dict for a pretty print on HTML."""
    try:
        data = loads(data)
    except (ValueError, TypeError):
        pass
    if isinstance(data, dict):
        try:
            return __tagger.pre(dumps(data, indent=4)
                                .replace('\n', __tagger.br(False)))
        except ValueError:
            pass
    return str(data)


def function_log_table(html, func, *args, **kwargs):
    """Prepare a function and arguments for logs printing.

    :param html: Return an html table format or simple data.
    :param func: The base function to generate table headers.
    :param args: Arguments the function is receiving.
    :param kwargs: Keyword arguments the function is receiving.
    :return: HTML table format or simple string format.
    """
    headers = func.__code__.co_varnames
    func_name = '"' + func.__name__ + '"'
    if html:
        title = __tagger.h4(func_name)
        head = __tagger.tr(''.join([__tagger.th(str_html(i)) for i in headers]))
        body = __tagger.tr(''.join([__tagger.td(str_html(i)) for i in args] +
                                   [__tagger.td(str_html(kwargs[i])) for i in kwargs]))
        return title + __tagger.table(head + body, border="1")
    else:
        return func_name + '\n' + \
               '\n'.join([str(headers[i]) + ' | ' + str(args[i])
                          for i in range(len(headers))])
