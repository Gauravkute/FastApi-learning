window
python -m venv venv

linux
python3 -m venv venv

window--
venv/Scripts/Activate.ps1

linux--
. venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload