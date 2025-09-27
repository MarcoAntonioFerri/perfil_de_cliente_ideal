
import argparse

from perfil_de_cliente_ideal.config import REPORTS_DIR
from perfil_de_cliente_ideal.pipeline import cmd_train, cmd_predict


def build_parser():

    # Cria o parser principal para a aplicação CLI
    p = argparse.ArgumentParser(description="Orquestrador: Treino e Predição")
    sub = p.add_subparsers(dest="cmd", required=True)

    # Adiciona subcomandos obrigatórios
    p_train = sub.add_parser("cmd_train")
    p_train.set_defaults(func=cmd_train)

    # Subcomando para predição
    p_pred = sub.add_parser("cmd_predict")
    p_pred.set_defaults(func=cmd_predict)

    # Argumento obrigatório: caminho para o CSV de entrada
    p_pred.add_argument("--path_to_input", "-pti", type=str, required=True,
                        help="CSV com dados novos para predição")

    # Argumento opcional: separador do CSV (default é vírgula)
    p_pred.add_argument("--sep", type=str, default=",",
                        help="Separador do CSV de entrada (default: config.CSV_SEPARATOR)")

    # Argumento opcional: caminho do arquivo de saída (onde salvar as predições)
    p_pred.add_argument("--output", "-o", type=str, default=REPORTS_DIR,
                        help="Arquivo para salvar as predições (csv). Se omitido, imprime no console")

    p_pred.set_defaults(func=cmd_predict)

    return p
