from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import json


# Initialize Selenium WebDriver
driver = webdriver.Chrome()


def generate_question_id():
    """Generates a random id, useful for our questions"""
    return random.randint(1000000000, 1000000000000)


def add_labels(answers, right_answer):
    """
    Adds labels to the answers based on their index in list
    :param answers: is list of all possible answers
    :param right_answer: right answer is selenium object that contains the right answer
    :return: is dictionary where the keys are the answers and the values are booleans
    which indicates is the answer right or not
    """
    result = {}
    for index, answer in enumerate(answers):
        if answer == right_answer.text:
            result[f'{index + 1}) {answer}'] = True
        else:
            result[f'{index + 1}) {answer}'] = False

    return result


class AnswerForQuestion:
    def __init__(self, index=0):
        """
        This class is created for each question, so if there are 20 questions in test,
        the 20 classes we need to create, to answer right to the whole test
        This class includes all necessary features to answer question and return the data for
        further storage
        :param index: is the number of question
        """
        self.index = index
        self.question_block = driver.find_element(By.ID, f'question_{self.index}')
        self.right_answer = self.question_block.find_element(By.XPATH,
                                                             ".//div[starts-with(@class, 'card') and contains(@class, 'True')]")

    def get_data(self):
        """
        This method is responsible for getting all possible data from question
        :return: a dictionary that contains a data of question such as:
        image, answers, right answer and question itself
        """
        question_block_splited = self.question_block.text.splitlines()
        answers = add_labels(question_block_splited[1:], self.right_answer)
        image = self.question_block.find_element(By.TAG_NAME, 'img')

        json_data = {
            'question': question_block_splited[0],
            'image': image.get_attribute('src'),
            'answers': '\n'.join(list(answers.keys())),
            'right_answer': ''.join([k for k, v in answers.items() if v])
        }
        return json_data

    def execute(self):
        """
        We need to run this method to answer the question of class, by its
        provided index in __init__
        :return:
        """
        self.right_answer.click()


def reset_json(data):
    """
    This function is mainly not used, it uses when json file is empty
    !!! If the json file is empty make sure instead add_json() in the
    end of parser function you user reset_json() !!!
    :param data: the data that we want to right to json
    :return:
    """
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_to_json(data):
    """
    Adding a new data to our json file
    :param data: the data that we want to add
    :return:
    """
    with open('data.json', 'r', encoding='utf-8') as file:
        existing_data = json.load(file)

    existing_data.update(data)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)


def parser():
    """
    Main parser that parse the website by such 'https://e-avtomaktab.uz/Home/Test' url
    :return:
    """
    url = 'https://e-avtomaktab.uz/Home/Test'
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@onclick, 'changeLang(3)')]").click()
    time.sleep(2)

    questions = [AnswerForQuestion(index=i) for i in range(1, 21)]
    nav_question_index = 2

    main_data = {}

    for question in questions:
        try:
            question.execute()
            question_id = str(generate_question_id())
            main_data[question_id] = question.get_data()
            a_next = driver.find_element(By.ID, f'TsubQuestionNumber_{nav_question_index}')
            nav_question_index += 1

            a_next.click()
        except:
            pass

    add_to_json(main_data)

    time.sleep(3)


def main():
    """
    Main function
    :return:
    """
    parse_times = int(input('Enter how many tests you want to parse: '))

    for i in range(parse_times):
        parser()

    print('End of program')


if __name__ == '__main__':
    main()
