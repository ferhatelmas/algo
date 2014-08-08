package page10.q947;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    System.out.println(new StringBuilder(new Scanner(System.in)
        .nextLine().replaceAll("\\D", "")).reverse().toString());
  }
}