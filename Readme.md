
# 🧠 Named Entity Recogniser

A user-friendly web application for **Named Entity Recognition (NER)** using a pre-trained BERT model. Built with Hugging Face Transformers and Gradio, this tool allows you to extract and visualize named entities (like Person, Organization, Location) from any input text.

🔗 [Try the live demo on Hugging Face Spaces](https://huggingface.co/spaces/NithyaShriSK/NER_Named_Entity_Recognition)

---

## 📌 Features

- **Extracts Named Entities**: Identify entities such as persons, organizations, and locations in your text.
- **Visualizes Entity Distribution**: View a bar chart showing the frequency of each entity type.
- **Interactive Web Interface**: Easily input text and view results using Gradio's intuitive UI.

---

## 🧰 Requirements

To run this project locally, ensure you have the following Python packages installed:

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:

- `torch`: For model inference.
- `transformers`: To load the pre-trained BERT model.
- `gradio`: For creating the web interface.
- `pandas`: For handling data.
- `matplotlib`: For plotting the entity distribution.
- `numpy`: For numerical operations.
- `scikit-learn`: For machine learning utilities.
- `tqdm`: For progress bars.

---

## 🚀 Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/NithyaShriSK/Named-Entity-Recogniser.git
   cd Named-Entity-Recogniser
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://localhost:7860` to use the NER tool.

---

## 🧪 Example

Input:

```
Elon Musk is the CEO of SpaceX and Tesla, Inc., both based in California.
```

Output:

| Word      | Entity Type | Confidence |
|-----------|-------------|------------|
| Elon Musk     | PER         | 0.99       |
| SpaceX    | ORG         | 0.97       |
| Tesla     | ORG         | 0.96       |
| California| LOC         | 0.95       |

Bar chart visualizing the distribution of entity types.

---


