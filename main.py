from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    gender: str
    age: int

# for reading json file, people.json when the program starts,
with open('people.json', 'r') as f:
    # into people variable, load people category from f (which is the people.json file)
    people = json.load(f)['people']

print(people)


# defining a function to retrieve a single person information using id
@app.get('/person/{p_id}', status_code=200)
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id] # person list will be created
    return person[0] if len(person) > 0 else {}