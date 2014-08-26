package vol12.p2136;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int[] freq = new int[26];

    for(int i=0; i<4; i++) {
      char[] chars = in.nextLine().toCharArray();
      for(char c : chars)
        if(c >= 'A' && c <= 'Z') freq[c-'A']++;
    }

    int max = 0;
    for(int f : freq) max = Math.max(max, f);

    StringBuilder sb1 = new StringBuilder(), sb2 = new StringBuilder();
    while(max > 0) {
      int p = 25;
      for(int i=0; i<freq.length; i++) {
        if(freq[i] == max) {
          sb1.append('*');
          freq[i]--;
          p = i;
        }
        else sb1.append(' ');
        sb1.append(' ');
      }
      max--;
      sb1.delete(2*p+1, 2*freq.length);
      sb1.append('\n');
      sb2.append(sb1.toString());
      sb1 = new StringBuilder();
    }
    for(int i=0; i<25; i++) {
      sb2.append((char)((int)'A'+i));
      sb2.append(' ');
    }
    sb2.append("Z\n");
    System.out.println(sb2.toString());
  }

}
