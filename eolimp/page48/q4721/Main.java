package page48.q4721;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int c = 0;
    for(char ch :new Scanner(System.in).next().toCharArray())
      if(ch == '5') c++;
    System.out.println(c);
  }
}
