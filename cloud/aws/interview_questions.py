"""This module contains the methods to 
write interview questions to a dynamo db
"""
import boto3
import uuid
import json

def insert_question(question: dict):
    """This method inserts a question
    to the dynamo db
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Questions')
    item = {
        "id": str(uuid.uuid4())
    }
    item.update(question)
    table.put_item(Item=item)


def get_interview_questions():
    """This method gets the interview questions
    from the dynamo db
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Questions')
    response = table.scan()
    return response['Items']

if __name__ == "__main__":
    # insert_question({
    #     "question": "What is the difference between a class and an object?",
    #     "answer": "A class is a blueprint for creating objects, while an object is an instance of a class."
    # })
    # insert_question({
    #     "question": "What is difference between list and tuple",
    #     "answer": "Lists are mutable, tuples are immutable."
    # })
    # questions = []
    # for question in get_interview_questions():
    #     questions.append(question)
    print(json.dumps(get_interview_questions(), indent=4))

    
    