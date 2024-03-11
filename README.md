# StoryDigest: Optimizing Novel Summaries for Comprehension

## Table of Contents
- [About](#about)
    - [Project Objective](#project-objective)
- [Prerequisites](#prerequisites)
- [Methodology](#methodology)
- [Results](#results)
- [Future Directions](#future-directions)
- [Contact](#contact)

## About
**StoryDigest** is an exploration to optimize novel summaries aiming to ascertain the ideal summary length that preserves a story's essence while enhancing reader comprehension. Utilizing advanced NLP techniques and Large Language Models (LLMs), this project seeks to:

1. **Summarization Experimentation**: Systematically summarize novels at varying lengths to investigate the impact on narrative understanding.
2. **Automated Evaluation**: Deploy machine learning models to assess summary effectiveness, focusing on preserving critical plot points and overall story arc.

### Project Objective
To determine how to optimally summarize novels to ensure readers grasp the majority of a story, enhancing the learning and reading experience in educational settings and beyond.

## Prerequisites
If you wish to go through the code, ensure you have Python installed on your machine and the following packages for running the project scripts:

```
pip install transformers requests numpy pandas scipy sklearn requests beautifulsoup4

```

- ## Methodology
The project's methodology is multifaceted, involving:
- **Data Collection**: Utilizing Project Gutenberg's repository of over 70,000 free ebooks, with a focus on selecting 'newer' books to avoid the confounding effect of translating Old English in the summarization process. Summary examples for training will initially be sourced from SparkNotes, providing both chapter-specific and entire novel summaries.
- **Model Exploration**: Initial phases will test both encoder-decoder and decoder-only models to assess their efficacy in novel summarization. The exploration includes pretrained Mamba models, known for their selectivity in processing, to potentially enhance summary quality.
- **Evaluation Metrics**: A dual approach incorporating n-gram based metrics (ROUGE, BLEU, METEOR, Sentence-BLEU) and embedding-based metrics (BERTscore, BLEURT) to comprehensively assess summary effectiveness.


## Results
*As the StoryDigest project is in its active stages of development and experimentation, this section is poised to evolve. Upon completion of the summarization experiments, it will be updated to showcase our findings, including insights into the optimal summary lengths and styles that best support narrative comprehension and retention. We are committed to sharing our discoveries and breakthroughs in enhancing the understanding of complex narratives through optimized summarization.*


## Contact
For inquiries or collaboration proposals, please contact me at sergiy12422@gmail.com or connect on [LinkedIn](https://www.linkedin.com/in/sergiy-chepiga/).

