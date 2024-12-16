import pytest

from services.API_AI_Choice.AI.answer_model import QASystem, convert_tag_to_answer
import datetime

model = QASystem()

# Выпускникам  специальности 09.02.01
def test_predict_model_090201_1():
    question = "какую специальность я получу отучившись на компьютерные системы и комплексы"

    true_response = "Выпускникам  специальности 09.02.01 Компьютерные ситемы и комплексы присваивается квалификация Техник по компьютерным системам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_090201_2():
    question = "Какая квалификация будет у меня после окончания обучения по специальности Компьютерные системы и комплексы 09.02.01?"

    true_response = "Выпускникам  специальности 09.02.01 Компьютерные ситемы и комплексы присваивается квалификация Техник по компьютерным системам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_090201_3():
    question = "Кем я стану после окончания обучения по специальности 09.02.01 "

    true_response = "Выпускникам  специальности 09.02.01 Компьютерные ситемы и комплексы присваивается квалификация Техник по компьютерным системам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_090201_4():
    question = "Какую специальность я получу, закончив обучение по направлению Компьютерные системы и комплексы"

    true_response = "Выпускникам  специальности 09.02.01 Компьютерные ситемы и комплексы присваивается квалификация Техник по компьютерным системам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_090201_5():
    question = "Что я буду уметь по окончанию специальности 09.02.01"

    true_response = "Выпускникам  специальности 09.02.01 Компьютерные ситемы и комплексы присваивается квалификация Техник по компьютерным системам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Оплата обучения

def test_predict_model_education_payment_1():
    question = "как оплатить обучение"

    true_response = "Оплата обучения осуществляется по семестрам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_payment_2():
    question = "Как произвести платеж за обучение"

    true_response = "Оплата обучения осуществляется по семестрам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_payment_3():
    question = "Способы внесения платы за семестр"

    true_response = "Оплата обучения осуществляется по семестрам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_payment_4():
    question = "Способы внесения платы за семестр"

    true_response = "Оплата обучения осуществляется по семестрам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_payment_5():
    question = "Процедура оплаты образовательной программы"

    true_response = "Оплата обучения осуществляется по семестрам"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Начало приёма документов

def test_predict_model_docs_getting_1():
    question = "когда начинается приём документов"

    true_response = "Прием докуменнтов для поступления проходит с 20 июня по 15 августа"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_docs_getting_2():
    question = "В какие сроки осуществляется подача документов"

    true_response = "Прием докуменнтов для поступления проходит с 20 июня по 15 августа"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_docs_getting_3():
    question = "Период начала приема заявлений для абитуриентов"

    true_response = "Прием докуменнтов для поступления проходит с 20 июня по 15 августа"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_docs_getting_4():
    question = "Когда можно подавать документы для поступления"

    true_response = "Прием докуменнтов для поступления проходит с 20 июня по 15 августа"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_docs_getting_5():
    question = "Когда стартует регистрация документов для зачисления"

    true_response = "Прием докуменнтов для поступления проходит с 20 июня по 15 августа"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Начало учебного года
def test_predict_model_education_year_starting_1():
    question = "когда начало учебного года"

    true_response = "Начало учебного года у студентов всех курсов 1 сентября"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_year_starting_2():
    question = "С какой даты стартует учебный год"

    true_response = "Начало учебного года у студентов всех курсов 1 сентября"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_year_starting_3():
    question = "Какого числа начинаются занятия"

    true_response = "Начало учебного года у студентов всех курсов 1 сентября"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_year_starting_4():
    question = "Когда первый день учебного семестра"

    true_response = "Начало учебного года у студентов всех курсов 1 сентября"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_year_starting_5():
    question = "Дата официального старта обучения для студентов"

    true_response = "Начало учебного года у студентов всех курсов 1 сентября"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Место обучения студентов
