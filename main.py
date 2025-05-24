from sample import BiologicalSample
from storage import load_from_file, save_to_file
from export import (
    export_to_excel,
    export_to_word,
    export_to_csv,
    export_to_json
    )
import re


def add_sample_menu(manager):
    """
    Меню добавление нового биологического образца.

    Args:
        manager (SampleManager): Объект для работы с коллекцией образцов.

    Просит пользователя ввести:
    - Уникальный ID
    - Название образца
    - Тип образца
    - Дату сбора (в формате ДД.ММ.ГГГГ)
    - Место сбора
    - Опциональные примечание

    Проверяет:
    - Уникальность ID
    - Корректность формата даты
    """
    print('Добавление образца')
    try:
        sample_id = int(input('ID: '))
        if sample_id in manager.samples:
            print(f'Ошибка: образец с ID {sample_id} уже существует')
            return

        name = input('Название: ')
        sample_type = input('Тип: ')

        date = input('Дата сбора (формат даты: ДД.ММ.ГГГГ): ')
        if not re.match(r'\d{2}\.\d{2}\.\d{4}', date):
            print('Ошибка: неверный формат даты')
            return

        location = input('Место сбора: ')

        notes = ''
        while True:
            add_notes = input('Добавить примечание?(Да/Нет): ').strip().lower()
            if add_notes == 'да':
                notes = input('Введите примечание: ').strip()
                break
            elif add_notes == 'нет':
                notes = ''
                break
            else:
                print('⚠ Пожалуйста, введите "Да" или "Нет"')

        sample = BiologicalSample(
            sample_id=sample_id,
            name=name,
            sample_type=sample_type,
            collection_date=date,
            location=location,
            notes=notes
        )
        manager.add_sample(sample)
        save = input('Сохранить изменения? (Да/Нет):').lower()
        if save == 'Да':
            save_to_file(manager)
        print('✅ Образец добавлен и данные сохранены!')
    except ValueError as e:
        print(f'Ошибка: {e}')


def search_sample_menu(manager):
    """
    Меню поиска образца по ID
    """
    print('\nПоиск образца по ID')
    try:
        sample_id = int(input('Введите ID образца: '))
        sample = manager.search_sample(sample_id)

        if sample:
            print('\nНайден образец:')
            print(sample)
        else:
            print(f'\nОбразец с ID {sample_id} не найден')
    except ValueError:
        print('Ошибка: ID должен быть числом')


def export_menu(manager):
    """
    Меню экспорта данных, в разные форматы.

    Args:
        manager (SampleManager): Объект работы с данными для экспорта.

    Поддерживаемые форматы:
    - Excel (.xlsx)
    - Word (.docx)
    - CSV
    - JSON

    При отсутствии данных выводит предупреждение.
    """
    print('\nЭкспорт данных')
    if not manager.samples:
        print('Нет данных для экспорта!')
        return

    print('1. Excel\n2. Word\n3. CSV\n4. JSON\n5. Назад')
    choice = input('Выберите формат: ')
    filename = input('Введите имя файла (без ресширения)')

    if choice == '1':
        export_to_excel(manager.samples.values(), filename=f'{filename}.xlsx')
        print('Данные экспортированы в samples.xlsx')
    elif choice == '2':
        export_to_word(manager.samples.values(), filename=f'{filename}.docx')
        print('Данные экспортированы в samples.docx')
    elif choice == '3':
        export_to_csv(manager.samples.values(), filename=f'{filename}.csv')
        print('Данные экспортированы в samples.csv')
    elif choice == '4':
        export_to_json(manager.samples.values(), filename=f'{filename}.json')
        print('Данные экспортированы в samples.json')
    elif choice == '5':
        return
    else:
        print('Выбранный вами пункт не существует. Пожалуйста выберете другой')


def main():
    """
    Основная функция, запускающая консольное меню управление
    биологическими образцами.

    Загружает данные из файла при старте и предоставляет интерфейс для:
    - Добавление новых образцов
    - Поиска существующих
    - Экспорта данных
    - Сохранения при выходе
    """
    manager = load_from_file()

    while True:
        print('\n=== Меню ===')
        print('1. Добавить образец')
        print('2. Поиск образца')
        print('3. Экспорт данных')
        print('4. Выйти')

        choice = input('Выберите пункт: ')

        if choice == '1':
            add_sample_menu(manager)
        elif choice == '2':
            search_sample_menu(manager)
        elif choice == '3':
            export_menu(manager)
        elif choice == '4':
            save_to_file(manager)
            break
        else:
            print('Ошибка: Такого пункта нет')


if __name__ == '__main__':
    main()
