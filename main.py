from pdf_parser import PDFParser
from retrieval_model import Retriever
from question_answerer import QuestionAnswerer
from slack_notifier import SlackNotifier

def main(pdf_path, questions, slack_channel):
    # Step 1: Parse the PDF and chunk the text
    parser = PDFParser(pdf_path)
    document_chunks = parser.chunk_pdf()

    # Step 2: Initialize the retriever
    retriever = Retriever(document_chunks)

    # Step 3: Answer the questions using RAG
    qa = QuestionAnswerer(retriever)
    answers = qa.answer_questions(questions)

    # Step 4: Output the result as a structured JSON blob
    #json_output = json.dumps(answers, indent=4)
    #print(json_output)

    # Step 5: Post the results to Slack (commented out)
    
    slack = SlackNotifier(slack_channel)
    slack.post_results(answers)
    


if __name__ == "__main__":
    pdf_path = r"C:\Users\bisht\OneDrive\Desktop\handbook.pdf"
    questions = ["What is the name of the company?"]
    slack_channel = "C07NGELPU4B"
    main(pdf_path, questions, slack_channel)

