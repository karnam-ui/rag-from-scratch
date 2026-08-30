from transformers import AutoModelForCausalLM, AutoTokenizer


class GemmaGenerator:
    DEFAULT_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    def __init__(self, model_name=None):
        self.model_name = model_name or self.DEFAULT_MODEL
        self._validate_access(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    @staticmethod
    def _validate_access(model_name):
        # This project now targets a public model with no gated auth requirement.
        return None

    def generate(self, query, context):
        messages = [
    {
        "role": "system",
        "content": """You are a Project Query assistant.

        Answer the user's question ONLY using the provided context.

        If the context does not contain sufficient information,
        say that "the provided context does not contain sufficient information."

        Do not invent facts, numbers, names, or procedures."""
    },
    {
        "role": "user",
        "content": f"""CONTEXT:
        {context}

        QUESTION:
        {query}"""
    }
]

        prompt = self.tokenizer.apply_chat_template(messages, tokenize = False,add_generated_prompt=True, add_eos_token=True)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        input_length = inputs["input_ids"].shape[1]
        outputs = self.model.generate(**inputs, max_length=500)
        generated_tokens = outputs[0][input_length:]
        answer = self.tokenizer.decode(generated_tokens,skip_special_tokens=True)
        return answer

    