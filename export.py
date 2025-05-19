from openpyxl import Workbook
from docx import Document
from typing import List
from sample import BiologicalSample
import csv
import json


def export_to_excel(samples: List[BiologicalSample], filename: str = "samples.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Образцы"
    # Добавьте заголовки и данные
    # ...
    wb.save(filename)


def export_to_word(samples: List[BiologicalSample], filename: str = "samples.docx"):
    doc = Document()
    # Добавьте заголовок документа
    for sample in samples:
        # Добавьте данные каждого образца
        pass
    doc.save(filename)


def export_to_csv(samples: List[BiologicalSample], filename: str = "samples.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Запишите заголовки и данные
