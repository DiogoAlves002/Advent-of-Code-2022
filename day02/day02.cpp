#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map> 

using std::istringstream;
using std::ifstream;
using std::string;
using std::cout;
using std::unordered_map;

int main(){


    string input;

    char opponent;
    char player;

    // part 1
    unordered_map<char, int> playerHands = {
        {'X', 1},
        {'Y', 2},
        {'Z', 3}
    };

    unordered_map<char, int> opponentHands_1 = {
        {'A', 3},
        {'B', 2},
        {'C', 1}
    };

    int points_1 = 0;
    
    // part 2
    unordered_map<char, int> opponentHands_2 = {
        {'A', 1},
        {'B', 2},
        {'C', 3}
    };
    
    int points_2 = 0; 

    ifstream inputFile("input.txt");
    while (getline(inputFile, input)){

        istringstream parsingStream(input);
        
        parsingStream >> opponent;
        parsingStream >> player;

        points_1 += (playerHands[player] * 3 + opponentHands_1[opponent] * 3) % 9 + playerHands[player]; 

        points_2 += (playerHands[player] - 1 ) * 3 + (playerHands[player] + opponentHands_2[opponent]) % 3 + 1 ; 

    } 

    
    inputFile.close();


    printf("Part 1: %i\n", points_1);
    printf("Part 2: %i\n", points_2);

    return 1;
}