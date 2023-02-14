class UserInterface:


    def add_title(args1):
        def args_dec(fn):
            def wrap(*args, **kwargs):
                print(args1.center(50, "="))
                b = fn(*args, **kwargs)
                print("=" * 50)
                return b
            return wrap
        return args_dec

    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        # print("Ввод пользовательских данных".center(50, "="))
        print("Действия со статьями:")
        print("1 - Создание статьи"
              "\n2 - просмотр статей"
              "\n3 - просмотр определённой статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    def add_user_article(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        print("Создание статьи".center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        print("=" * 50)
        return dict_article

    def show_all_articles(self, articles):
        print("Список статей: ".center(50, '='))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        print("=" * 50)
