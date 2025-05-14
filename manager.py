from sample import BiologicalSample


class SampleManager:
    def __init__(self):
        self.samples = {}

    def add_sample(self, sample: BiologicalSample):
        """
        Добовляет образец в коллекцию.
        Если образец с таким ID уже существует, вызывает ValueError.
        """
        if sample.id in self.samples:
            raise ValueError(f'Образец с ID {sample.id} уже существует')
        self.samples[sample.id] = sample

    def delete_sample(self, sample_id):
        """
        Удаляет образец по ID.
        Возвращает True, если образец был удалён, и False, если не найден.
        """
        if sample_id in self.samples:
            self.samples.pop(sample_id)
            return True
        return False
