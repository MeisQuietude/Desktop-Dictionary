import random
import re
import json
import codecs


def add_tdict(en:dict, ru:dict):
    """ Добавление в словарь новых слов"""
    print('Введите словосочетание в строгом порядке: {english русское}')
    print('Например: cat кошка')
    print('-1, если закончили')
    while True:
        k = len(en) + 1
        words = input().lower().split()
        if '-1' in words: break
        en.__setitem__(k, words[0])
        ru.__setitem__(k, words[1])
        del words
    return en, ru


def show_dict(language='eng'):
    """ Показать существующий словарь (rus/eng) """
    if language.lower().startswith('en') or language.lower().startswith('анг'):
        return EN
    if language.lower().startswith('ru') or language.lower().startswith('ру'):
        return RU
    return print(EN, RU)


def rules():
    """ Выбор действия """
    rule = input('Просмотреть словарь: показать / show\n'
             'Добавить новые слова в словарь: add\n'
             'Перейти к тестированию: test\n\n')
    return rule


def rule_test():
    """ Выбор режима теста """
    mode = input('Русский, английский или микс?\n')
    while mode != 'rus' or mode != 'eng' or mode != 'mix':
        mode = mode.lower()
        if mode.startswith('ру') or mode.startswith('ru'):
            mode = 'rus'
        elif mode.startswith('en') or mode.startswith('en'):
            mode = 'eng'
        elif mode.startswith('m') or mode.startswith('м'):
            mode = 'mix'
        else:
            mode = input('Попробуйте ещё раз\n')
    return mode


def rule_add():
    """ Добавление в словарь"""
    return add_tdict(EN,RU)


def rule_show():
    """ Показать словарь """
    return show_dict(rule)


def rule_choice(rule):
    """ Техническая часть """
    if rule.lower().startswith('te') or rule.lower().startswith('те'):
        mode = rule_test()
        return start_test_mix(EN,RU) if mode == 'mix' else start_test(mode,EN,RU) # return 'mode'
    if rule.lower().startswith('sh') or rule.lower().startswith('пок'):
        return rule_show()     # return 'RU and/or EN'
    if rule.lower().startswith('ad') or rule.lower().startswith('доб'):
        return rule_add()      # return 'new EN and RU'


def import_dict():
    """ Импорт Словарь.txt """
    with codecs.open('../config/dictionary_en.json', 'r', encoding='utf-8') as f:
        EN = json.load(f)
    with codecs.open('../config/dictionary_ru.json', 'r', encoding='utf-8') as f:
        RU = json.load(f)
    return EN, RU


def export_dict(_en:dict,_ru:dict):
    """ Экспорт Словарь.txt """
    with codecs.open('../config/dictionary_en.json', 'w', encoding='utf-8') as f:
        json.dump(_en, f, ensure_ascii=False)
    with codecs.open('../config/dictionary_ru.json', 'w', encoding='utf-8') as f:
        json.dump(_ru, f, ensure_ascii=False)


def start_test_mix(dict_en, dict_ru):
    """ Старт комбинированного теста """
    pass


def start_test(mode, dict_en, dict_ru):
    """ Старт теста (input mode, eng dict and rus dict """
    pass


if __name__ == "__main__":
    # print('Learning English with (c) Quietude\n\n')

    tuple_rules = ('ad')

    EN,RU = import_dict()               # return dictionary
    while True:
        rule = rules()                  # return test(rus\eng\mix)/add_td/show_d
        to_do = rule_choice(rule)       # переменная to_do

        if rule.lower().startswith('ad') or rule.lower().startswith('доб'):
            EN,RU = to_do               # return new EN,RU dictionary
            export_dict(EN,RU)
        elif rule.lower().startswith('te') or rule.lower().startswith('те'): None
        elif rule.lower().startswith('sh') or rule.lower().startswith('пок'): None
        else:
            print('Попытайтесь снова')
            continue