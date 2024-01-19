# letters = "Z, O, N, R, I, A, C"
# middle_letter = "R"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "^[zonriac]{4,}$"