import time
import random
from django.core.management.base import BaseCommand
from scores.models import Team, Fixture

class Command(BaseCommand):
    help = 'Load EPL teams and fixtures'

    def handle(self, *args, **kwargs):
        ITERATIONS = 10

        for i in range(ITERATIONS):
            time.sleep(random.randint(1,6))

            # выбираем, сколько раз мы собираемся обновить результаты
            update_count = random.randint(1,6)

            # проверяем, что матч завершен
            fixtures = Fixture.objects.filter(game_finished=False).order_by("?")

            # при изменении счета, он обновляется
            fixtures = fixtures[:update_count]

            self.update_fixtures(fixtures)

            self.is_game_finished(fixtures)

    def update_fixtures(self, fixtures):
        """ Добавить 0 или 1 гол для каждой команды """
        for fixture in fixtures:
            home_goal = random.randint(0,1)
            away_goal = random.randint(0,1)
            fixture.home_goals += home_goal
            fixture.away_goals += away_goal

        Fixture.objects.bulk_update(fixtures, ['home_goals', 'away_goals'])

    def is_game_finished(self, fixtures):
        """ При вероятности 0.3 - отметим матч как завершенный  """
        for fixture in fixtures:
            # Генерируем случайное число от 0 до 1
            # Если оно получилось меньше 0.3 - матч завершается
            P = random.uniform(0,1)
            if P < 0.3:
                fixture.game_finished = True
                fixture.save()