def test_predict_model_education_place_1():
    question = "где учаться студенты"

    true_response = "Студенты первокусники всех специальностей обучаются по адресу ул. Нежинская д.7. Начиная со  2 курса студенты учатся по двум адресам:ул.Нежинская д. 7 и Нахимовской проспект д.21 в зависимости от расписания"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_place_2():
    question = "Где проходит обучение студентов"

    true_response = "Студенты первокусники всех специальностей обучаются по адресу ул. Нежинская д.7. Начиная со  2 курса студенты учатся по двум адресам:ул.Нежинская д. 7 и Нахимовской проспект д.21 в зависимости от расписания"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_place_3():
    question = "Какие адреса учебных корпусов для студентов"

    true_response = "Студенты первокусники всех специальностей обучаются по адресу ул. Нежинская д.7. Начиная со  2 курса студенты учатся по двум адресам:ул.Нежинская д. 7 и Нахимовской проспект д.21 в зависимости от расписания"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_place_4():
    question = "Расположение мест обучения для студентов"

    true_response = "Студенты первокусники всех специальностей обучаются по адресу ул. Нежинская д.7. Начиная со  2 курса студенты учатся по двум адресам:ул.Нежинская д. 7 и Нахимовской проспект д.21 в зависимости от расписания"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_education_place_5():
    question = "В каких местах занимаются студенты"

    true_response = "Студенты первокусники всех специальностей обучаются по адресу ул. Нежинская д.7. Начиная со  2 курса студенты учатся по двум адресам:ул.Нежинская д. 7 и Нахимовской проспект д.21 в зависимости от расписания"

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Выплата стипендии
def test_predict_model_payment_1():
    question = "выплачивается ли стипендия"

    true_response = "С 1 сентября по 31 декабря государственная академическая стипендия назначается всем студентам первого курса, обучающимся за счёт бюджетных средств. В последующем академическая стипендия назначаются студентам, окончившим семестр только на «хорошо» и «отлично»."

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_payment_2():
    question = "Как происходит начисление стипендии"

    true_response = "С 1 сентября по 31 декабря государственная академическая стипендия назначается всем студентам первого курса, обучающимся за счёт бюджетных средств. В последующем академическая стипендия назначаются студентам, окончившим семестр только на «хорошо» и «отлично»."

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_payment_3():
    question = "Кому и при каких условиях платят стипендию"

    true_response = "С 1 сентября по 31 декабря государственная академическая стипендия назначается всем студентам первого курса, обучающимся за счёт бюджетных средств. В последующем академическая стипендия назначаются студентам, окончившим семестр только на «хорошо» и «отлично»."

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_payment_4():
    question = "Существует ли денежное обеспечение для студентов"

    true_response = "С 1 сентября по 31 декабря государственная академическая стипендия назначается всем студентам первого курса, обучающимся за счёт бюджетных средств. В последующем академическая стипендия назначаются студентам, окончившим семестр только на «хорошо» и «отлично»."

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_model_payment_5():
    question = "Какие условия для получения студенческой стипендии"

    true_response = "С 1 сентября по 31 декабря государственная академическая стипендия назначается всем студентам первого курса, обучающимся за счёт бюджетных средств. В последующем академическая стипендия назначаются студентам, окончившим семестр только на «хорошо» и «отлично»."

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Как добраться до корпусов

