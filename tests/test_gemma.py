import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from generation.gemma_gen import GemmaGenerator
from retrieval.context_builder import ContextBuilder


def main():
    context_builder = ContextBuilder()
    query = "How many people's names are there?"
    context, _ = context_builder.build_context(query, topk=5, rerank_topk=2)

    generator = GemmaGenerator("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    answer = generator.generate(query, context)
    print(answer)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(str(exc))
        print("Request access to the model on Hugging Face, then run 'huggingface-cli login'.")


