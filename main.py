def custom_sum(number):
    if number == 0:
        return 0
    else:
        return number % 10 + custom_sum(number // 10)


result_with_recursion = custom_sum(1234)
print("Результат з рекурсією:", result_with_recursion)
