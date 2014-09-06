package page56.q5501;

import java.util.Scanner;

// Not enough memory for Java
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int i = 1, j = i, max = Integer.MIN_VALUE;

    while(in.hasNextLine()) {
      for(String s : in.nextLine().split("\\s")) {
        if(!s.isEmpty()) {
          int m = Integer.parseInt(s);
          if (m > max) {
            j = i;
            max = m;
          }
        }
      }
      i++;
    }
    System.out.println(max + " " + j);
  }
}
