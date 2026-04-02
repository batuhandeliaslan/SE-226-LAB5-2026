#include <iostream>

double solve_sn_recursive(int n) {
    if (n == 1) {
        return 1.0;
    }
    
    double term = 1.0 / n;
    if (n % 2 == 0) {
        return solve_sn_recursive(n - 1) - term;
    } else {
        return solve_sn_recursive(n - 1) + term;
    }
}

int main() {
    int n;
    std::cin >> n;
    
    if (n > 0) {
        std::cout << solve_sn_recursive(n) << std::endl;
    }
    
    return 0;
}
