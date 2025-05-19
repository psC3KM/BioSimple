class BiologicalSample:
    def __init__(self, sample_id, name, sample_type,
                 collection_date, location, notes=''):
        """
        Конструктор класса.
        sample_id: Уникальный интедификатор образца (число или строка).
        name: Название образца.
        sample_type: Тип образца.
        collection_date: Дата сбора образца в формате 'DD.MM.YYYY'.
        location: Место сбора.
        notes: Дополнительные заметки.
        """
        self.sample_id = sample_id
        self.name = name
        self.type = sample_type
        self.collection_date = collection_date
        self.location = location
        self.notes = notes

    def __str__(self):
        """
        Возвращает строковое представление образца.
        """
        return (
            f'Образец №{self.id}: {self.name} ({self.type}),'
            f' собрано {self.collection_date} в {self.location}'
        )


if __name__ == '__main__':
    sample = BiologicalSample(
        sample_id=1,
        name='',
        sample_type='',
        collection_date='',
        location='',
        notes='.'
    )
    print(sample)
