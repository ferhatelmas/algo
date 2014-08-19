package page15.q1444;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) throws Exception {
    String s = new Scanner(System.in).nextLine().replace("=", "===");
    ScriptEngine se = new ScriptEngineManager().getEngineByName("js");

    for(int i=1; i<10; i++)
      for(int j=1; j<10; j++)
        for(int k=1; k<10; k++) {
          String r = s.replaceAll("A", String.valueOf(i))
                      .replaceAll("B", String.valueOf(j))
                      .replaceAll("C", String.valueOf(k));
          if((Boolean)se.eval(r)) {
            System.out.println(r.replaceFirst("===", "="));
            return;
          }
        }
  }
}
