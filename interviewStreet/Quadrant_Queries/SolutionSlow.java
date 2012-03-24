import java.util.Scanner;

public class SolutionSlow {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int points[][] = new int[N][2];

        for(int i=0; i<N; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }

        int Q = sc.nextInt();

        for(int i=0; i<Q; i++) {

            String q = sc.next();
            int min = sc.nextInt();
            int max = sc.nextInt();

            if(q.equals("C")) {
                int c1 = 0, c2 = 0, c3 = 0, c4 = 0;

                for(int j=min-1; j<max; j++) {
                    if(points[j][0] > 0) {
                        if(points[j][1] > 0) c1++;
                        else c4++;
                    } else {
                        if(points[j][1] > 0) c2++;
                        else c3++;
                    }
                }

                System.out.println(c1 + " " + c2 + " " + c3 + " " + c4);
            } else if(q.equals("X")){
                for(int j=min-1; j<max; j++) {
                    points[j][1] = -points[j][1];
                }
            } else {
                for(int j=min-1; j<max; j++) {
                    points[j][0] = -points[j][0];
                }
            }

        }


    }

}
