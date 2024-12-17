from django.core.management.base import BaseCommand
from ativos.models import Ativo
from ativos.utils import obter_cotacao

class Command(BaseCommand):
    help = "Busca as cotações dos ativos cadastrados"

    def handle(self, *args, **kwargs):
        ativos = Ativo.objects.all()
        for ativo in ativos:
            cotacao = obter_cotacao(ativo.codigo)
            if cotacao is not None:
                ativo.ultima_cotacao = cotacao
                ativo.save()
                self.stdout.write(f"Cotação de {ativo.codigo} atualizada para {cotacao}")