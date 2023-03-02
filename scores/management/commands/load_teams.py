from django.core.management.base import BaseCommand
from scores.models import Team, Tournament, Fixture

TEAMS = [
    'Арсенал', 'Астон Вилла', 'Борнмут', 'Брайтон', 'Брентфорд', 'Вест Хэм Юнайтед', 'Вулверхэмптон',
    'Кристал Пэлас', 'Лестер Сити', 'Ливерпуль', 'Лидс Юнайтед', 'Манчестер Сити', 'Манчестер Юнайтед',
    'Ноттингем Форест', 'Ньюкасл Юнайтед', 'Саутгемптон', 'Тоттенхэм', 'Фулхэм', 'Челси', 'Эвертон'
]

class Command(BaseCommand):
    help = 'Load EPL teams and fixtures'

    def handle(self, *args, **kwargs):
        tournament = Tournament.objects.get_or_create(name="Английская премьер лига 2022/23")[0]

        if Team.objects.count() == 0:
            team_objs = [Team(name=team_name) for team_name in TEAMS]
            teams = Team.objects.bulk_create(team_objs)
        else:
            teams = Team.objects.all()


        fixtures = []
        for i in range(0, len(teams), 2):
            fixtures.append(
                Fixture(home_team=teams[i], away_team=teams[i+1], tournament=tournament)
            )

        if Fixture.objects.count() == 0:
            fixtures = Fixture.objects.bulk_create(fixtures)