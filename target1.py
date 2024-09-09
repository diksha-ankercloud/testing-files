# target.py - Main file that uses classes and functions from context1.py and context2.py
from context1 import read_file
from context2 import PythonProcessor, transform_data, save_result

def main():
    file_path = 'data/input.txt'
    data = read_file(file_path)

    processor = PythonProcessor("Python File Processor")
    processed_data = processor.process(data)

    transformed_data = transform_data(processed_data)
    
    output_file_path = 'data/output.txt'
    save_result(transformed_data, output_file_path)

    print(f"Data processing complete. Results saved to {output_file_path}")

if __name__ == "__main__":
    main()
