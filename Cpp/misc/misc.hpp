#include <iostream>
#include <vector>

std::vector<std::string> split(std::string target, char splitBy);

std::vector<std::string> split(std::string target, char splitBy) { 
    std::vector<std::string> output = std::vector<std::string>();
    int cur_pointer = 0;
    for(int i = 0; i < target.length();i++){
        
        if (target[i] == splitBy){
            output.push_back(target.substr(cur_pointer, i-cur_pointer));
            cur_pointer = i+1;
        }
        else if (i == target.length()-1){
            output.push_back(target.substr(cur_pointer));
        }
    }
    return output;
}