def test_predict_how_to_get_buildings_1():
    question = "Как добраться до корпуса на нежинской"

    true_response = 'Главное здание: г. Москва, Нежинская улица, 7. Вариант №1: метро "Славянский бульвар", далее автубусами: 641, 341 \nВариант №2: метро "Давыдково, далее автобусом 325, 329 Вариант №3: метро "Аминьевское шоссе", далее автобусами 274, 325, 329, Вариант №4 метро "Минская", далее автобусом 260\nЗдание 1 Нахимовский пр-т д. 21 Вариант №1: пешком по прямой от метро "Нахимовский проспек; Вариант №2: метро Профсоюзная,тролл. №52. авт. № 219 до остановки "Московский приборостроительный техникум"'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_how_to_get_buildings_2():
    question = "Как проехать к зданию на Нежинской"

    true_response = 'Главное здание: г. Москва, Нежинская улица, 7. Вариант №1: метро "Славянский бульвар", далее автубусами: 641, 341 \nВариант №2: метро "Давыдково, далее автобусом 325, 329 Вариант №3: метро "Аминьевское шоссе", далее автобусами 274, 325, 329, Вариант №4 метро "Минская", далее автобусом 260\nЗдание 1 Нахимовский пр-т д. 21 Вариант №1: пешком по прямой от метро "Нахимовский проспек; Вариант №2: метро Профсоюзная,тролл. №52. авт. № 219 до остановки "Московский приборостроительный техникум"'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_how_to_get_buildings_3():
    question = "Какой маршрут до учебного здания на Нахимоском проспекте"

    true_response = 'Главное здание: г. Москва, Нежинская улица, 7. Вариант №1: метро "Славянский бульвар", далее автубусами: 641, 341 \nВариант №2: метро "Давыдково, далее автобусом 325, 329 Вариант №3: метро "Аминьевское шоссе", далее автобусами 274, 325, 329, Вариант №4 метро "Минская", далее автобусом 260\nЗдание 1 Нахимовский пр-т д. 21 Вариант №1: пешком по прямой от метро "Нахимовский проспек; Вариант №2: метро Профсоюзная,тролл. №52. авт. № 219 до остановки "Московский приборостроительный техникум"'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_how_to_get_buildings_4():
    question = "Какой маршрут до учебного здания на Нахимоском проспекте"

    true_response = 'Главное здание: г. Москва, Нежинская улица, 7. Вариант №1: метро "Славянский бульвар", далее автубусами: 641, 341 \nВариант №2: метро "Давыдково, далее автобусом 325, 329 Вариант №3: метро "Аминьевское шоссе", далее автобусами 274, 325, 329, Вариант №4 метро "Минская", далее автобусом 260\nЗдание 1 Нахимовский пр-т д. 21 Вариант №1: пешком по прямой от метро "Нахимовский проспек; Вариант №2: метро Профсоюзная,тролл. №52. авт. № 219 до остановки "Московский приборостроительный техникум"'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_how_to_get_buildings_5():
    question = "Где находятся корпуса колледжа"

    true_response = 'Главное здание: г. Москва, Нежинская улица, 7. Вариант №1: метро "Славянский бульвар", далее автубусами: 641, 341 \nВариант №2: метро "Давыдково, далее автобусом 325, 329 Вариант №3: метро "Аминьевское шоссе", далее автобусами 274, 325, 329, Вариант №4 метро "Минская", далее автобусом 260\nЗдание 1 Нахимовский пр-т д. 21 Вариант №1: пешком по прямой от метро "Нахимовский проспек; Вариант №2: метро Профсоюзная,тролл. №52. авт. № 219 до остановки "Московский приборостроительный техникум"'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Есть ли питание в столовой

def test_predict_food_in_caffe_1():
    question = "Есть ли питание в столовой"

    true_response = 'В здании техникума на Нахимовском проспекте есть столовая с комплексным питанием, в здании техникума на Нежинской столовой с комплексным питанием нет, но есть буфет. Время работы: c 10-00 до 16-00'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_food_in_caffe_2():
    question = "Какое питание в техникуме"

    true_response = 'В здании техникума на Нахимовском проспекте есть столовая с комплексным питанием, в здании техникума на Нежинской столовой с комплексным питанием нет, но есть буфет. Время работы: c 10-00 до 16-00'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_food_in_caffe_3():
    question = "Как питаются студенты в техникуме"

    true_response = 'В здании техникума на Нахимовском проспекте есть столовая с комплексным питанием, в здании техникума на Нежинской столовой с комплексным питанием нет, но есть буфет. Время работы: c 10-00 до 16-00'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_food_in_caffe_4():
    question = "Есть ли столовая в колледже"

    true_response = 'В здании техникума на Нахимовском проспекте есть столовая с комплексным питанием, в здании техникума на Нежинской столовой с комплексным питанием нет, но есть буфет. Время работы: c 10-00 до 16-00'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_food_in_caffe_5():
    question = "Как можно поесть в техникуме"

    true_response = 'В здании техникума на Нахимовском проспекте есть столовая с комплексным питанием, в здании техникума на Нежинской столовой с комплексным питанием нет, но есть буфет. Время работы: c 10-00 до 16-00'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Возможность прохождения практики за границей


