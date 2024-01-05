from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import gunicorn
import uvicorn
from model import nlp_summarizer
from mangum import Mangum




app = FastAPI()
handler = Mangum(app)

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers=["*"]
                   )

@app.get("/")
def summarize(text:str):
    result = nlp_summarizer(text)
    return JSONResponse({"pred":result})

if __name__ =="__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

    #if not result:
        #raise HTTPException(status_code=400)
    
    #return result