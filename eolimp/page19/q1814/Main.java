package page19.q1814;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s;

    while(!(s = in.nextLine()).equals("#")) {
      StringBuilder sb = new StringBuilder();
      boolean isValid = true;
      for(char c : s.toCharArray()) {
        switch(c) {
          case 'b': sb.append('d'); break;
          case 'd': sb.append('b'); break;
          case 'p': sb.append('q'); break;
          case 'q': sb.append('p'); break;
          default:
            if("iowvx".indexOf(c) > -1) sb.append(c);
            else isValid = false;
        }
        if(!isValid) break;
      }
      System.out.println(isValid ? sb.reverse().toString() : "INVALID");
    }
  }
}
