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

    def search_sample(self, **filters):
        """
        Поиск образцов по критериям
        filters: Поля и их значения для фильтрации.
        return: Список подходящих образцов.
        """
        result = []
        for sample in self.samples.values():
            match = True
            for field, value in filters.items():
                if getattr(sample, field) != value:
                    match = False
                    break
            if match:
                result.append(sample)
        return result

    def edit_sample(self, sample_id, **changes):
        """
        Редактирует поля образца по ID.
        sample_id: ID образца.
        changes: Поля и их новые значения.
        return: True, если успешно, инчае False.
        """
        if sample_id in self.samples:
            sample = self.samples[sample_id]
            for field, value in changes.items():
                setattr(sample, field, value)
            return True
        return False