def test_predict_practice_out_of_country_1():
    question = "Могу ли я проходить практику не в российской компании"

    true_response = 'На данный момент нельзя проходить практику за границей.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_practice_out_of_country_2():
    question = "Возможно ли прохождение практики в зарубежной организации"

    true_response = 'На данный момент нельзя проходить практику за границей.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_practice_out_of_country_3():
    question = "Можно ли проходить стажировку в зарубежной фирме"

    true_response = 'На данный момент нельзя проходить практику за границей.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_practice_out_of_country_4():
    question = "Можно ли проходить практику не в россии"

    true_response = 'На данный момент нельзя проходить практику за границей.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_practice_out_of_country_5():
    question = "В компаниях каких стран можно проходить практику"

    true_response = 'На данный момент нельзя проходить практику за границей.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Уровень квалификации преподаветелей

def test_predict_teachers_level_1():
    question = "Какой уровень образования преподавателей"

    true_response = '30% преподавателей техникума высшую категорию, 40% преподаватели 1 категории, 80 % преподавателей имеют высшее образование.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_teachers_level_2():
    question = "Образовательный уровень педагогических работников"

    true_response = '30% преподавателей техникума высшую категорию, 40% преподаватели 1 категории, 80 % преподавателей имеют высшее образование.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_teachers_level_3():
    question = "Образовательный уровень педагогических работников"

    true_response = '30% преподавателей техникума высшую категорию, 40% преподаватели 1 категории, 80 % преподавателей имеют высшее образование.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_teachers_level_4():
    question = "Какое образование у преподавательского состава"

    true_response = '30% преподавателей техникума высшую категорию, 40% преподаватели 1 категории, 80 % преподавателей имеют высшее образование.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_teachers_level_5():
    question = "На сколько умные преподаватели"

    true_response = '30% преподавателей техникума высшую категорию, 40% преподаватели 1 категории, 80 % преподавателей имеют высшее образование.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Могут ли получить общежитие студенты

def test_predict_get_dorm_1():
    question = "Могу ли я получить общежитие"

    true_response = 'Общежитие студентам техникума не предоставляется'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_get_dorm_2():
    question = "Какие условия предоставления общежития"

    true_response = 'Общежитие студентам техникума не предоставляется'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_get_dorm_3():
    question = "Как получить общежитие"

    true_response = 'Общежитие студентам техникума не предоставляется'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_get_dorm_4():
    question = "Есть ли у техникума общежитие"

    true_response = 'Общежитие студентам техникума не предоставляется'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_get_dorm_5():
    question = "Кому предоставляется общежитие"

    true_response = 'Общежитие студентам техникума не предоставляется'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Как проходят собеседования

def test_predict_interviews_1():
    question = "Проходят ли собеседования с будущими работодателями"

    true_response = 'Собеседование с работодателями проводятся перед началом производственной практики.'

    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_interviews_2():
    question = "Организуются ли встречи с потенциальными работодателями"
    true_response = 'Собеседование с работодателями проводятся перед началом производственной практики.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_interviews_3():
    question = "Существует ли практика трудоустройства через личные встречи"
    true_response = 'Собеседование с работодателями проводятся перед началом производственной практики.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_interviews_4():
    question = "Как происходит знакомство студентов с будущими работодателями"
    true_response = 'Собеседование с работодателями проводятся перед началом производственной практики.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_interviews_5():
    question = "Проводятся встречи с компаниями-работодателями"
    true_response = 'Собеседование с работодателями проводятся перед началом производственной практики.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Как перевестись с другой специальности

