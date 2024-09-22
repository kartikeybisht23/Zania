import openai

class QuestionAnswerer:
    def __init__(self, retriever):
        self.retriever = retriever
        openai.api_key = ''

    def is_word_to_word_match(self, question, answer):
        # Simple heuristic to check if the answer matches the question word-to-word
        return question.strip().lower() == answer.strip().lower()

    def answer_questions(self, questions):
        answers = {}
        for question in questions:
            relevant_chunks = self.retriever.retrieve(question)
            context = " ".join(relevant_chunks)

            # Check if the context contains a word-for-word match with the question
            if self.is_word_to_word_match(question, context):
                answer = context
            else:
                # Use GPT model to generate the answer
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",  # Adjust based on the model available
                    messages=[
                        {"role": "user", "content": f"{context}\nAnswer the question: {question}"}
                    ],
                    max_tokens=100
                )

                answer = response.choices[0].message["content"].strip()

                # Check if the confidence in the answer is low
                if not answer or len(answer) < 2:  # If answer is too short or seems low quality
                    answer = "Data Not Available"

            answers[question] = answer
        return answers
