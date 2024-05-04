import sys
import ast

def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

            # Utilizar el módulo ast para analizar el código Python y contar las líneas
            tree = ast.parse(code)
            code_lines = sum(1 for node in ast.walk(tree) if isinstance(node, ast.stmt))

            return code_lines
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    # Verificar si se proporciona exactamente un argumento de línea de comando
    if len(sys.argv) != 2:
        print("Too few or too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    # Verificar si el nombre del archivo especificado termina en ".py"
    if not file_path.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    # Contar las líneas de código en el archivo especificado
    lines_of_code = count_lines_of_code(file_path)
    print(lines_of_code)