def test_predict_change_course_1():
    question = "Как перевестись на другую специальность"
    true_response = 'На другую специальность перевестить можно при небольшой разности в учебных планах. Разницу в учебных планах неоюходимо будет ликвидировать в соответствии с графиком, который составляет приемная комиссия.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_change_course_2():
    question = "Возможно ли изменение направления обучения"
    true_response = 'На другую специальность перевестить можно при небольшой разности в учебных планах. Разницу в учебных планах неоюходимо будет ликвидировать в соответствии с графиком, который составляет приемная комиссия.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_change_course_3():
    question = "Процедура смены образовательной программы"
    true_response = 'На другую специальность перевестить можно при небольшой разности в учебных планах. Разницу в учебных планах неоюходимо будет ликвидировать в соответствии с графиком, который составляет приемная комиссия.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_change_course_4():
    question = "Каков порядок перехода между специальностями"
    true_response = 'На другую специальность перевестить можно при небольшой разности в учебных планах. Разницу в учебных планах неоюходимо будет ликвидировать в соответствии с графиком, который составляет приемная комиссия.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_change_course_5():
    question = "Условия перевода на альтернативную специальность"
    true_response = 'На другую специальность перевестить можно при небольшой разности в учебных планах. Разницу в учебных планах неоюходимо будет ликвидировать в соответствии с графиком, который составляет приемная комиссия.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Выдача техники

def test_predict_need_have_yourself_techic_1():
    question = "Нужна ли своя техника для обучения"
    true_response = 'Техникум оснащен вычислительной техникой, на которое утсановлено неоходимое для занятий программное обеспечение.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_need_have_yourself_techic_2():
    question = "Обязательно ли иметь личный компьютер для учебы"
    true_response = 'Техникум оснащен вычислительной техникой, на которое утсановлено неоходимое для занятий программное обеспечение.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_need_have_yourself_techic_3():
    question = "Какие требования к технике для студентов"
    true_response = 'Техникум оснащен вычислительной техникой, на которое утсановлено неоходимое для занятий программное обеспечение.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_need_have_yourself_techic_4():
    question = "Предоставляется ли техника для обучения"
    true_response = 'Техникум оснащен вычислительной техникой, на которое утсановлено неоходимое для занятий программное обеспечение.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_need_have_yourself_techic_5():
    question = "Как организовано техническое обеспечение учебного процесса"
    true_response = 'Техникум оснащен вычислительной техникой, на которое утсановлено неоходимое для занятий программное обеспечение.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Дистанционное обучение

def test_predict_distant_education_1():
    question = "Есть ли возможность обучения дистанционно"
    true_response = 'Обучение в техникуме только очное'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_distant_education_2():
    question = "Предусмотрено ли онлайн-обучение"
    true_response = 'Обучение в техникуме только очное'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_distant_education_3():
    question = "Возможен ли удаленный формат образования"
    true_response = 'Обучение в техникуме только очное'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_distant_education_4():
    question = "Как организовано обучение в формате онлайн"
    true_response = 'Обучение в техникуме только очное'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_distant_education_5():
    question = "Практикуется ли электронное обучение"
    true_response = 'Обучение в техникуме только очное'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#День открытых дверей

def test_predict_open_door_day_1():
    question = "Когда день открытых дверей в колледже"
    true_response = 'День открытых дверей проводится перед приёмом документов абитуриентов. Следите за новостями в соц сетях мпт (перечислить соц сети) или или на сайте'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_open_door_day_2():
    question = "В какие сроки проводится день открытых дверей"
    true_response = 'День открытых дверей проводится перед приёмом документов абитуриентов. Следите за новостями в соц сетях мпт (перечислить соц сети) или или на сайте'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_open_door_day_3():
    question = "Как узнать дату мероприятия для абитуриентов"
    true_response = 'День открытых дверей проводится перед приёмом документов абитуриентов. Следите за новостями в соц сетях мпт (перечислить соц сети) или или на сайте'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_open_door_day_4():
    question = "Периодичность проведения дня открытых дверей"
    true_response = 'День открытых дверей проводится перед приёмом документов абитуриентов. Следите за новостями в соц сетях мпт (перечислить соц сети) или или на сайте'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_open_door_day_5():
    question = "Информация о презентационном дне для поступающих"
    true_response = 'День открытых дверей проводится перед приёмом документов абитуриентов. Следите за новостями в соц сетях мпт (перечислить соц сети) или или на сайте'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Аттестация студентов

