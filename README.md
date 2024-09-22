Objective
 AI agent that leverages the capabilities of a large language model. This agent will be able to extract answers based on the content of a large PDF document and post the results on Slack. 


The structure of the code:

Zania_assignment/
¦
+-- pdf_parser.py          # Handles PDF text extraction and chunking
+-- retriever.py           # Embeds the PDF text chunks and retrieves relevant chunks for the question
+-- question_answerer.py   # Answers questions using OpenAI's GPT model
+-- slack_notifier.py      # Posts the results to a specified Slack channel
+-- main.py                # Orchestrates the entire process
+-- README.md              # Documentation for the project

1. pdf_parser.py
 This file contains the PDFParser class, responsible for extracting and chunking text from the PDF file.

 Methods:
  1.1 extract_text(): Extracts text from all pages of the PDF except for the first three.
  1.2 chunk_pdf(chunk_size=300): Splits the extracted text into chunks of approximately 300 words each for easier processing.

2. retriever.py
 This file contains the Retriever class, which retrieves relevant document chunks based on a question.

 Methods:
  2.1 embed_chunks(): Embeds the text chunks using the SentenceTransformer model.
  2.2 embed_query(query): Embeds the query (question) to match it with the chunk embeddings.
  2.3 retrieve(query, top_k=2): Retrieves the top-k relevant chunks from the document based on similarity with the query.

3. question_answerer.py
 This file contains the QuestionAnswerer class, which handles answering questions based on the retrieved chunks.

 Methods:
  3.1 is_word_to_word_match(question, answer): A heuristic to check if the retrieved chunk is an exact match for the question.
  3.2 answer_questions(questions): Uses the OpenAI API to generate answers for the provided questions based on the retrieved chunks.

4. slack_notifier.py
 This file contains the SlackNotifier class, which posts the generated answers to a Slack channel.

 Methods:
  4.1 post_results(answers): Posts the answers in a formatted message to a specified Slack channel using the Slack Web API.

5. main.py
 This file orchestrates the entire process:

 Parses the PDF using PDFParser.
 Retrieves relevant chunks using Retriever.
 Answers questions using QuestionAnswerer.
 Posts the answers to Slack using SlackNotifier.

