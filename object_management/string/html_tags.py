class Html5Tags:
    """HTML open and close tags generator.

    The main goal of this class is accessibility and
    easy use for HTML generation."""
    __instance = None

    def __init__(self):
        """This class works as a singleton."""
        if Html5Tags.__instance is not None:
            raise Exception("Use this class as singleton!")
        else:
            Html5Tags.__instance = self
        self.__left = '<'
        self.__right = '>'
        self.__left_close = '</'
        self.__right_close = '/>'

    @staticmethod
    def get_tagger():
        """Get this class instance."""
        if Html5Tags.__instance is None:
            Html5Tags()
        return Html5Tags.__instance

    def __generic(self, tag, string, **style):
        """Generate the tag.

        :param tag: for open and closing.
        :param string: contents inside the tag.
        :param style: styles the tag might receive.
        :return: tagged string like <table border='1'>...</table>
        """
        if string:
            add_values = ' '.join([key+'='+'"'+style[key]+'"' for key in style])
            return self.__left + tag + ' ' + add_values + self.__right + \
                string + self.__left_close + tag + self.__right
        else:
            return self.__left + tag + self.__right_close

    def h1(self, string, **style):
        return self.__generic(self.h1.__name__, string, **style)

    def h2(self, string, **style):
        return self.__generic(self.h2.__name__, string, **style)

    def h3(self, string, **style):
        return self.__generic(self.h3.__name__, string, **style)

    def h4(self, string, **style):
        return self.__generic(self.h4.__name__, string, **style)

    def table(self, string, **style):
        return self.__generic(self.table.__name__, string, **style)

    def tr(self, string, **style):
        return self.__generic(self.tr.__name__, string, **style)

    def th(self, string, **style):
        return self.__generic(self.th.__name__, string, **style)

    def td(self, string, **style):
        return self.__generic(self.td.__name__, string, **style)

    def pre(self, string, **style):
        return self.__generic(self.pre.__name__, string, **style)

    def br(self, string, **style):
        return self.__generic(self.br.__name__, string, **style)