def test_predict_student_scorring_1():
    question = "Как происходит аттестация студентов"
    true_response = 'Промежуточная аттестация студентов осуществляется через процесс оценки их знаний по окончании семестра. В течение учебного года проводятся две зачетно-экзаменационные сессии: зимняя и летняя, которые организуются в соответствии с учебным планом и утвержденным расписанием. Оценки выставляются в ведомости и зачетные книжки студентов.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


def test_predict_student_scorring_2():
    question = "Каков процесс оценивания знаний студентов"
    true_response = 'Промежуточная аттестация студентов осуществляется через процесс оценки их знаний по окончании семестра. В течение учебного года проводятся две зачетно-экзаменационные сессии: зимняя и летняя, которые организуются в соответствии с учебным планом и утвержденным расписанием. Оценки выставляются в ведомости и зачетные книжки студентов.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_student_scorring_3():
    question = "Механизм контроля успеваемости в учебном заведении"
    true_response = 'Промежуточная аттестация студентов осуществляется через процесс оценки их знаний по окончании семестра. В течение учебного года проводятся две зачетно-экзаменационные сессии: зимняя и летняя, которые организуются в соответствии с учебным планом и утвержденным расписанием. Оценки выставляются в ведомости и зачетные книжки студентов.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_student_scorring_4():
    question = "Есть ли промежуточная аттестация в техникуме"
    true_response = 'Промежуточная аттестация студентов осуществляется через процесс оценки их знаний по окончании семестра. В течение учебного года проводятся две зачетно-экзаменационные сессии: зимняя и летняя, которые организуются в соответствии с учебным планом и утвержденным расписанием. Оценки выставляются в ведомости и зачетные книжки студентов.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_student_scorring_5():
    question = "Методика оценивания результатов обучения"
    true_response = 'Промежуточная аттестация студентов осуществляется через процесс оценки их знаний по окончании семестра. В течение учебного года проводятся две зачетно-экзаменационные сессии: зимняя и летняя, которые организуются в соответствии с учебным планом и утвержденным расписанием. Оценки выставляются в ведомости и зачетные книжки студентов.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Трудоустройство после обучения

def test_predict_working_after_studying_1():
    question = "Есть ли трудоустроство после обучения"
    true_response = 'Перспективы трудоустройства после окончания техникума зависят от выбранной специальности и вашего поведения во время учебы и практик. На нашем сайте представлена информация о организациях, с которыми мы сотрудничаем, и которые принимают наших выпускников. Техникум демонстрирует высокий уровень трудоустройства — в среднем 93% за последние пять лет, что подтверждает качество подготовки студентов и их востребованность на рынке труда.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_working_after_studying_2():
    question = "Гарантировано ли трудоустройство после окончания учебы"
    true_response = 'Перспективы трудоустройства после окончания техникума зависят от выбранной специальности и вашего поведения во время учебы и практик. На нашем сайте представлена информация о организациях, с которыми мы сотрудничаем, и которые принимают наших выпускников. Техникум демонстрирует высокий уровень трудоустройства — в среднем 93% за последние пять лет, что подтверждает качество подготовки студентов и их востребованность на рынке труда.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_working_after_studying_3():
    question = "Каковы шансы на работу после получения диплома"
    true_response = 'Перспективы трудоустройства после окончания техникума зависят от выбранной специальности и вашего поведения во время учебы и практик. На нашем сайте представлена информация о организациях, с которыми мы сотрудничаем, и которые принимают наших выпускников. Техникум демонстрирует высокий уровень трудоустройства — в среднем 93% за последние пять лет, что подтверждает качество подготовки студентов и их востребованность на рынке труда.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_working_after_studying_4():
    question = "Помогает ли техникум в поиске работы выпускникам"
    true_response = 'Перспективы трудоустройства после окончания техникума зависят от выбранной специальности и вашего поведения во время учебы и практик. На нашем сайте представлена информация о организациях, с которыми мы сотрудничаем, и которые принимают наших выпускников. Техникум демонстрирует высокий уровень трудоустройства — в среднем 93% за последние пять лет, что подтверждает качество подготовки студентов и их востребованность на рынке труда.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_working_after_studying_5():
    question = "Возможности трудоустройства после завершения обучения"
    true_response = 'Перспективы трудоустройства после окончания техникума зависят от выбранной специальности и вашего поведения во время учебы и практик. На нашем сайте представлена информация о организациях, с которыми мы сотрудничаем, и которые принимают наших выпускников. Техникум демонстрирует высокий уровень трудоустройства — в среднем 93% за последние пять лет, что подтверждает качество подготовки студентов и их востребованность на рынке труда.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Новости техникума

