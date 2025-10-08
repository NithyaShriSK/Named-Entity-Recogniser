
import gradio as gr
from transformer import NERExtractor
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

ner_extractor = NERExtractor()

def ner_app(text):
    if not text.strip():
        return "⚠️ Please enter some text to analyze.", None

    entities = ner_extractor.extract_entities(text)
    if not entities:
        return "No named entities found.", None

 
    df = pd.DataFrame(entities)

   
    counts = Counter(df["Entity Type"])
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values(), color='skyblue')
    ax.set_title("Entity Distribution")
    ax.set_xlabel("Entity Type")
    ax.set_ylabel("Count")

    return df, fig


interface = gr.Interface(
    fn=ner_app,
    inputs=gr.Textbox(lines=10, placeholder="Enter or paste your text..."),
    outputs=[gr.Dataframe(headers=["Word", "Entity Type", "Confidence"]), gr.Plot()],
    title="🧠 Named Entity Recognition (NER)",
    description="Extract named entities (Person, Organization, Location, etc.) and visualize entity distribution using a pre-trained BERT model.",
)

interface.launch(share=True)
