import time

class User:

    def __init__(self, nickname, password, age):

        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title,  duration, time_now=0, adult_mode=False):

        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self, users=[], videos=[], current_user=None):

        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):

        for user in self.users:

            if user.nickname == nickname and user.password == hash(password):

                self.current_user = user

    def register(self, nickname, password, age):

        for user in self.users:

            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        user_1 = User(nickname, password, age)
        self.users.append(user_1)
        print(f'Пользователь {user_1.nickname} успешно создан.')

        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def  add(self, *args):

        for video in args:

            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):                            #Как Сделать нижний регистор?

        searched_video = []

        for i in self.videos:
            if search.lower() in i.title.lower():
                searched_video.append(i.title)

        return searched_video

    def watch_video(self, film):

        if self.current_user is None:
            print(f'Войдите в аккаунт')
            return

        for video in self.videos:

            if video.title == film:

                if video.adult_mode == True and self.current_user.age < 18:
                    print(f'Видео недоступно')
                else:
                    for i in range(video.time_now, video.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео.')
            else:
                print(f'Видео не найдено.')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')


