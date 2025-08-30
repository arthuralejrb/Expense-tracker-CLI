# Expense-tracker-CLI
A CLI-based expense tracker built in Python. It uses `argparse` for robust command-line argument handling and the `rich` library for clear, formatted, and visually enhanced output in the terminal. 

## Features

- **Add an expense** You will be able to adds expense with details such as amount, category and description

- **Update an expense** You can update expenses informations as you please

- **Delete an expense** You can delete any expenses you want, or all of them at once 

- **List expenses** You can list all expenses, possibly filtering them by category

- **Show summary** You can see a summary of all expenses, optionally you can see only the summary of a given month

- **Set a budget** You can set a limited budget for any given month

- **Exports to CSV** You can export all your expenses to a CSV file, so you can work with them in your spreadsheet


## Installation
    1. Clone git repository
    ```
    git clone https://github.com/arthuralejrb/Expense-tracker-CLI
    ```


    2. Create a virtual enviroment
    ```
    python -m venv venv
    ```


    3. Activate the virtual enviroment
    ```
    # On MacOS and Linux:
    source venv/bin/activate
    
    # On Windows:
    ./venv/Scripts/activate
    ```


    4. Install all requirements
    ```
    pip install -r requirements.txt
    ```


## Usage

```
python3 main.py add --amount 100 --d Lego --category Gifts #Adds an expense
python3 main.py add --a 40 --description "books" #Another expense
python3 main.py list #Lists all expenses
python3 main.py list --c Gifts #Lists all expenses by category
python3 main.py update --id 1 --amount 75 #Updates an expense
python3 main.py delete --id 2 #Deletes an expense
python3 main.py delete --all #Deletes all expenses
python3 main.py budget --month 4 --amount 300 #Sets a budget for a given month
python3 main.py summary #Shows a summary of all expenses
python3 main.py summary --month #Shows a summary of all expenses in a given month
python3 main.py csv #Exports all data to a .CSV file
```


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.


### Inspired by: https://roadmap.sh/projects/expense-tracker
