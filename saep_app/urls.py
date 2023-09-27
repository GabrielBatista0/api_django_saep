from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('professor',views.ProfessorViewSet),
router.register('turma',views.TurmaViewSet),
router.register('turmaAtividade',views.Turma_atividadeViewSet),
router.register('atividade',views.AtividadeViewSet),
router.register('professorTurma',views.Professor_turmaViewSet),
router.register('login',views.LoginProfessorViewSet),

urlpatterns =[] +router.urls