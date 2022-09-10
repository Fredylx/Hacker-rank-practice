/*
Title     : Return Sum
Domain    : Java
Author    : Fredy
*/

String[] sNums = jTextField1.getText().replaceAll("[^1-9]", "").split("(?<!^)");
int sum = 0;
for (String s : sNums) {
    sum += Integer.parseInt(s); // add all digits
}

while (sum > 9) { // add all digits of the number, until left with one-digit number
    int temp = 0;
    while (sum > 0) {
        temp += sum % 10;
        sum = sum / 10;
    }
    sum = temp;
}
