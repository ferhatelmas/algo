package page51.q5089;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    ArrayList<String> s = new ArrayList<String>(in.nextInt());
    while(in.hasNext()) s.add(in.next());
    Collections.sort(s);
    for(String ss : s) System.out.println(ss);
  }
}