def test_predict_college_news_1():
    question = "Где я могу узнать новости техникума"
    true_response = 'С новостями техникума вы можете ознакомиться на главной странице нашего сайта.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_college_news_2():
    question = "Информационные ресурсы для отслеживания новостей техникума"
    true_response = 'С новостями техникума вы можете ознакомиться на главной странице нашего сайта.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_college_news_3():
    question = "Как быть в курсе последних событий учебного заведения"
    true_response = 'С новостями техникума вы можете ознакомиться на главной странице нашего сайта.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_college_news_4():
    question = "Канал получения актуальной информации о техникуме"
    true_response = 'С новостями техникума вы можете ознакомиться на главной странице нашего сайта.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_college_news_5():
    question = "Где публикуются официальные сообщения учебного заведения"
    true_response = 'С новостями техникума вы можете ознакомиться на главной странице нашего сайта.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

#Средний балл для поступления

def test_predict_middle_score_1():
    question = "Какой средний балл для поступления в техникум"
    true_response = 'Средний балл для поступления зависит от успеваемости абитуриентов и варьируется каждый год в зависимости от конкуренции и результатов студентов. Для получения более подробной информации о текущих требованиях и средних баллах, необходимых для поступления, вы можете обратиться на сайт приемной комиссии техникума.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_middle_score_2():
    question = "Проходной балл для зачисления в учебное заведение"
    true_response = 'Средний балл для поступления зависит от успеваемости абитуриентов и варьируется каждый год в зависимости от конкуренции и результатов студентов. Для получения более подробной информации о текущих требованиях и средних баллах, необходимых для поступления, вы можете обратиться на сайт приемной комиссии техникума.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_middle_score_3():
    question = "Какие оценки нужны для поступления"
    true_response = 'Средний балл для поступления зависит от успеваемости абитуриентов и варьируется каждый год в зависимости от конкуренции и результатов студентов. Для получения более подробной информации о текущих требованиях и средних баллах, необходимых для поступления, вы можете обратиться на сайт приемной комиссии техникума.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_middle_score_4():
    question = "Критерии оценивания абитуриентов при зачислении"
    true_response = 'Средний балл для поступления зависит от успеваемости абитуриентов и варьируется каждый год в зависимости от конкуренции и результатов студентов. Для получения более подробной информации о текущих требованиях и средних баллах, необходимых для поступления, вы можете обратиться на сайт приемной комиссии техникума.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response

def test_predict_middle_score_5():
    question = "Требования к аттестату для поступления"
    true_response = 'Средний балл для поступления зависит от успеваемости абитуриентов и варьируется каждый год в зависимости от конкуренции и результатов студентов. Для получения более подробной информации о текущих требованиях и средних баллах, необходимых для поступления, вы можете обратиться на сайт приемной комиссии техникума.'
    response = convert_tag_to_answer(question.strip(), model)

    with open('results/results_for_questions_all.txt', "w", encoding="utf-8") as f:
        for_write = ''
        if response == true_response:
            for_write = question + "_" + "true\n" + str(datetime.datetime.now().date()) + "\n"

        else:
            for_write = question + "_" + "false" + str(datetime.datetime.now().date()) + "\n"

        f.write(for_write)

    assert response == true_response


#Подсчёт результатов!!!

def count_results_from_file():
    pass