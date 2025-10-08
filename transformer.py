from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

class NERExtractor:
    def __init__(self, model_name="dslim/bert-base-NER"):
        print("🔄 Loading NER model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.ner_pipeline = pipeline(
            "ner",
            model=self.model,
            tokenizer=self.tokenizer,
            aggregation_strategy="max"
        )
        print("✅ Model loaded successfully!")

    def extract_entities(self, text):
        if not text.strip():
            return []

        entities = self.ner_pipeline(text)
        
        formatted = [
            {"Word": e["word"], "Entity Type": e["entity_group"], "Confidence": round(e["score"], 2)}
            for e in entities
        ]
        return formatted
