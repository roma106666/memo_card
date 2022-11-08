from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint



def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbnt_1.setChecked(False)
    rbnt_2.setChecked(False)
    rbnt_3.setChecked(False)
    rbnt_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_correct(res):
    label_1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3] or isChecked():
            show_correct('Неправильно!')
    r = window.score / window.total * 100
    print('Статистика')
    print('-Всего вопросов: ',window.total)
    print('-Правильных ответов: ',window.score)
    print('Рейтинг: ', r, '%')
        
def next_question():
    window.total += 1
    window.cur_question = randint(0, len(question_list)-1)
    q = question_list[window.cur_question]
    ask(q)
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
        
question_list = []
question_list.append(Question('Что?','ничего','б','никогда','нет'))
question_list.append(Question('Где?','нет','8','нигде','чего'))
question_list.append(Question('Когда?','вчера','завтра','никогда','3453352452'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(450,250)

quastion1 = QLabel('Вопрос')
button = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbnt_1 = QRadioButton('Вариант 1')
rbnt_2 = QRadioButton('Вариант 2')
rbnt_3 = QRadioButton('Вариант 3')
rbnt_4 = QRadioButton('Вариант 4')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbnt_1)
layout_ans2.addWidget(rbnt_2)
layout_ans3.addWidget(rbnt_3)
layout_ans3.addWidget(rbnt_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_card = QVBoxLayout()

layout_line1.addWidget(quastion1,alignment = Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)

layout_line3.addWidget(button,alignment = Qt.AlignCenter)

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

AnsGroupBox = QGroupBox('Результат теста')
AnsGroupBox.hide()
label_1 = QLabel('Правильно/Неправильно')
label_2 = QLabel('Правильный ответ')
layout_ans4 = QVBoxLayout()

layout_ans4.addWidget(label_1,alignment = Qt.AlignLeft)
layout_ans4.addWidget(label_2,alignment = Qt.AlignCenter)

AnsGroupBox.setLayout(layout_ans4)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbnt_1)
RadioGroup.addButton(rbnt_2)
RadioGroup.addButton(rbnt_3)
RadioGroup.addButton(rbnt_4)

layout_line2.addWidget(AnsGroupBox)

button.clicked.connect(click_OK)

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quastion1.setText(q.question)
    label_2.setText(q.right_answer)
    show_question()

answers = [rbnt_1,rbnt_2,rbnt_3,rbnt_4]

window.setLayout(layout_card)

window.cur_question = 1
window.total = 0
window.score = 0

next_question()
window.show()
app.exec()