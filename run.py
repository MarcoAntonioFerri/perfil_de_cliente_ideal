from perfil_de_cliente_ideal.cmd import build_parser

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":

    #Exemplo de código caso alguém queira rodar, porém não saiba usar o "make".
    #raise SystemExit(main(["cmd_predict", "-pti", "data/processed/clean_dataset.csv", "-o", "reports/predicao01.csv"]))
    #raise SystemExit(main(["cmd_predict", "-pti", "data/processed/clean_dataset.csv"]))
    #raise SystemExit(main(["cmd_train"]))

    raise SystemExit(main())