import sys

from .utils import parse_args
from .algoritmos.gemini_integration import GeminiClient

# Entry point do pacote


def main():
    print("Meu pacote python começa aqui!")
    args = parse_args()
    try:
        # url = args.url
        problema = args.problema
        print(f"Problema: {problema}")
        
        print(f"Geração de Texto básico")
        gemini_client = GeminiClient(api_key='tua-chave', model_name='gemini-2.0-flash', max_output_tokens=500)
        response_text = gemini_client.generate_response(problema)
        
        print(f"resposta: {response_text}\n")
        
        
        return 0
    except Exception as e:
        print(f"Erro: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
