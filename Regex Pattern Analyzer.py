import re
import tkinter as tk
from tkinter import ttk

def analyze_regex_pattern(pattern):
    try:
        compiled_pattern = re.compile(pattern)
        pattern_components = {
            'pattern': pattern,
            'is_regular': is_regular_language(pattern),
            'pattern_structure': get_pattern_structure(compiled_pattern),
            'match_example': get_match_example(pattern),
            'min_accepted_string': get_min_accepted_string(compiled_pattern),
            'num_groups': compiled_pattern.groups
        }
        return pattern_components
    except re.error as e:
        return {'error': str(e)}

def is_regular_language(pattern):
    try:
        re.compile(f"({pattern})?")
        return True
    except re.error:
        return False

def get_match_example(pattern):
    example_input = "abab"
    match = re.search(pattern, example_input)
    return match.group() if match else "No match example"

def get_min_accepted_string(compiled_pattern):
    # Generate the minimum accepted string for the given pattern
    min_accepted_string = ""
    pattern = compiled_pattern.pattern
    inside_group = False  # Flag to track if we're inside a group
    
    # Traverse the pattern character by character
    i = 0
    while i < len(pattern):
        if pattern[i] == '(':
            inside_group = True
            i += 1
        elif pattern[i] == ')':
            inside_group = False
            i += 1
        elif pattern[i].isalpha() and not inside_group:  # Check if character is alphabet and not inside a group
            # Check if the next character is '*' (zero or more)
            if i < len(pattern) - 1 and pattern[i+1] == '*':
                i += 2  # Skip '*' and the alphabet
            else:
                min_accepted_string += pattern[i]
                i += 1
        elif pattern[i] == '|':  # If encountered '|' (OR operator) within a group
            if inside_group:
                # Find the next character which is an alphabet
                j = i + 1
                while j < len(pattern) and not pattern[j].isalpha():
                    j += 1
                if j < len(pattern):
                    min_accepted_string += pattern[j]
                break  # Break out of the loop after processing '|' and alphabet
        else:
            i += 1  # Move to the next character
    
    return min_accepted_string



def get_pattern_structure(compiled_pattern):
    pattern_structure = []
    for element in compiled_pattern.pattern:
        if element.isalpha():
            pattern_structure.append(f'Character: {element}')
        elif element == '|':
            pattern_structure.append('Or')
        elif element == '(':
            pattern_structure.append('Start Group')
        elif element == ')':
            pattern_structure.append('End Group')
        elif element == '*':
            pattern_structure.append('Zero or more (*)')
        elif element == '+':
            pattern_structure.append('One or more (+)')
        elif element == '?':
            pattern_structure.append('Zero or one (?)')
    return pattern_structure

def analyze_button_click():
    regex_pattern = regex_entry.get()
    analysis_result = analyze_regex_pattern(regex_pattern)
    
    result_text.delete(1.0, tk.END)  # Clear previous result
    if 'error' in analysis_result:
        result_text.insert(tk.END, f"Error: {analysis_result['error']}")
    else:
        result_text.insert(tk.END, "Analysis Result:\n")
        for key, value in analysis_result.items():
            if key == 'pattern_structure':
                result_text.insert(tk.END, f"{key}:\n")
                for structure in value:
                    result_text.insert(tk.END, f"  {structure}\n")
            else:
                result_text.insert(tk.END, f"{key}: {value}\n")

def clear_button_click():
    regex_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

def clear_test_input():
    input_entry.delete(0, tk.END)
    test_result_label.config(text="")

def test_regex():
    input_text = input_entry.get()
    regex_pattern = regex_entry.get()
    result = "Accepted" if re.fullmatch(regex_pattern, input_text) else "Not Accepted"
    test_result_label.config(text=f"Regex Test Result: {result}")

# GUI setup
root = tk.Tk()
root.title("Regex Pattern Analyzer (Theory of Computation)")

# Regex entry
regex_label = ttk.Label(root, text="Enter a regex pattern:")
regex_label.pack(pady=10)

regex_entry = ttk.Entry(root, width=40)
regex_entry.pack()

# Analyze button
analyze_button = ttk.Button(root, text="Analyze Pattern", command=analyze_button_click)
analyze_button.pack(pady=10)

# Result text
result_text = tk.Text(root, height=15, width=70)
result_text.pack()

# Clear button
clear_button = ttk.Button(root, text="Clear", command=clear_button_click)
clear_button.pack(pady=10)

# Regex tester
regex_test_label = ttk.Label(root, text="Enter text for regex testing:")
regex_test_label.pack(pady=10)

input_entry = ttk.Entry(root, width=40)
input_entry.pack()

test_button = ttk.Button(root, text="Test Regex", command=test_regex)
test_button.pack(pady=10)

# Clear Test Input button
clear_test_input_button = ttk.Button(root, text="Clear Test Input", command=clear_test_input)
clear_test_input_button.pack(pady=10)

test_result_label = ttk.Label(root, text="")
test_result_label.pack(pady=10)

root.mainloop()