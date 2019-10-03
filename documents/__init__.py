class Document:
    def __init__(self):
        self._exercises = list()
        self._title = ''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title:str):
        self._title = title

    def add_exercise(self, ex:dict):
        """
        {description: str, pattern:[]}
        :param ex:
        :return:
        """
        self._exercises.append(ex)

    def generate_tex(self):
        document = list()
        document.append('\\documentclass[a4paper, 12pt, twocolumn, '
                                   'twoside]{article}')
        document.append("\\usepackage[utf8]{inputenc}")
        document.append("\\usepackage{natbib}")
        document.append("\\usepackage{graphicx}")
        document.append("\\usepackage[hangul]{dhucs}")
        document.append("\\begin{document}")
        for ex in self._exercises:
            document.append("\\paragraph{%s}" % (ex['description']))
            document.append("\\begin{enumerate}")
            for q in ex['pattern']:
                document.append("\\item ${}=$".format(q[0]))
            document.append("\\end{enumerate}")

        document.append('\\newpage')
        document.append('정답\\\\')
        for ex in self._exercises:
            document.append("{}\\\\".format(ex['description']))
            answer = list()
            for i, q in enumerate(ex['pattern'], 1):
                answer.append("({})${}$".format(i, q[1]))
            document.append(', '.join(answer))
            document.append('\\newline')
            document.append('\\newline')
        document.append("\\end{document}")


        return '\n'.join(document)







