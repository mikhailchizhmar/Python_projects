## SmartCalc_v3_Python

### Project structure:

```plaintext
src/
├── frontend/
│   ├── index.html
│   ├── icon.icns
│   ├── view.py
├── backend/
│   ├── s21_calc_model.cpp
│   ├── s21_calc_model.h
├── tests/
|   ├── test.py
├── libcalc.dylib
├── main.py
├── model.py
├── presenter.py
├── install_script.sh
├── build_pkg.sh
├── history.json
├── requirements.txt
```


### How to work with this project:

1. You can open SmartCalc_v3 application via terminal (from ``src`` directory):

        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt

* To install dynamic library:

        g++ -arch x86_64h -std=c++17 -fPIC -c backend/s21_calc_model.cpp -o s21_calc_model.o
        g++ -arch x86_64h -dynamiclib -o libcalc.dylib s21_calc_model.o 

* To launch:

        python3 main.py

2. You can open SmartCalc_v3 application via installation (here is represented ``MacOS`` installation):

        chmod +x install_script.sh
        chmod +x build_pkg.sh
        ./build_pkg.sh


        - Open .pkg installer
        - Install the App
        - Open the App via Desktop

3. To run tests (from ``tests/`` folder):

        python3 -m unittest -b tests/test.py


