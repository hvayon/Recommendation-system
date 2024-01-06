WANT = r'(?P<want>(хочу|хочется))'

GENERAL_QUESTION = r'(?P<general_question>(что|какой))'
EXIST = r'(?P<exist>(есть|предложить))'

NOT_KNOW_GENERAL = r'(?P<not_know_general>(не.*знать).*(хотеть|надо))'

HELP = r'(?P<help>(посоветовать|помочь|предложить|подсказать|показать|порекомендовать|посмотреть|ознакомиться))'
LIKE = r'(?P<like>(нравиться|любить))'
DISLIKE = r'(?P<dislike>(не переносить|не нравиться|не подходить|не любить|терпеть не мочь|ненавидеть))'

SIMILAR_TO = r'(?P<similar_to>(похожий на|на подобие|аналог|тип))'
NOT_SIMILAT_TO = r'(?P<not_similar_to>(не похожий|отличный от))'
NAME = r'(?P<similar_name>(shalimar|3 l\'голодные игры|сумерки|убить пересмешника|великий гэтсби|виноваты звезды|ангелы и демоны|гордость и предубеждение|бегущий за ветром|дивергент|братство кольца|баллада о змеях и певчих птицах|гарри поттер и орден феникса|гарри поттер и кубок огня|гарри поттер и дары смерти|гарри поттер и принц-полукровка|повелитель мух|исчезнувшая|прислуга|мемуары гейши|алхимик|дающий|лев, колдунья и платяной шкаф|жена путешественника во времени|игра престолов|перси джексон и похититель молний|маленькие женщины|джейн эйр|дневник памяти|жизнь пи|вода для слонов|книжный вор|451 градус по фаренгейту|новолуние))'
DISLIKE_EXT = r'({}|{})'.format(DISLIKE, NOT_SIMILAT_TO)

GENRE = r'(?P<genre>(роман|романтическое фэнтези|приключения|фэнтези|научная фантастика|антиутопия|социальная фантастика|детектив|классическая проза|экранизация))'
LIKE_GENRE = r'.*{}.*{}.*'.format(LIKE, GENRE)
HELP_GENRE = r'.*{}.*{}.*'.format(HELP, GENRE)

TAG = r'(?P<tag>(юношеский литература|антиутопия|Боевая фантастика|Зарубежная фантастика|Игры на выживание|Постапокалиптика|Сборник рассказов|Социальная фантастика|Экранизации|Бессмертие|Вампиры|Зарубежное фэнтези|Книги про вампиров|Любовное фэнтези|Любовные испытания|Мистика|Оборотни|Экранизации|Американская классика|Зарубежная классика|Литература 20 века|Расизм|Социальная проза|Становление героя|Экранизации|20-е годы|Американская литература|Высшее общество|Жизненные ценности|Зарубежная классика|Классическая проза|Экранизации|Зарубежные любовные романы|Мировой бестселлер|Романтические истории|Сила любви|Экранизации|Древние реликвии|Загадочные убийства|Зарубежные детективы|Квест|Тайны прошлого|Тайные общества|Триллеры|Английская классика|Вечные сюжеты|Женские истории|Исторические любовные романы|Классические любовные романы|Литература 19 века|Ближний Восток|Жизненные трудности|Мужская дружба|Повороты судьбы|Современная зарубежная литература|Экранизированный бестселлер|Антиутопия|Жестокие игры|Зарубежная фантастика|Психологическая фантастика|Социальная фантастика|Становление героя|Эксперименты над людьми|Героическое фэнтези|Зарубежное фэнтези|Квест|Классика фэнтези|Книги про волшебников|Красочные иллюстрации|Спасение мира|Эпическое фэнтези|Антиутопия|Боевая фантастика|Игры на выживание|Любовно-фантастические романы|Постапокалиптика|Приквел|Социальная фантастика|Юношеская литература|Приключения|Фэнтези|Взросление|Жестокость|Зарубежная классика|Литература 20 века|Робинзонада|Социальная проза|Философская проза|Бестселлеры|Загадочное исчезновение|Зарубежные детективы|Психологические триллеры|Современные детективы|Тайны прошлого|Триллеры|Экранизации|Американская литература|Женские судьбы|Расизм|Современная зарубежная литература|Социальная проза|Экранизации|Женские судьбы|Жизненные трудности|Исторические любовные романы|Любовные интриги|Экранизации|Япония|Мировой бестселлер|Поиски смысла жизни|Современная зарубежная литература|Судьба человека|Тайны мироздания|Философская проза|Антиутопия|Близкое будущее|Детская фантастика|Книги для подростков|Социальная фантастика|Становление героя|Философская фантастика|Экранизации|Волшебные существа|Детское фэнтези|Зарубежное фэнтези|Книги про волшебников|Магические миры|Пророчества и предсказания|Экранизации|Американская литература|Зарубежная фантастика|История любви|Любовно-фантастические романы|Путешествия во времени|Становление героя|Экранизации|Боевое фэнтези|Героическое фэнтези|Драконы|Зарубежное фэнтези|Придворные интриги|Сражения|Экранизации|Эпическое фэнтези|Героическое фэнтези|Детское фэнтези|Древние боги|Зарубежное фэнтези|Книги про волшебников|Мифологические сюжеты|Становление героя|Экранизации|Детская проза|Зарубежная классика|Зарубежные детские книги|Литература 19 века|Первая любовь|Романтические отношения|Романы для девочек|Становление героя|Экранизации))'
LIKE_TAG = r'.*{}.*{}.*'.format(LIKE, TAG)
HELP_TAG = r'.*{}.*{}.*'.format(HELP, TAG)

INFO = r'Я ничего не знаю о книгах\. Расскажи, какие жанры бывают.'

DURABILITY = r'(?P<durability>(очень маленький|маленький|средний|большой|очень большой))'
SHOW_DURABILITY = r'.*{}.* книг.*'.format(DURABILITY)

GENERAL_EXT = r'({}|{})'.format(GENERAL_QUESTION, WANT)

WHAT_EXISTS = r'.*{}.*{}.*'.format(GENERAL_QUESTION, EXIST)


I_LIKE_BOOK = r'.*{}.*{}.*'.format(LIKE, NAME)
I_DISLIKE_BOOK = r'.*{}.*{}.*'.format(DISLIKE, NAME)

SIMILAR_TO_BOOK = r'.*{}.*{}.*'.format(SIMILAR_TO, NAME)
NOT_SIMILAR_TO_BOOK = r'.*{}.*{}.*'.format(DISLIKE_EXT, NAME)

RULE_ARR = [NOT_SIMILAR_TO_BOOK,
            SIMILAR_TO_BOOK,
            SHOW_DURABILITY,
            I_DISLIKE_BOOK,
            I_LIKE_BOOK,
            WHAT_EXISTS,
			LIKE_GENRE,
			HELP_GENRE,
			LIKE_TAG,
			HELP_TAG,
			INFO,
			]