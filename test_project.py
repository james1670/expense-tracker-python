from unittest.mock import patch
import project


def main():
    test_take_action()
    test_take_input()
    test_validate_input()


def test_take_action():
    with patch('project.input', side_effect=["1", "2024-10-10", "Food", "100", "0"]), \
         patch('project.data_handler.log_expense') as mock_log_expense:
        
        project.take_action()

        mock_log_expense.assert_called_once_with("Expenses.csv", "2024-10-10", "Food", "100")
    
    with patch('project.input', side_effect=["2", "0"]), \
         patch('project.data_handler.retrieve_expenses') as mock_retrieve_expenses:
        
        project.take_action()

        mock_retrieve_expenses.assert_called_once_with("Expenses.csv")

    with patch('project.input', side_effect=["3", "0"]), \
         patch('project.data_handler.check_budget') as mock_check_budget:
        
        project.take_action()

        mock_check_budget.assert_called_once_with("Expenses.csv")

    with patch('project.input', side_effect=["5", "0"]), \
         patch('project.data_handler.edit_or_delete_expense') as mock_edit_expense:
        
        project.take_action()

        mock_edit_expense.assert_called_once_with("Expenses.csv", "edit")

    with patch('project.input', side_effect=["6", "0"]), \
         patch('project.data_handler.edit_or_delete_expense') as mock_delete_expense:
        
        project.take_action()

        mock_delete_expense.assert_called_once_with("Expenses.csv", "delete")



def test_take_input():    
    with patch('builtins.input', side_effect=["2024-10-10", "Food", "100"]), \
         patch('project.validate_input', side_effect=[True, True, True]):

        result = project.take_input()

        assert result == ("2024-10-10", "Food", "100"), "The function should return valid input values"

    with patch('builtins.input', side_effect=["invalid-date", "Food", "100"]), \
         patch('project.validate_input', side_effect=[False, True, True]):
        
        with patch('builtins.print') as mock_print:
            project.take_input()
            mock_print.assert_called_with("\nInvalid DATE\n")

    # Test invalid category input
    with patch('builtins.input', side_effect=["2024-10-10", "invalid-category", "100"]), \
         patch('project.validate_input', side_effect=[True, False, True]):
        
        with patch('builtins.print') as mock_print:
            project.take_input()
            mock_print.assert_called_with("\nInvalid CATEGORY\n")

    with patch('builtins.input', side_effect=["2024-10-10", "Food", "invalid-amount"]), \
         patch('project.validate_input', side_effect=[True, True, False]):
        
        with patch('builtins.print') as mock_print:
            project.take_input()
            mock_print.assert_called_with("\nInvalid AMOUNT\n")



def test_validate_input():
    # Test valid date inputs
    assert project.validate_input("2024-10-10", "date") == True
    assert project.validate_input("2024-02-29", "date") == True
    assert project.validate_input("2024-01-01", "date") == True

    # Test invalid date inputs
    assert project.validate_input("2024-10-32", "date") == False
    assert project.validate_input("2024-13-01", "date") == False
    assert project.validate_input("invalid-date", "date") == False

    # Test valid category inputs
    assert project.validate_input("Food", "category") == True
    assert project.validate_input("Transport", "category") == True
    assert project.validate_input("Entertainment", "category") == True

    # Test invalid category inputs
    assert project.validate_input("InvalidCategory", "category") == False
    assert project.validate_input("1234", "category") == False

    # Test valid amount inputs
    assert project.validate_input("100", "amount") == True
    assert project.validate_input("0", "amount") == True
    assert project.validate_input("100.50", "amount") == True

    # Test invalid amount inputs
    assert project.validate_input("-50", "amount") == False
    assert project.validate_input("invalid-amount", "amount") == False



if __name__ == "__main__":
    main()
