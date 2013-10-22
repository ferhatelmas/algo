package page17.q1616;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    for(int i=2; i<Math.ceil(Math.sqrt(n)); i++)
      if(n%i == 0) {
        System.out.println("No");
        return;
      }
    System.out.println("Yes");
  }
}
