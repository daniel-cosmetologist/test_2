from A import run as run_a
from B import run as run_b
from C import run as run_c
from D import run as run_d
from E import run_text_analyzer

def main():
    print("Запуск задачи A:")
    run_a()
    
    print("\nЗапуск задачи B:")
    run_b()
    
    print("\nЗапуск задачи C:")
    run_c()
    
    print("\nЗапуск задачи D:")
    run_d()
    
    print("\nЗапуск задачи E и F:")
    run_text_analyzer()

if __name__ == "__main__":
    main()
