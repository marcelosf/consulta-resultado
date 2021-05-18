import io
import csv
import chardet


class CsvExtractor:
    def __init__(self, file, skip_first_line=True):
        self.file = file
        self.skip_first_line = skip_first_line
        self.participantes = list()

    def get_participantes(self):
        try:
            self.read_file(encoding='utf-8')
        except:
            self.read_file(encoding='latin1')
        
        return self.participantes
    
    def read_file(self, encoding):
        with open(self.file, newline='', encoding=encoding) as csvfile:
            spamreader = csv.reader(csvfile)
            spamreader = self.skip_line(spamreader)
            self.append_participantes(spamreader)

    def skip_line(self, spamreader):
        if self.skip_first_line:
            spamreader = iter(spamreader)
            next(spamreader)
        return spamreader

    def append_participantes(self, spamreader):
        for row in spamreader:
            self.participantes.append({
                'posicao': int(row[0]),
                'nome': row[1],
                'status': row[2]
            })
