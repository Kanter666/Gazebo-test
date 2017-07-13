#include <iostream>
#include <boost/filesystem.hpp>


int main() {
    std::string folder = "Hello";

    namespace fs = boost::filesystem;
    boost::filesystem::path full_path = fs::system_complete("../Models/"+folder);

    if(boost::filesystem::create_directory(full_path)) {
        std::cout << "Success" << "\n";
    }
    return 0;
}