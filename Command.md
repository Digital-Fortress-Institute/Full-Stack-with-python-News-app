python -m venv enironmentname    -- To create python virtual environmnet
(for gitbash or terminal)source  enironmentname/Scripts/activate   --To activate the python virtual environment

pip freeze > requirements.txt    --To generate all the libraries or packages used in a program
pip install -r requirements.txt  --To install all packages or library listed in the requirements.txt

flask --app hello run --debug  -- To start local server on debug mode
flask run --host=0.0.0.0    --To run development server on a visible server