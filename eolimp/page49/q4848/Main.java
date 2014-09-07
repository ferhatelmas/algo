package page49.q4848;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    ArrayList<Integer> ls = new ArrayList<Integer>();

    while(in.hasNextInt())
      ls.add(in.nextInt());

    Collections.sort(ls);
    StringBuilder sb = new StringBuilder();
    for(int i : ls)
      sb.append(' ').append(i);
    System.out.println(sb.length() == 0 ? "" : sb.substring(1));
  }
}
