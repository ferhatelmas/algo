package com.ferhatelmas.eolimp.page36.q1077;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

  public static void main(String[] args) {
    String v = new Scanner(System.in).nextLine();

    if(isError(v)) {
      System.out.println("Error!");
      return;
    }

    Matcher m;
    StringBuffer sb = new StringBuffer();
    if(v.contains("_")) {
      m = Pattern.compile("_([a-z])").matcher(v);
      while(m.find()) m.appendReplacement(sb, m.group(1).toUpperCase());
    } else {
      m = Pattern.compile("([A-Z])").matcher(v);
      while(m.find()) m.appendReplacement(sb, "_" + m.group(1).toLowerCase());
    }
    m.appendTail(sb);
    System.out.println(sb.toString());
  }

  private static boolean isError(String s) {
    return s.endsWith("_") || s.matches("[^a-z].*") ||
           s.matches(".*([^\\w_]|(_[^a-z])).*")     ||
           (!s.equals(s.toLowerCase()) && s.contains("_"));
  }
}
