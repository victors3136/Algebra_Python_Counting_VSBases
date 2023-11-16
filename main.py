INPUT_FILES = ["input_1.txt", "input_2.txt", "input_3.txt", "input_4.txt", "input_5.txt"]
OUTPUT_FILES = ["output_1.txt", "output_2.txt", "output_3.txt", "output_4.txt", "output_5.txt"]


def number_of_bases(number_of_dimensions) -> int:
    if number_of_dimensions <= 0:
       raise ValueError()
    product: int = 1
    two_to_n: int = 2 ** number_of_bases
    current: int = 1
    for index in range(number_of_dimensions):
        product *= two_to_n - current
        current *= 2
    return product


def output_solution(found_solution, number_of_dimensions, out):
    format_specifier: str = "{0:0" + str(number_of_dimensions) + "b}"
    matrix: list[list[str]] = [list(format_specifier.format(vector)) for vector in found_solution]
    for index in range(number_of_dimensions):
        for vector in matrix:
            out.write(" [" + str(vector[index]) + "] ")
        out.write("\n")
    out.write("____________________\n")


def bitwise_added_pairs_of_vectors(list_of_vectors: list[int], length: int):
    return {list_of_vectors[i] ^ list_of_vectors[j]
            for i in range(length)
            for j in range(i + 1, length)}


def is_linearly_independent(list_of_vectors, number_of_dimensions) -> bool:
    if len(list_of_vectors) == 0:
        return True
    if list_of_vectors[-1] == 0:
        return False
    length: int = len(list_of_vectors)
    match length:
        case 1:
            return True
        case 2:
            return (list_of_vectors[0] ^ list_of_vectors[1]) != 0
        case 3:
            bitwise_addition_of_pairs = bitwise_added_pairs_of_vectors(list_of_vectors, length)
            return not (list_of_vectors[length - 1] in list_of_vectors[:(length - 1)]
                        or list_of_vectors[length - 1] in bitwise_addition_of_pairs)
        case 4:
            bitwise_addition_of_pairs = bitwise_added_pairs_of_vectors(list_of_vectors, length)
            bitwise_addition_of_triple = list_of_vectors[0] ^ list_of_vectors[1] ^ list_of_vectors[2]
            return not (list_of_vectors[length - 1] in list_of_vectors[:(length - 1)]
                        or list_of_vectors[length - 1] in bitwise_addition_of_pairs
                        or list_of_vectors[length - 1] == bitwise_addition_of_triple)
        case _:
            return len(list_of_vectors) <= number_of_dimensions


def generate_possible_bases(number_of_dimensions, out):
    possible_solution: list[int] = [0]
    while len(possible_solution) > 0:
        linearly_independent: bool = False
        while not linearly_independent and possible_solution[-1] < 2 ** number_of_dimensions - 1:
            possible_solution[-1] += 1
            linearly_independent = is_linearly_independent(possible_solution[:], number_of_dimensions)
        if linearly_independent:
            if len(possible_solution) == number_of_dimensions:
                output_solution(possible_solution, number_of_dimensions, out)
            possible_solution.append(0)
        else:
            possible_solution = possible_solution[:-1]


if __name__ == "__main__":
    user_input: int = abs(int(input("Pick the number of the input and output files (integer between 1 and 5):")) - 1)
    input_file = open(INPUT_FILES[user_input], "r")
    output_file = open(OUTPUT_FILES[user_input], "w")
    dimensions: int = int(input_file.read())
    if dimensions == 1:
        output_file.write("For 1 dimension, there is " + str(number_of_bases(dimensions)) + " base.\n\n")
    else:
        output_file.write(
            "For " + str(dimensions) + " dimensions, there are " + str(number_of_bases(dimensions)) + " bases.\n\n")
    if dimensions <= 4:
        generate_possible_bases(dimensions, output_file)
    input_file.close()
    output_file.close()
