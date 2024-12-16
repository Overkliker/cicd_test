import pytest

class TestClass1:
    @pytest.mark.ss
    def test_predict_model_1(self,):
        question = "какую специальность я получу отучившись на компьютерные системы и комплексы"

        true_response = "Выпускникам  специальности 09.02.01 Компьютерные ситемы и комплексы присваивается квалификация Техник по компьютерным системам"

        assert true_response == true_response

    @pytest.mark.sanity
    def test_predict_model_2(self,):
        question = "как оплатить обучение"

        true_response = "Оплата обучения осуществляется по семестрам"

        assert question == true_response

class TestClass2:
    @pytest.mark.gg
    def test_predict_model_3(self,):
        question = "когда начинается приём документов"

        true_response = "Прием докуменнтов для поступления проходит с 20 июня по 15 августа"

        assert question == true_response


