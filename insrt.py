from PyQt5.QtCore import QTime
txt_title = 'Health Test'
win_width, win_height = 1000, 600
win_x, win_y = 200, 100

hi_text = 'Добро пожаловать'
rule_text = ('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
nxt_button =  'Далее'
txt_age = 'Полных лет'
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.'
txt_test2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.'
txt_test3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.'

time = QTime(0,0,0)
txt_timer = time.toString('hh:mm:ss')

txt_name = 'Введите Ф.И.О.:'
txt_hintname = "Ф.И.О."
txt_hintage =  "0"
txt_hinttest1 = '0'
txt_hinttest2 =  '0'
txt_hinttest3 = '0'
txt_sendresults= '  Отправить результаты  '
txt_starttest1='  Начать первый тест  '
txt_starttest2='  Начать второй тест  '
txt_starttest3='  Начать третий тест  '
txt_finalwin = 'Health Test'
txt_workheart = 'Работа сердца: '
txt_index = 'Индекс Руфье:  '
exs_buttton = 'Закрыть'




