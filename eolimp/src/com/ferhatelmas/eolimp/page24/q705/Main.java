package com.ferhatelmas.eolimp.page24.q705;

import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;
import java.util.Arrays;
import java.util.Scanner;


public class Main {

  private static char[] c = new char[17],
                  symbols = new char[]{' ', '+', '-'};
  private static ScriptEngine engine = new ScriptEngineManager().getEngineByName("JavaScript");

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    Arrays.fill(c, ' ');
    for(int i=0; i<c.length; i+=2)
      c[i] = (char)((int)'0' + i/2 + 1);

    for(int i=0; i<t; i++) {
      getZeroSum(in.nextInt(), 1);
      if(i < t-1) System.out.println();
    }
  }

  private static void getZeroSum(int n, int offset) {
    if(offset == 2*n-1) {
      doSum(n);
      return;
    }

    for(char ch : symbols) {
      c[offset] = ch;
      getZeroSum(n, offset+2);
    }
  }

  private static void doSum(int n) {
    try {
      String s = new String(c).substring(0, 2*n-1);
      if(((Double)engine.eval(s.replace(" ", ""))).intValue() == 0) System.out.println(s);
    } catch(ScriptException s) {}
  }
}
