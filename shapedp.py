from shapes import *
def load():
    file_name = input("Please enter the text file name: ")
    print("Processing <<", file_name, ">>")
    line_nb = 0
    l_set = []
    error_nb = 0
    with open(file_name, 'r') as file:
        # reading each line
        for line in file:
            line_nb += 1
            words = line.split()
            if words[0].lower() == "shape":
                l_set.append(Shape())
            elif words[0].lower() == "circle":
                if len(words) == 2 and float(words[1]) > 0:
                    l_set.append(Circle(float(words[1])))
                else:
                    error_nb += 1
                    print("Error: Invalid Circle on line", line_nb, line)
            elif words[0].lower() == "ellipse":
                if len(words) == 3 and float(words[1]) > 0 and float(words[2]) > 0:
                    l_set.append(Ellipse(float(words[1]), float(words[2])))
                else:
                    error_nb += 1
                    print("Error: Invalid Ellipse on line", line_nb, line)
            elif words[0].lower() == "rhombus":
                if len(words) == 3 and float(words[1]) > 0 and float(words[2]) > 0:
                    l_set.append(Rhombus(float(words[1]), float(words[2])))
                else:
                    error_nb += 1
                    print("Error: Invalid Rhombus on line", line_nb, line)
            else:
                error_nb += 1
                print("Error: Invalid Shape on line", line_nb, line)
            words = ''
    print("Processed",line_nb, "rows,", len(l_set), "shapes added,", error_nb, "errors.")
    return l_set
def toset(multi_set):
    print("Multi-set is converting to a set")
    unique_set = []
    for shapes in multi_set:
        is_duplicate = False
        for unique in unique_set:
            # compare equality based on type and parameters
            if type(shapes) == Shape and type(shapes) == type(unique):
                is_duplicate = True
                break
            elif type(shapes) == Circle and type(shapes) == type(unique) and shapes.radius == unique.radius:
                is_duplicate = True
                break
            elif type(shapes) == Ellipse and type(shapes) == type(unique) and shapes.semi_ma == unique.semi_ma and shapes.semi_mi == unique.semi_mi:
                is_duplicate = True
                break
            elif type(shapes) == Rhombus and type(shapes) == type(unique) and shapes.d1 == unique.d1 and shapes.d2== unique.d2:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_set.append(shapes)
    return unique_set
def save(im_set):
    file_name = input("Please enter the text file name to save: ")
    print("Saving the current in-memory database to a file <<", file_name, ">>")
    with open(file_name, 'w') as file:
        for shape in im_set:
            shape_name = type(shape).__name__
            if isinstance(shape, Circle):
                file.write(f"{shape_name} {shape.radius}\n")
            elif isinstance(shape, Ellipse):
                file.write(f"{shape_name} {shape.semi_ma} {shape.semi_mi}\n")
            elif isinstance(shape, Rhombus):
                file.write(f"{shape_name} {shape.d1} {shape.d2}\n")
            else:
                file.write(f"{shape_name}\n")
def prints(im_set):
    count = 0
    for shape in im_set:
        count += 1
        print(count, ": ", end="")
        shape.print()
def summary(im_set):
    output = []
    nb_c = 0
    nb_e = 0
    nb_r = 0
    nb_s = 0
    for shape in im_set:
        shape_name = type(shape).__name__
        if shape_name.lower() == "circle":
            nb_c += 1
        elif shape_name.lower() == "ellipse":
            nb_e += 1
        elif shape_name.lower() == "rhombus":
            nb_r += 1
        elif shape_name.lower() == "shape":
            nb_s += 1
    output.append(f"Circle(s): {nb_c}")
    output.append(f"Ellipse(s): {nb_e}")
    output.append(f"Rhombus(s): {nb_r}")
    for line in output:
        print(line)
    print(f"Shape(s): {nb_c+nb_e+nb_r+nb_s }")
def detail(im_set):
    for shape in im_set:
        shape_name = type(shape).__name__
        if isinstance(shape, Circle):
            print(f"{shape_name} {shape.radius}\n")
        elif isinstance(shape, Ellipse):
            print(f"{shape_name} {shape.semi_ma} {shape.semi_mi}\n")
        elif isinstance(shape, Rhombus):
            print(f"{shape_name} {shape.d1} {shape.d2}\n")
        else:
            print(f"{shape_name}\n")


def main():
    print("Please select the following: ")
    in_memory_set = []
    while True:
        print("LOAD ")
        print("TOSET")
        print("SAVE")
        print("PRINT")
        print("SUMMARY")
        print("DETAILS")
        print("QUIT")

        choice = input("Enter Choice: ")
        if choice == "LOAD":
            in_memory_set = load()
        elif choice == "TOSET":
            in_memory_set = toset(in_memory_set)
        elif choice == "SAVE":
            save(in_memory_set)
        elif choice == "PRINT":
            prints(in_memory_set)
        elif choice == "SUMMARY":
            summary(in_memory_set)
        elif choice == "DETAILS":
            detail(in_memory_set)
        elif choice == "QUIT":
            print("The program will terminate")
            quit()
        else:
            print("Invalid option. Please try again")

if __name__ == '__main__':
        main()