#include <random>
#include <iostream>
#include <bitset>

int main() {
/**
     * @details
     * 1. Использует генератор случайных чисел (`std::random_device`)
     * 2. Применяет 64 битный вихрь Мерсенна (`std::mt19937`) для генерации
     * 3. Выводит результат в консоль
     *
     * @return 0 при успешном выполнении
*/
    std::random_device rd;
    std::mt19937_64 gen(rd());
    uint64_t high = gen();
    uint64_t low = gen();

    // Print as a 128-bit binary sequence
    std::bitset<64> high_bits(high);
    std::bitset<64> low_bits(low);
    std::cout << high_bits << low_bits << std::endl;

    return 0;
}