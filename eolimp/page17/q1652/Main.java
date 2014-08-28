package page17.q1652;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
  public static void main(String[] args) throws Exception {
    Scanner in = new Scanner(System.in);
    String s = in.nextLine();
    if(!(s.startsWith("-") || s.startsWith("+"))) s = "+".concat(s);

    ArrayList<Integer> is = new ArrayList<Integer>();
    Pattern p = Pattern.compile("([\\+\\-])");
    Matcher m = p.matcher(s);
    while(m.find())
      is.add(m.start());
    is.add(s.length());

    long sum = 0;
    String x = in.next();
    ScriptEngine e = new ScriptEngineManager().getEngineByName("js");
    for(int i=0, l=is.size(); i<l-1; i++) {
      String t = s.substring(is.get(i), is.get(i+1));
      if(!t.isEmpty()) {
        if(t.contains("x")) {
          if(t.contains("^"))
            t = t.replaceAll("x\\^\\d",
                "Math.pow(" + x + ", " + t.split("\\^")[1] + ")");
          else
            t = t.replaceAll("x", String.valueOf(x));
        }
        sum += ((Double)e.eval(t)).longValue();
      }
    }
    System.out.println(sum);
  }
}
