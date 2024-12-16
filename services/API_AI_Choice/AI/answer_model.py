import pandas as pd
import numpy as np
import torch
import re
import os
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple, Optional
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class QASystem:
    def __init__(self,
                 model_name: str = 'DeepPavlov/rubert-base-cased',
                 threshold: float = 0.5,
                 max_length: int = 128):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        logger.info(f"Используется устройство: {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()

        self.question_embeddings: Dict = {}
        self.answers: Dict = {}
        self.threshold = threshold
        self.max_length = max_length
        self.model_path = 'qa_model.pth'

        if os.path.exists(self.model_path):
            self.load_model()
        else:
            self.train_model()

    def preprocess_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = str(text).lower().strip()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[,.?\-!":()\s]', '', text)
        return text

    def encode_text(self, text: str) -> np.ndarray:
        text = self.preprocess_text(text)
        if not text:
            return np.zeros((1, self.model.config.hidden_size))

        tokens = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors='pt'
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**tokens)
            embeddings = outputs.last_hidden_state.mean(dim=1)

        return embeddings.cpu().numpy()

    def train_model(self, excel_path: str = 'FormattedQuestions.xlsx'):
        logger.info("Начало обучения модели...")

        try:
            # Читаем Excel файл
            df = pd.read_excel(excel_path, header=None)
            df.columns = ['Col1', 'Col2']  # Присваиваем имена столбцам

            current_id = None
            current_answer = None
            questions_batch = []

            # Проходим по всем строкам
            for idx, row in df.iterrows():
                col1 = str(row['Col1']).strip() if pd.notna(row['Col1']) else ""
                col2 = str(row['Col2']).strip() if pd.notna(row['Col2']) else ""

                # Если первая колонка содержит число (ID вопроса)
                if col1 and col1.replace('.', '').isdigit():
                    current_id = float(col1)
                    if col2:  # Если есть ответ
                        current_answer = col2
                        self.answers[current_id] = current_answer
                        logger.debug(f"Найден ответ для ID {current_id}: {current_answer[:50]}...")

                # Если это строка с вопросом (не ID и не пустая)
                elif col1 and not col1.replace('.', '').isdigit() and current_id is not None:
                    questions_batch.append({
                        'question': col1,
                        'answer_id': current_id
                    })
                    logger.debug(f"Добавлен вопрос: {col1[:50]}... для ID {current_id}")

            # Обрабатываем собранные вопросы
            questions_processed = 0
            for q_data in questions_batch:
                try:
                    embedding = self.encode_text(q_data['question'])
                    key = f"{q_data['answer_id']}_{questions_processed}"
                    self.question_embeddings[key] = {
                        'embedding': embedding,
                        'question': q_data['question'],
                        'answer_id': q_data['answer_id']
                    }
                    questions_processed += 1
                except Exception as e:
                    logger.error(f"Ошибка при обработке вопроса: {q_data['question'][:50]}... Ошибка: {str(e)}")

            logger.info(f"Обучение завершено. Обработано {questions_processed} вопросов и {len(self.answers)} ответов")
            self.save_model()

        except Exception as e:
            logger.error(f"Ошибка при обучении модели: {str(e)}")
            raise

    def get_answer(self, query: str) -> str:
        try:
            if not self.question_embeddings:
                return "База знаний пуста"

            query_embedding = self.encode_text(query)
            similarities = []

            for qid, data in self.question_embeddings.items():
                similarity = cosine_similarity(
                    query_embedding,
                    data['embedding']
                )[0][0]

                similarities.append({
                    'similarity': similarity,
                    'answer_id': data['answer_id'],
                    'question': data['question']
                })

            # Сортировка по убыванию схожести
            similarities.sort(key=lambda x: x['similarity'], reverse=True)
            best_match = similarities[0]

            if best_match['similarity'] > self.threshold:
                answer = self.answers.get(best_match['answer_id'])
                return (f"Ответ (уверенность: {best_match['similarity']:.2f}):\n{answer}\n\n"
                        f"Похожий вопрос: {best_match['question']}")
            else:
                return "Извините, не могу найти подходящий ответ на ваш вопрос"

        except Exception as e:
            logger.error(f"Ошибка при поиске ответа: {str(e)}")
            return f"Произошла ошибка при обработке вопроса: {str(e)}"

    def save_model(self):
        try:
            data = {
                'embeddings': self.question_embeddings,
                'answers': self.answers,
                'threshold': self.threshold
            }
            torch.save(data, self.model_path)
            logger.info(f"Модель сохранена в {self.model_path}")
        except Exception as e:
            logger.error(f"Ошибка при сохранении модели: {str(e)}")

    def load_model(self):
        try:
            data = torch.load(self.model_path)
            self.question_embeddings = data['embeddings']
            self.answers = data['answers']
            self.threshold = data['threshold']
            logger.info(f"Модель загружена из {self.model_path}")
        except Exception as e:
            logger.error(f"Ошибка при загрузке модели: {str(e)}")
            logger.info("Начинаю новое обучение...")
            self.train_model()


def print_debug_info(qa_system):
    """Вывод отладочной информации"""
    print("\nОтладочная информация:")
    print(f"Количество ответов: {len(qa_system.answers)}")
    print(f"Количество вопросов: {len(qa_system.question_embeddings)}")
    print("\nПримеры ответов:")
    for id, answer in list(qa_system.answers.items())[:3]:
        print(f"ID {id}: {answer[:100]}...")
    print("\nПримеры вопросов:")
    for key, data in list(qa_system.question_embeddings.items())[:3]:
        print(f"Key {key}: {data['question']}")


def convert_tag_to_answer(tag, model: QASystem):
    return model.get_answer(tag)

def interactive_mode():
    """Интерактивный режим работы с системой"""
    qa = QASystem()

    # Вывод отладочной информации
    print_debug_info(qa)

    logger.info("\nСистема вопросов и ответов готова к работе!")
    print("\nДля выхода введите 'exit' или 'quit'\n")

    while True:
        question = input("\nВведите ваш вопрос: ").strip()

        if question.lower() in ['exit', 'quit']:
            print("Завершение работы...")
            break

        if not question:
            continue

        answer = qa.get_answer(question)
        print("\nОТВЕТ:", answer)


if __name__ == "__main__":
    # Удаление старой модели для переобучения
    if os.path.exists('qa_model.pth'):
        os.remove('qa_model.pth')
    interactive_mode()