#include <iostream>
#include <boost/filesystem.hpp>
#include <iostream>
#include <fstream>
using namespace std;


int main() {
    string folder = "Hello";

    namespace fs = boost::filesystem;
    boost::filesystem::path full_path = fs::system_complete("../Models/"+folder);

    if(boost::filesystem::create_directory(full_path)) {
        cout << "Success" << "\n";
    }

    ofstream myfile;
    cout << ("../Models/"+folder+"/model.config");
    myfile.open ("../Models/"+folder+"/model.config");
    myfile << "Here will be config.\n";
    myfile.close();

    return 0;
}

void create_sdf(double width, double length, double depth, string file_name){
    cout << "Inside create sdf";
}