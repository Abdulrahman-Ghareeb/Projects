from continuous_exponential import continuous_exponential
from continuous_gaussian import continuous_gaussian
from continuous_uniform import continuous_uniform
from discrete_binomial import discrete_binomial
from discrete_geometric import discrete_geometric
from discrete_poisson import discrete_poisson
from discrete_bernoulli import discrete_bernoulli
from discrete_uniform import discrete_uniform

def print_box(text):
    line = "-" * (len(text) + 4)
    print(f"+{'-' * len(line)}+")
    print(f"|  {text}  |")
    print(f"+{'-' * len(line)}+")

def main_menu():
    while True:
        print_box("Distributions")
        print("Welcome to the probability distribution selector!")
        print_box("Options")
        print("1. Continuous")
        print("2. Discrete")
        choice = int(input("Enter your choice (1/2): "))

        if choice == 1:
            print_box("Continuous Options")
            print("1. Continuous Exponential")
            print("2. Continuous Gaussian")
            print("3. Continuous Uniform")
            cont_choice = int(input("Enter your choice (1/2/3): "))
            if cont_choice == 1:
                continuous_exponential()
            elif cont_choice == 2:
                continuous_gaussian(0, 1, sample_size=10000)
            elif cont_choice == 3:
                t = float(input("Enter minimum value: "))
                u = float(input("Enter maximum value: "))
                continuous_uniform(t,u)
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

        elif choice == 2:
            print_box("Discrete Options")
            print("1. Binomial")
            print("2. Geometric")
            print("3. Poisson")
            print("4. Bernoulli")
            print("5. Uniform")
            disc_choice = int(input("Enter your choice (1/2/3/4/5): "))
            if disc_choice == 1:
                discrete_binomial(10, 0.3)
            elif disc_choice == 2:
                discrete_geometric(0.3, 100)
            elif disc_choice == 3:
                discrete_poisson(10000,0.01)
            elif disc_choice == 4:
                discrete_bernoulli(0.8,1000)
            elif disc_choice == 5:
                t = float(input("Enter minimum value: "))
                u = float(input("Enter maximum value: "))
                discrete_uniform(t, u)
            else:
                print("Invalid choice! Please enter a valid option.")
        else:
            print("Invalid choice! Please enter 1 or 2.")

        another = input("Do you want to make another distribution? (type yes to continue, type ANYTHING to cancel): ")
        if another.lower() != 'yes':
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main_menu()
