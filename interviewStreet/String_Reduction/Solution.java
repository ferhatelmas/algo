import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        int results[] = new int[T];

        for(int i=0; i<T; i++) {

            results[i] = solve(br.readLine());

        }

        for(int i : results) {

            System.out.println(i);

        }

    }

    private static int solve(String s) {

        if(s.length() == 1) return 1;
        if (s.length() == 2 && s.charAt(0) == s.charAt(1)) return 2;

        int min = s.length();
        for(int i=0; i<s.length()-1; i++) {

            if(s.charAt(i) != s.charAt(i+1)) {
                StringBuilder sb = new StringBuilder();
                sb.append(s.substring(0, i));
                sb.append(getOtherChar(s.charAt(i), s.charAt(i+1)));
                sb.append(s.substring(i+2));

                int reduced = solve(sb.toString());
                if(reduced < 3) return reduced;
                min = Math.min(reduced, min);
            }

        }

        return min;

    }

    private static char getOtherChar(char c1, char c2) {

        char ch[] = {'a', 'b', 'c'};
        for(char c : ch) {
            if(c1 != c && c2 != c) return c;
        }
        return 'a';
    }

}
