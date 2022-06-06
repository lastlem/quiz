from tkinter import *
from tkinter.ttk import *

answers = []
dict_data = {'points': 0, 'question_number': 0}
all_questions = [
    ("?Which widgets using to display text with the ability to edit it?",
     "+Canvas", "-Listbox", "+Entry", "+Text", "-Label"),
    ('?What widgets using for positioning other widgets?',
     '-Button', '-Radiobutton', '+Frame', '-Text', '+LabelFrame'),
    ('?How are you?',
     '-Bad', '-Good', '+Normal', '-Very Good', '+Very Normal')
]


def reset_variables():
    dict_data['points'], dict_data['question_number'] = 0, 0
    answers.clear()


def clear_widgets_in_frame(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_result(frame):
    Label(frame, text=f'Your result: {dict_data["points"]} points.').pack()
    Button(frame, text='Try again', command=lambda: ask_question(frame)).pack()
    reset_variables()


def check():
    question_number = dict_data['question_number']
    for true_answer, chosen_answer in zip(all_questions[question_number][1:], answers[question_number]):
        true_answer = true_answer[0] == '+'
        if true_answer and true_answer == chosen_answer.get():
            dict_data['points'] += 1
        elif true_answer != chosen_answer.get():
            dict_data['points'] -= 1


def next_action(frame: Frame):
    check()
    if dict_data['question_number'] < len(all_questions) - 1:
        dict_data['question_number'] += 1
        ask_question(frame)
    else:
        clear_widgets_in_frame(frame)
        show_result(frame)


def ask_question(frame):
    clear_widgets_in_frame(frame)

    question_answers = []
    question_number = dict_data['question_number']
    for index, text in enumerate(all_questions[question_number]):
        if text.startswith('?'):
            Label(frame, text=text[1:]).pack()
        else:
            answer = BooleanVar()
            Checkbutton(frame, text=text[1:], variable=answer, onvalue=1, offvalue=0).pack(anchor=W)
            question_answers.append(answer)

    answers.append(question_answers)
    Button(frame, text="Next >>", command=lambda: next_action(frame)).pack()


def first_screen(frame):
    Label(frame, text='Welcome to my quiz!\nPress "Start" to continue...').pack()
    Button(frame, text="Start", command=lambda: ask_question(frame)).pack()


def main():
    root = Tk()
    root.title('My quiz')

    main_frame = LabelFrame(root, text="Generate screen")
    main_frame.pack()

    first_screen(main_frame)

    root.mainloop()


if __name__ == '__main__':
    main()
