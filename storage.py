import json
from sample import BiologicalSample
from manager import SampleManager


def save_to_file(manager, filename='data.json'):
    """
    Сохраняет все образцы из SampleManager в JSON-файл.
    """
    samples_list = []

    for sample in manager.samples.values():
        samples_list.append(sample.__dict__)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(samples_list, file)


def load_from_file(filename='data.json'):
    """
    Загружает образцы из JSON-файла и возвращает SampleManager.
    Если файла нет, возвращает ошибку FileNotFoundError.
    """
    manager = SampleManager()
    try:
        with open(filename, 'r') as file:
            samples_data = json.load(file)

            for sample_dict in samples_data:
                sample = BiologicalSample(
                    sample_id=sample_dict['sample_id'],
                    name=sample_dict['name'],
                    type=sample_dict['type'],
                    collection_date=sample_dict['collection_date'],
                    location=sample_dict['location'],
                    notes=sample_dict.get('notes', '')
                )
                manager.add_sample(sample)

    except FileNotFoundError:
        pass

    except json.JSONDecodeError:
        print('Ошибка: файл повреждён')
        return SampleManager()

    return manager
