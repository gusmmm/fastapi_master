from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Ola Mundo!'}


if __name__ == '__main__':
    print(read_root())
