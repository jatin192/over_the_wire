#include <iostream>
#include <string>
using namespace std;

int main() {
    string text = "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4"; // ROT13 string

    for (char &c : text) {
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) 
        {
            if ((c >= 'A' && c <= 'M') || (c >= 'a' && c <= 'm'))
            {
                c += 13;  
            }    
            else
            {
                c -= 13;  
            }
        }
    }
    cout << text << endl; 
    return 0;
}



/*

ASCII of 'C' = 67
c += 13 → 67 + 13 = 80
ASCII 80 → 'P'


a................m................z
1st             13th             26th


Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

*/