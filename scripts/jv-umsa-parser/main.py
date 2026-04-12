import argparse
import os
import sys

from lib import Parser


def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="jv-umsa-parser",
        description="Crea archivos base de problemas de jv.umsa.bo.",
    )
    parser.add_argument(
        "-p",
        "--path",
        default=os.getcwd(),
        help="Carpeta de salida para guardar los archivos .py (default: directorio actual).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="Timeout en segundos para peticiones HTTP (default: 20).",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    problem_cmd = subparsers.add_parser("problem", help="Descarga un problema por URL.")
    problem_cmd.add_argument("url", help="URL del problema.")

    contest_cmd = subparsers.add_parser(
        "contest", help="Descarga todos los problemas de un concurso."
    )
    contest_cmd.add_argument("url", help="URL del concurso.")
    contest_cmd.add_argument(
        "--fail-fast",
        action="store_true",
        help="Detiene la ejecucion en el primer error.",
    )

    return parser


def run_problem(parser_obj: Parser, url: str) -> int:
    status, file_path = parser_obj.create_problem(url)
    if status == "creado":
        print(f"[OK] Creado: {file_path}")
    else:
        print(f"[SKIP] Ya existe: {file_path}")
    return 0


def run_contest(parser_obj: Parser, url: str, fail_fast: bool) -> int:
    results = parser_obj.create_contest(url, continue_on_error=not fail_fast)

    created = 0
    skipped = 0
    errors = 0

    for status, file_path, problem_url in results:
        if status == "creado":
            created += 1
            print(f"[OK] {file_path}")
        elif status == "ya_existe":
            skipped += 1
            print(f"[SKIP] {file_path}")
        else:
            errors += 1
            print(f"[ERROR] {problem_url}")

    print(f"Resumen: creados={created}, existentes={skipped}, errores={errors}")
    return 1 if errors else 0


def main() -> int:
    cli = build_cli()
    args = cli.parse_args()
    parser_obj = Parser(path=args.path, timeout=args.timeout)

    try:
        if args.command == "problem":
            return run_problem(parser_obj, args.url)
        if args.command == "contest":
            return run_contest(parser_obj, args.url, args.fail_fast)
        cli.error("Comando no soportado.")
        return 2
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
