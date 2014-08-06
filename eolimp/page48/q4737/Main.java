package page48.q4737;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    StringBuilder sb = new StringBuilder();
    String ss[] = new Scanner(System.in).nextLine().trim().split("\\s+");
    for(String s : ss)
      sb.append(' ').append(s.trim());
    System.out.println(ss.length > 0 ? sb.substring(1) : "");
  }
}
